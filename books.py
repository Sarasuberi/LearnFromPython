# coding=utf-8
from bs4 import BeautifulSoup
import requests
import time
import lxml
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from urllib.parse import urljoin


# 创建带重试的session
def create_session():
    session = requests.Session()
    retry = Retry(total=3,
                  backoff_factor=0.5,
                  status_forcelist=[500, 502, 503, 504])
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    return session


# 通用选择器方案
def find_content(soup, selectors):
    for selector in selectors:
        content = soup.select(selector)
        if content:
            return content
    return []


# 获取单个页面内容
def get_single_page_content(url, selector_list, session):
    try:
        headers = {
            'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Referer': 'https://www.3yt.org/'
        }
        response = session.get(url, headers=headers, timeout=15)
        response.encoding = 'utf-8'
        if response.status_code != 200:
            print(f"请求失败: {url}, 状态码: {response.status_code}")
            return None, None
        soup = BeautifulSoup(response.text, 'html.parser')
        content = find_content(soup, selector_list)
        return soup, content
    except Exception as e:
        print(f"获取内容失败: {url}, 错误: {str(e)}")
        return None, None


# 处理分页章节内容
def process_pages(base_url, selector_list, session):
    all_content = []
    current_url = base_url
    page_count = 0
    max_pages = 2  # 防止无限循环

    while current_url and page_count < max_pages:
        soup, content = get_single_page_content(current_url, selector_list,
                                                session)

        if not content:
            print(f"未找到内容: {current_url}")
            break

        # 提取本页文本内容
        page_text = "\n".join([p.text for p in content])
        all_content.append(page_text)

        # 查找下一页链接
        next_link = None
        # 尝试找包含"下一页"文本的链接
        next_a = soup.find('a', string=lambda s: s and "下一页" in s.strip())
        if next_a:
            next_link = next_a.get('href')
        else:
            # 尝试找class包含'next'的链接
            next_a = soup.select_one('a[class*="next"], a[class*="Next"]')
            if next_a:
                next_link = next_a.get('href')
            else:
                # 尝试找最后的分页链接
                pagination = soup.select('.pagination a:last-child')
                if pagination and pagination[0].text != "当前页":
                    next_link = pagination[0].get('href')

        # 准备下一页URL
        if next_link:
            new_url = urljoin(current_url, next_link)
            # 检查避免重复请求
            if new_url == current_url:
                print(f"检测到重复URL，退出分页: {current_url}")
                break
            current_url = new_url
            page_count += 1
            print(f"找到下一页: {current_url}")
            time.sleep(1.5)  # 避免请求过快
        else:
            current_url = None

    return "\n\n".join(all_content)  # 合并所有分页内容


# 获取章节完整内容（处理分页）
def get_chapter_content(url, selector_list, session):
    soup, content = get_single_page_content(url, selector_list, session)
    if not content:
        return "[内容获取失败]"

    # 检查是否需要分页
    page_indicators = ["下一页", "下页", "next", "page", "翻页"]
    if any(ind in soup.text.lower() for ind in page_indicators):
        print(f"检测到分页结构，开始处理: {url}")
        return process_pages(url, selector_list, session)
    else:
        return "\n".join([p.text for p in content])


# 保存文件
def getValueList(url, selector_list, session):
    try:
        headers = {
            'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Referer': 'https://www.3yt.org/'
        }

        # 使用会话对象发送请求
        response = session.get(url, headers=headers, timeout=15)
        response.encoding = 'utf-8'

        if response.status_code != 200:
            print(f"请求失败: {url}, 状态码: {response.status_code}")
            return None

        # soup = BeautifulSoup(response.text, 'html.parser')
        soup = BeautifulSoup(response.text, 'lxml')

        # 调试: 保存页面源码
        # with open(f"debug_{url.split('/')[-1]}.html", "w",
        #           encoding="utf-8") as f:
        #     f.write(response.text)

        # 尝试多个选择器
        content = find_content(soup, selector_list)
        return content
    except Exception as e:
        print(f"获取内容失败: {url}, 错误: {str(e)}")
        return None


def getAllValue(urlList, selector_list, base_url, session):
    start_time = time.time()
    result = ""
    for zjName in urlList:
        if not zjName.get('href'):
            print(f"章节缺少链接: {zjName.text}")
            continue

        # 构建完整URL
        full_url = urljoin(base_url, zjName['href'])
        zjName_list = []
        if zjName.text not in zjName_list:
            print(f"开始获取: {zjName.text} ({full_url})")

            # 获取章节内容（包含分页处理）
            content = get_chapter_content(full_url, selector_list, session)
            result += f"{zjName.text}\n{content}\n\n"

            # 保存章节名字避免重复获取
            zjName_list.append(zjName.text)
            print(f"完成获取: {zjName.text}")
        else:
            print(f"章节已获取，跳过: {zjName.text}")

        # # 获取内容
        # content = getValueList(full_url, selector_list, session)

        # if content:
        #     # 处理多个匹配结果的情况
        #     text_content = "\n".join(
        #         [p.text
        #          for p in content]) if len(content) > 1 else content[0].text
        #     result += f"{zjName.text}\n{text_content}\n\n"
        #     print(f"成功获取: {zjName.text}")
        # else:
        #     result += f"{zjName.text}\n[内容获取失败]\n\n"
        #     print(f"获取失败: {zjName.text}")

        time.sleep(2)  # 合理延迟

    end_time = time.time()
    print(f"获取章节耗时: {end_time - start_time:.2f} 秒")

    return result


def saveFile(fileName, fileValue):
    with open(fileName, 'w', encoding="utf-8") as f:  # 改用覆盖写入
        f.write(fileValue)
    print(f"文件已保存: {fileName}")


def main():
    # 主URL和基础URL
    # url = "https://www.3yt.org/ml/94328"  # 快穿系统之反派BOSS来袭
    # url = "https://www.3yt.org/ml/63543"  # 快穿：男神，有点燃
    # url = "https://www.3yt.org/ml/172981" # 欢迎来到我的地域
    url = "https://www.3yt.org/ml/268476/"
    base_url = url.rsplit('/', 1)[0] + '/'  # 获取基础URL

    # 备用选择器列表
    selector_list = [
        '#htmlContent',  # 原选择器
        '#chapterContent',  # 常见变体
        '.article-content',  # 类选择器
        '.novel-content',  # 小说内容
        '[id*="content"]',  # 包含content的id
        '[class*="content"]'  # 包含content的类
    ]

    session = create_session()

    # 获取目录列表
    urlList = getValueList(url, ['dd > a'], session)
    if not urlList:
        print("目录获取失败！")
        return

    # 获取所有章节
    start_time = time.time()
    jzValue = getAllValue(urlList, selector_list, base_url, session)
    end_time = time.time()
    deplete_time = end_time - start_time
    print(f"获取所有章节总耗时: {deplete_time:.2f} 秒")
    print(f"获取所有章节总字数: {deplete_time / 60:.2f} 分钟")

    # 保存结果
    if jzValue:
        saveFile("健身教练！.txt", jzValue)
    else:
        print("未获取到任何章节内容！")


if __name__ == "__main__":
    main()
