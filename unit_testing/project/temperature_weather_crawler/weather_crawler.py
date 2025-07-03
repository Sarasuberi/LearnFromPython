import os
import time
import requests
import parsel
import csv
import execjs
import pandas as pd
import pyecharts.options as opts
from pyecharts.charts import Line
from pyecharts.faker import Faker


def get_weather_for_bugs():
    """初始化一个存数据的文件，准备开始找数据"""
    # 准备一个weather.csv文件用以可视化调用
    f = open('weather.csv', 'w', encoding='utf-8', newline='')
    csv_writer = csv.DictWriter(
        f, fieldnames=['日期', '星期', '最高温度', '最低温度', '天气', '风向'])
    csv_writer.writeheader()
    """发送请求"""
    # 模拟浏览器
    headers = {
        'cookie':
        'UserId=17513556747345276; Hm_lvt_7c50c7060f1f743bccf8c150a646e90a=1751355675; \
                    HMACCOUNT=056C1DF689B4C978; Hm_lvt_30606b57e40fddacb2c26d2b789efbcb=1751355712; \
                    Hm_lvt_5326a74bb3e3143580750a123a85e7a1=1751355712; Hm_lvt_ab6a683aa97a52202eab5b3a9042a8d2=1751356421; \
                    HMACCOUNT=056C1DF689B4C978; cityPy=suzhou; cityPy_expire=1751961238; \
                    UserId=17513566819148965; \
                    Hm_lpvt_ab6a683aa97a52202eab5b3a9042a8d2=1751356682; \
                    Hm_lpvt_30606b57e40fddacb2c26d2b789efbcb=1751360580; \
                    Hm_lpvt_5326a74bb3e3143580750a123a85e7a1=1751417466; \
                    Hm_lpvt_7c50c7060f1f743bccf8c150a646e90a=1751417466',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
                        AppleWebKit/537.36 (KHTML, like Gecko) \
                        Chrome/137.0.0.0 Safari/537.36  ',
        'Referer': 'https://lishi.tianqi.com/kunshan/index.html'
    }

    years: int = 2021
    months: int = 1
    max_year: int = 2024
    max_month: int = 12

    # 遍历年份日期合并请求网址
    while months <= max_month:
        url = f"https://lishi.tianqi.com/kunshan/{years}{months:02d}.html"
        url_next = f"https://lishi.tianqi.com/monthdata/kunshan/{years}{months:02d}"

        print(f'请求地址：{url}')
        print(f'第二个请求地址：{url_next}')

        # 请求网址
        # url = 'https://lishi.tianqi.com/kunshan/202406.html'
        # url_next = 'https://lishi.tianqi.com/monthdata/kunshan/202406'
        """获取加密参数"""
        # 通过Python代码调用JS代码内容，获取加密参数
        current_dir = os.path.dirname(os.path.abspath(__file__))
        js_path = os.path.join(current_dir, 'weather.js')
        city = "kunshan"
        crypte = execjs.compile(open(js_path, encoding='utf-8').read()).call(
            'getSign', city)
        print(f'加密参数：{crypte}')

        # 请求参数
        params = {'crypte': crypte}

        # 发送请求
        response = requests.get(url=url, headers=headers)
        print(f'正在获取{years}-{months}数据...')
        print(f'数据{years}-{months}获取完成，等待5秒')
        time.sleep(5)
        response_next = requests.post(url=url_next,
                                      headers=modify_referer(months),
                                      data=params)
        print(f'正在获取{years}-{months}更多数据...')
        """获取数据"""
        # 获取响应的文本数据
        html = response.text

        # 获取相应的json数据
        json_html = response_next.json()
        """解析数据"""
        # 把获取到的html字符串，转成可解析的对象
        selector = parsel.Selector(html)

        # 提取天气所在li标签
        lis = selector.css('.inleft .tian_three .thrui li ')

        # 遍历li标签
        for li in lis:
            """提取具体每天天气详细的数据"""
            date_info = li.css(' .th200::text').get().split(
                ' ')  # 2024-06-01  星期六
            date = date_info[0]  # 日期
            week = date_info[1]  # 星期
            weather_info = li.css(
                ' .th140::text').getall()  #  26℃~18℃ 多云 东北风2级
            # 保存字典
            dit = {
                '日期': date,
                '星期': week,
                '最高温度': weather_info[0].replace('℃', ''),
                '最低温度': weather_info[1].replace('℃', ''),
                '天气': weather_info[2],
                '风向': weather_info[3]
            }

            # 保存数据
            csv_writer.writerow(dit)

        # 遍历并保存json文件内容
        for index in json_html:
            """提取具体每天天气详细的数据"""
            dit_next = {
                '日期': index['date_str'],
                '星期': index['week'],
                '最高温度': index['htemp'],
                '最低温度': index['ltemp'],
                '天气': index['weather'],
                '风向': index['WD'] + index['WS']
            }

            # 保存数据
            csv_writer.writerow(dit_next)

        print(f'数据{years}-{months}获取完成，准备下次获取......')

        # 等待2秒再继续避免出问题
        print(f'等待2秒后继续获取数据......')
        time.sleep(2)

        # 如果月份大于12了，就重置月份并且结束这次循环，开始下一年份的循环，否则月份加一
        if years == max_year and months == max_month:
            break
        elif months == max_month:
            print(f'数据{years}获取完成，重置months并且years+1......')
            months = 1
            years += 1
            print(f'等待5秒后继续获取数据......')
            time.sleep(5)
        else:
            months += 1
    # while months <= max_month:


