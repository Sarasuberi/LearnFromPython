"""这是个爬虫软件"""
import time
import re
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import requests


HEADERS = {
            'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
                AppleWebKit/537.36 (KHTML, like Gecko)\
                Chrome/91.0.4472.124 Safari/537.36'                                                                                                                                                                                                                                                                                                                                                                                                                                                                           ,
            'Referer': 'https://www.3yt.org/'
        }

def create_session():
    """创建带重试的session"""

    session = requests.Session()
    retry = Retry(total=3,
                  backoff_factor=0.5,
                  status_forcelist=[500, 502, 503, 504])
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    return session

def find_content(soup, selectors):
    """通用选择器方案"""
    for selector in selectors:
        content = soup.select(selector)
        if content:
            return content
    return []

def get_single_page_content(url, selector_list, session):
    """获取单个页面内容"""
    try:
        headers = HEADERS
        response = session.get(url, headers=headers, timeout=15)
        response.encoding = 'utf-8'
        if response.status_code != 200:
            print(f"请求失败: {url}, 状态码: {response.status_code}")
            return None, None
        soup = BeautifulSoup(response.text, 'html.parser')
        content = find_content(soup, selector_list)
        return soup, content
    except ValueError as e:
        print(f"获取内容失败: {url}, 错误: {str(e)}")
        return None, None

def process_pages(base_url, selector_list, session):
    """处理分页章节内容"""
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

def get_chapter_content(url, selector_list, session):
    """获取章节内容（处理分页）"""
    soup, content = get_single_page_content(url, selector_list, session)
    if not content:
        return "[内容获取失败]"

    # 改进分页检测逻辑
    def has_pagination_indicator(soup):
        # 检查是否有下一页文本
        if soup.find(string=lambda s: s and any(
                ind in s.strip().lower() for ind in ["下一页", "下页", "next"])):
            return True

        # 检查下一页按钮
        next_buttons = soup.select(
            'a[href*="page"], a[href*="next"], a[class*="next"]')
        if next_buttons:
            return True

        # 检查页码控件
        pagination = soup.select('.pagination, .page-links, .pager')
        if pagination and len(pagination[0].find_all('a')) > 1:
            return True

        return False

    # 检查是否需要分页
    if has_pagination_indicator(soup):
        print(f"检测到分页结构，开始处理: {url}")
        return process_pages(url, selector_list, session)
    return "\n".join([p.text for p in content])

"""
def get_chapter_content(url, selector_list, session):
    获取章节内容（处理分页）
    # 调用get_single_page_content函数，获取网页内容和soup对象
    soup, content = get_single_page_content(url, selector_list, session)
    # 如果内容为空，返回内容获取失败
    if not content:
        return "[内容获取失败]"

    # 检查是否需要分页
    page_indicators = ["下一页", "下页", "next", "page", "翻页"]
    if any(ind in soup.text.lower() for ind in page_indicators):
        print(f"检测到分页结构，开始处理: {url}")
        return process_pages(url, selector_list, session)
    else:
        return "\n".join([p.text for p in content])
"""

def get_value_list(url, selector_list, session):
    """获取所有章节链接"""
    try:
        headers = HEADERS

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

        chapter_links = []
        found_first_chapter = False

        # 通过选择器筛选章节链接
        content = find_content(soup, selector_list)

        # 找到第一章开始保存链接
        for title in content:
            if not found_first_chapter :
                if re.match(r"^第1章", title.text):
                    found_first_chapter = True
                    chapter_links.append(title)
            else:
                chapter_links.append(title)

        return chapter_links
    except ValueError as e:
        print(f"获取内容失败: {url}, 错误: {str(e)}")
        return None

