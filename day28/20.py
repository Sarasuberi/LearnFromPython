# 并发编程 -- 进程池
# 进程的创建和销毁比起线程更加昂贵
# 频繁的创建和销毁线程对系统性能影响更大
# 进程池是Python提供的便于进程管理和提高性能的工具
# 使用进程池
# concurrent.futures.ProcessPoolExecutor
# 启动一个任务，返回一个Future对象
# ProcessPoolExecutor.submit(fn, *args, **kwargs)
# 启动多个任务，返回一个迭代器
# ProcessPoolExecutor.map(fn, *iterables, timeout=None)
# 关闭线程池，wait=True表示等待所有任务执行完毕
# ProcessPoolExecutor.shutdown(wait=True)
# Future
# 获取任务结果，如果任务未完成会阻塞，timeout表示最长等待时间
# result(timeout=None)
# 获取任务异常，如果任务未完成会阻塞
# exception()


import os.path
import time
from concurrent.futures import ProcessPoolExecutor
from urllib.request import urlopen, Request


def download_img(url: str):

    # 发送请求，获取网页内容
    site_url = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urlopen(site_url) as web_file:
        img_data = web_file.read()

    # 如果没有获取到图片数据，抛出异常
    if not img_data:
        raise Exception(f"Error: cannot load the image from {url}")

    # 获取图片文件名
    file_name = os.path.basename(url)

    # 将图片数据写入文件
    with open(file_name, 'wb') as file:
        file.write(img_data)

    # 返回下载成功的消息
    return f"Download image successfully, {url}"


def main():
    with ProcessPoolExecutor() as executor:
        urls = [
            "https://cdn.pixabay.com/photo/2021/09/28/13/14/cat-6664412_1280.jpg",
            "https://cdn.pixabay.com/photo/2022/11/10/00/38/creative-7581718_640.jpg",
            "https://cdn.pixabay.com/photo/2022/11/19/11/53/rose-7601873_640.jpg",
            "https://cdn.pixabay.com/photo/2022/10/18/12/05/clouds-7530090_640.jpg"
        ]

        results = executor.map(download_img, urls)

        for res in results:
            print(res)


if __name__ == "__main__":
    main()
