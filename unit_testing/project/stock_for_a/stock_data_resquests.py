import requests
import pandas as pd
from datetime import datetime


def get_wly_history_data() -> pd.DataFrame:
    # 请求头设置（模拟浏览器访问）
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6422.112 Safari/537.36',
        'Referer': 'https://quote.eastmoney.com/'
    }

    # 东方财富API接口（使用复权数据）
    api_url = "https://push2his.eastmoney.com/api/qt/stock/kline/get"

    # 请求参数
    params = {
        'fields1': 'f1,f2,f3,f4,f5,f6,f7,f8',
        'fields2': 'f51,f52,f53,f54,f55,f56,f57,f58,f59,f60,f61',
        'secid': '0.000858',  # 深市股票前缀0；沪市前缀1
        'klt': '101',  # 101表示日K线
        'fqt': '2',  # 1表示前复权；2表示后复权
        'beg': '19900101',  # 起始日期
        'end': '20900101',  # 结束日期
        'lmt': '100000',  # 获取全部数据
    }

    try:
        # 发送HTTP请求
        response = requests.get(api_url,headers=headers,params=params,timeout=10)
        response.raise_for_status()
        json_data = response.json()

        # 解析数据
        if json_data['data'] is None:
            print("未获取到数据，请检查股票代码或网络连接")
            return None

        klines = json_data['data']['klines']

        # 处理每行数据
        processed_data = []
        for line in klines:
            items = line.split(',')
            # 解析每个字段
            trade_date = items[0]  # 交易日期
            open_price = float(items[1])  # 开盘价
            close_price = float(items[2])  # 收盘价
            high_price = float(items[3])  # 最高价
            low_price = float(items[4])  # 最低价
            volume = int(items[5])  # 成交量(手)
            turnover = float(items[6])  # 成交额(元)
            amplitude = items[7]  # 振幅(不需要)
            change_percent = float(items[8].rstrip('%'))  # 涨跌幅(去掉百分号)
            change_amount = float(items[9])  # 涨跌额
            turnover_rate = items[10]  # 换手率(不需要)

            # 计算昨日收盘价（当日收盘价 - 涨跌额）
            prev_close = round(close_price - change_amount, 2)

            # 转换成交量为"手"到"股"（东方财富接口返回的成交量单位是手）
            volume_shares = volume * 100

            # 转换成交额为"元"到"万元"（东方财富接口返回的成交额单位是元）
            turnover_ten_thousand = turnover / 10000

            # 添加到数据集
            processed_data.append([
                trade_date, open_price, high_price, low_price, close_price,
                prev_close, change_amount, change_percent, volume,
                turnover_ten_thousand
            ])

        # 创建DataFrame
        df = pd.DataFrame(processed_data,
                          columns=[
                              '交易日期', '开盘价', '最高价', '最低价', '收盘价', '昨收价',
                              '涨跌额', '涨跌幅(%)', '成交量(手)', '成交额(万元)'
                          ])

        # 按日期升序排列
        df.sort_values(by='交易日期', ascending=True, inplace=True)

        return df

    except Exception as e:
        print(f"获取数据失败: {e}")
        return None


if __name__ == "__main__":
    print("开始获取五粮液(000858)历史交易数据...")
    wly_data = get_wly_history_data()

    if wly_data is not None:
        # 生成时间戳文件名
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"五粮液股票历史数据_{timestamp}.csv"

        # 保存为CSV文件
        wly_data.to_csv(filename, index=False, encoding='utf-8')
        print(f"数据已成功保存到 {filename}")
        print(f"共获取 {len(wly_data)} 条记录")
    else:
        print("未能获取数据，请重试")
