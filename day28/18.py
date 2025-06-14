# 并发编程 -- 线程池
# 线程的创建和销毁相对比较昂贵
# 频繁的创建和销毁线程不利于高性能
# 线程池是Python提供的便于线程管理和提高性能的工具
# 使用线程池
# concurrent.futures.ThreadPoolExecutor
# ThreadPoolExecutor.submit(fn, *args, **kwargs)
# 启动一个任务，返回一个Future对象
# ThreadPoolExecutor.map(fn, *iterables, timeout=None)
# 启动多个任务，返回一个迭代器
# ThreadPoolExecutor.shutdown(wait=True)
# 关闭线程池，wait=True表示等待所有任务执行完毕
# Future
# Future.result(timeout=None)
# 获取任务执行结果，如果任务未完成会阻塞，timeout表示最长等待时间
# Future.exception()
# 获取任务执行过程中抛出的异常


import os.path
import time
from concurrent.futures import ThreadPoolExecutor
from urllib.request import urlopen, Request


def task(name: str):
    print(f"{name} - step 1\n", end='')
    time.sleep(1)
    print(f"{name} - step 2\n", end='')

    return f"{name} complete"

# with ThreadPoolExecutor() as executor:
#     result_1 = executor.submit(task, 'A')
#     result_2 = executor.submit(task, 'B')

#     print(result_1.result())
#     print(result_2.result())

# with ThreadPoolExecutor() as executor:
#     results = executor.map(task, ['C', 'D'])

#     for r in results:
#         print(r)

def download_img(url: str):

    # 创建一个请求对象，设置请求头为Mozilla/5.0
    site_url = Request(url, headers={"User-Agent": "Mozilla/5.0"})

    # 打开请求对象，读取网页内容
    with urlopen(site_url) as web_file:
        img_data = web_file.read()

    # 如果读取到的内容为空，抛出异常
    if not img_data:
        raise Exception(f"Error: cannot load the image from {url}")

    # 获取图片的文件名
    file_name = os.path.basename(url)

    # 以二进制写入的方式打开文件
    with open(file_name, 'wb') as file:
        file.write(img_data)    # 将读取到的内容写入文件

    # 返回下载成功的提示信息
    return f"Download image successfully, {url}"


with ThreadPoolExecutor() as executor:
    urls = [
        "https://cdn.pixabay.com/photo/2021/09/28/13/14/cat-6664412_1280.jpg",
        "https://cdn.pixabay.com/photo/2022/11/10/00/38/creative-7581718_640.jpg",
        "https://cdn.pixabay.com/photo/2022/11/19/11/53/rose-7601873_640.jpg",
        "https://cdn.pixabay.com/photo/2022/10/18/12/05/clouds-7530090_640.jpg"
    ]

    results = executor.map(download_img, urls)

    for res in results:
        print(res)