def get_all_value(uril_list, selector_list, base_url, session):
    """获取所有章节内容"""
    # 准备一些参数
    start_time = time.time()
    result = ""
    chapter_name_list = []

    # 开始获取章节内容
    for chapter in uril_list:
        if not chapter.get('href'):
            print(f"章节缺少链接: {chapter.text}")
            continue

        # 构建完整URL
        full_url = urljoin(base_url, chapter['href'])
        if chapter.text not in chapter_name_list:
            print(f"开始获取: {chapter.text} ({full_url})")

            # 获取章节内容（包含分页处理）
            content = get_chapter_content(full_url, selector_list, session)
            result += f"{chapter.text}\n{content}\n\n"

            # 保存章节名字避免重复获取
            chapter_name_list.append(chapter.text)
            print(f"完成获取: {chapter.text}")
        else:
            print(f"章节已获取，跳过: {chapter.text}")

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

def save_file(file_name, file_value):
    """保存文件"""
    with open(file_name, 'w', encoding="utf-8") as f:  # 改用覆盖写入
        f.write(file_value)
    print(f"文件已保存: {file_name}")

# 文本格式化函数：根据标点符号进行合理换行
def format_text(content):
    """
    格式化小说文本：在句末标点后添加换行，智能处理连续标点
    :param content: 原始文本内容（无换行符）
    :return: 格式化后的文本
    """

    # 步骤1: 处理复杂连续标点（包含混合标点的情况）
    def replace_complex_punctuation(match):
        """处理??, !?等连续混合标点"""
        puncs = match.group(0)
        # 当连续标点中有混合类型时，只在最后一个标点后换行
        if len(set(puncs)) > 1:  # 检查是否有多种标点
            return puncs[:-1] + f"{puncs[-1]}\n"
        return f"{puncs}\n"  # 同类型标点整体换行

    # 处理复杂连续标点（???!、？！?等）
    content = re.sub(r'([？?!！。】]{2,})', replace_complex_punctuation, content)

    # 步骤2: 处理单个句末标点和简单连续标点
    content = re.sub(r'([。？！！？])(?=[^”？\]」！。？！])', r'\1\n', content)

    # 步骤3: 特殊情况处理 - 引号、括号后的标点
    # 中文引号/括号后跟标点：在标点后换行
    content = re.sub(r'([”’\]」》】])([。？！；]|(?:[！？]{1,2}))', r'\1\2\n', content)

    # 步骤4: 处理段落开头特殊字符
    # 移除可能出现在行首的空格
    content = re.sub(r'\n\s+', '\n', content)

    # 步骤5: 处理多余的空行
    content = re.sub(r'\n{3,}', '\n\n', content)

    # 步骤6：匹配章节名称前后换行
    chapter_pattern = r'(\n第[^章节]*[章节]\s*.*?)\n(\s*\n)*'
    content = re.sub(chapter_pattern, r'\n\1\n\n', content)

    return content

def main():
    """开始爬虫内容"""
    # 主URL和基础URL
    # url = "https://www.3yt.org/ml/87750/"     # 快穿女配：反派BOSS有毒    时笙
    url = "https://www.3yt.org/ml/94328"  # 快穿系统之反派BOSS来袭    明姝
    # url = "https://www.3yt.org/ml/37642/"     # 这个大佬画风不对          初筝
    # url = "https://www.3yt.org/ml/114229/"    # 十万个氪金的理由          灵琼
    # url = "https://www.3yt.org/ml/172981"     # 欢迎来到我的地域          银苏
    # url = "https://www.3yt.org/ml/268476/"
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
    uril_list = get_value_list(url, ['dd > a'], session)
    if not uril_list:
        print("目录获取失败！")
        return

    # 获取所有章节
    start_time = time.time()
    chapter_value = get_all_value(uril_list, selector_list, base_url, session)
    end_time = time.time()
    deplete_time = end_time - start_time
    print(f"获取所有章节总耗时: {deplete_time:.2f} 秒")
    print(f"获取所有章节总字数: {deplete_time / 60:.2f} 分钟")

    # 格式化文本
    chapter_value = format_text(chapter_value)

    # 保存结果
    if chapter_value:
        save_file("健身教练！.txt", chapter_value)
    else:
        print("未获取到任何章节内容！")


if __name__ == "__main__":
    main()
