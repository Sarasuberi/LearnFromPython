from urllib.request import urlopen, Request
import os.path


class ProductService:

    def download_img(self, url: str):

        # 发送请求，获取图片数据
        site_url = Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urlopen(
                site_url
        ) as web_file:  #  使用urlopen函数打开site_url，并将返回的文件对象赋值给web_file
            img_data = web_file.read()  #  读取web_file中的数据，并赋值给img_data

        # 如果图片数据为空，则抛出异常
        if not img_data:
            raise Exception(f"Error: cannot load the image from {url}")

        # 获取图片文件名
        file_name = os.path.basename(url)

        # 将图片数据写入文件
        with open(file_name, 'wb') as file:
            file.write(img_data)

        # 返回下载成功信息
        return f"Download image successfully, {file_name}"