def modify_referer(months):
    """修改Referer"""
    headers = {
        'cookie':
        'UserId=17513556747345276; Hm_lvt_7c50c7060f1f743bccf8c150a646e90a=1751355675; \
                    HMACCOUNT=056C1DF689B4C978; Hm_lvt_30606b57e40fddacb2c26d2b789efbcb=1751355712; \
                    Hm_lvt_5326a74bb3e3143580750a123a85e7a1=1751355712; Hm_lvt_ab6a683aa97a52202eab5b3a9042a8d2=1751356421; \
                    HMACCOUNT=056C1DF689B4C978; cityPy=suzhou; cityPy_expire=1751961238; \
                    UserId=17513566819148965; \
                    Hm_lpvt_ab6a683aa97a52202eab5b3a9042a8d2=1751356682; \
                    Hm_lpvt_30606b57e40fddacb2c26d2b789efbcb=1751360580; \
                    Hm_lpvt_5326a74bb3e3143580750a123a85e7a1=1751417466; \
                    Hm_lpvt_7c50c7060f1f743bccf8c150a646e90a=1751417466',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
                        AppleWebKit/537.36 (KHTML, like Gecko) \
                        Chrome/137.0.0.0 Safari/537.36  ',
        'Referer': f'https://lishi.tianqi.com/kunshan/{months:02d}.html'
    }

    return headers


def date_visualization():
    """数据可视化"""
    with open('weather.csv', 'r', encoding='utf-8') as f:
        df = pd.read_csv(f)
        df.head()
        date = df['日期'].tolist()
        high_temp = df['最高温度'].tolist()
        low_temp = df['最低温度'].tolist()

        line_chart = (Line().add_xaxis(date)
                      .add_yaxis("最高温度", high_temp,
                                areastyle_opts=opts.AreaStyleOpts(opacity=0.5))
                      .add_yaxis("最低温度",low_temp,
                                areastyle_opts=opts.AreaStyleOpts(opacity=0.5))
                      .add_yaxis("平均气温", (df['最高温度'] + df['最低温度']) / 2,
                                linestyle_opts=opts.LineStyleOpts(width=2, type_="dashed"))
                      .set_global_opts(title_opts=opts.TitleOpts(title="昆山温度折线图")))

        # 渲染为HTML文件
        output_file = "KS_Temperature_Line_Chart.html"
        line_chart.render(output_file)
        print(f"文件已保存为: {output_file}")


def main():
    """爬虫获取数据"""
    print("开始获取数据......")
    get_weather_for_bugs()
    print("获取数据完成!")
    """数据可视化"""
    date_visualization()


if __name__ == '__main__':
    main()
