import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# 1.创建一个包含姓名和年龄的DataFrame，数据如下
# Tom：20
# John：25
# Amy：30
df = pd.DataFrame({
    '姓名': ['Tom', 'John', 'Amy','Tom','Jack'],
    '年龄': [20, 25, 30,23,22]
})
print(f'1.创建一个包含姓名和年龄的DataFrame:\n{df}')
print("---------------------")
print("---------------------")
# 2.显示创建的DataFrame前2行数据
print(f'2.显示创建的DataFrame前2行数据:\n{df.head(2)}')
print("---------------------")
print("---------------------")
# 3.显示创建的DataFrame后3行数据
print(f'3.显示创建的DataFrame后3行数据:\n{df.tail(3)}')
print("---------------------")
print("---------------------")
# 4.提取出名字相同的‘tom’的行，输出所有的列表头名
print(f'4.提取出名字相同的‘tom’的行:\n{df[df["姓名"] == "Tom"]}')
print(f'输出所有的列表头名:\n{df.columns}')
print("---------------------")
print("---------------------")
# 5.修改第二列的名字为‘age’
df.rename(columns={'年龄': 'age'}, inplace=True)
print(f'5.修改第二列的名字为‘age’:\n{df}')
print("---------------------")
print("---------------------")
# 6.按照姓名列进行去重
print(f'6.按照姓名列进行去重:\n{df.drop_duplicates("姓名")}')
print("---------------------")
print("---------------------")
# 7.统计年龄的平均值
print(f'7.统计年龄的平均值:\n{df["age"].mean()}')
print("---------------------")
print("---------------------")
# 8.查找年龄大于23的行
print(f'8.查找年龄大于23的行:\n{df[df["age"] > 23]}')
print("---------------------")
print("---------------------")
# 9.按照年龄降序排序
print(f'9.按照年龄降序排序:\n{df.sort_values(by="age", ascending=False)}')
print('默认是升序，ascending=False表示降序')
print("---------------------")
print("---------------------")
# 10.计算年龄的总和
print(f'10.计算年龄的总和:\n{df["age"].sum()}')
print("---------------------")
print("---------------------")
# 11.更改Jack的年龄为35，然后显示更新后的数据
df.loc[df['姓名'] == 'Jack', 'age'] = 35
print(f'11.更改Jack的年龄为25，然后显示更新后的数据:\n{df}')
print("---------------------")
print("---------------------")
# 12.删除年龄大于30的行，然后显示更新后的数据
print(f'12.删除年龄大于30的行，然后显示更新后的数据:\n{df[df["age"] <= 30]}')
print("---------------------")
print("---------------------")
# 13.将姓名列转换成list
print(f'13.将姓名列转换成list:\n{df["姓名"].tolist()}')
print("---------------------")
print("---------------------")
# 14.将姓名转换为全大写，并添加一个新的“姓名（大写）”列
df['姓名（大写）'] = df['姓名'].str.upper()
print(f'14.将姓名转换为全大写，并添加一个新的“姓名（大写）”列:\n{df}')
print("---------------------")
print("---------------------")
# 15.将DataFrame保存为csv文件
df.to_csv('pandas_80.csv', index=False)
print('15.将DataFrame保存为pandas_80.csv文件结束，请检查文件夹内文件')
print("---------------------")
print("---------------------")
# 16.查看最后2行数据
print(f'16.查看最后2行数据:\n{df.tail(2)}')
print("---------------------")
print("---------------------")
# 17.删除最后一行数据
df.drop(df.tail(1).index, inplace=True)
print(f'17.删除最后一行数据:\n{df}')
print("---------------------")
print("---------------------")
# 18.添加一行数据姓名Rose年龄20
new_row = {'姓名':'Rose', 'age':20}
df.loc[df.index.max() + 1] = new_row
print(f'18.添加一行数据姓名Rose年龄20:\n{df}')
print("---------------------")
print("---------------------")
# 19.对数据按照'年龄'列值的大小进行排序
print(f'19.对数据按照"年龄"列值的大小进行排序:\n{df.sort_values(by="age")}')
print("---------------------")
print("---------------------")
# 20.统计‘姓名’列每个字符串的长度
print(f'20.统计“姓名”列每个字符串的长度:\n{df["姓名"].apply(len)}')
df['str_len'] = df['姓名'].map(lambda x: len(x))
print(f'20.将字符串长度加入数据列表:\n{df}')
print("---------------------")
print("---------------------")
# 21.将年龄分为不同的年龄段（20一下，20-30,30以上），并统计每个年龄段的人数
df['年龄段'] = pd.cut(df['age'], bins=[0, 20, 30, float('inf')], labels=['20以下', '20-30', '30以上'])
age_count = df['年龄段'].value_counts().reset_index()
age_count.columns = ['年龄段', '人数']
print(f'21.将年龄分为不同的年龄段（20以下，20-30,30以上），并统计每个年龄段的人数:\n{age_count}')
print("---------------------")
print("---------------------")
# 22.删除年龄列
df_age = df.copy()
df_age.drop('age', axis=1, inplace=True)
print('22.axis=0表示删除行，axis=1表示删除列，inplace=True表示在原数据上修改')
print(f'22.删除年龄列:\n{df_age}')
print("---------------------")
print("---------------------")
# 23.删除含有缺失的行
df.dropna(inplace=True)
print(f'23.删除含有缺失的行:\n{df}')
print("---------------------")
print("---------------------")
# 24.计算‘年龄’，‘长度’列的均值
print(f'24.计算“年龄”，“长度”列的均值:\n{df[["age", "str_len"]].mean()}')
print("---------------------")
print("---------------------")
# 25.查找含有指定关键字的行
print(f'25.查找含有指定关键字的行:\n{df[df["姓名"].str.contains("Tom")]}')
print("---------------------")
print("---------------------")
# 26.读取本地excel数据
df = pd.read_excel('zhiwei.xlsx')
print(f'26.读取本地excel数据:\n{df}')
print("---------------------")
print("---------------------")
# 27.查看df数据前5行和后5行
print(f'27.查看df数据前5行:\n{df.head(5)}')
print(f'27.查看df数据后5行:\n{df.tail(5)}')
print("---------------------")
print("---------------------")
# 28.将‘薪资’列数据转换为最大值与最小值的平均值
df['平均薪资'] = (df['薪资'].str.split('-').str[0].astype(float) + df['薪资'].str.split('-').str[1].str.replace('k','',regex=False).astype(float)) / 2
print(f'28.将“薪资”列数据转换为最大值与最小值的平均值:\n{df}')
print("---------------------")
print("---------------------")
# 29.将数据根据‘学历’进行分组并计算平均薪资
df_grouped = df.groupby('学历')['平均薪资'].mean()
print(f'29.将数据根据“学历”进行分组并计算平均薪资:\n{df_grouped}')
print("---------------------")
print("---------------------")
# 30.将‘日期’列时间转换为‘月-日’
df['日期'] = pd.to_datetime(df['日期']).dt.strftime('%m-%d')
print(f'30.将“日期”列时间转换为“月-日”:\n{df}')
print("---------------------")
print("---------------------")
# 31.查看索引、数据类型和内存信息
print(f'31.查看索引、数据类型和内存信息:\n{df.info()}')
print("---------------------")
print("---------------------")
# 32.查看‘数值型’列的汇总统计
print(f'32.查看“数值型”列的汇总统计:\n{df.describe()}')
print("---------------------")
print("---------------------")
# 33.新增一列根据‘平均薪资’将数据分为三组
df['薪资水平'] = pd.qcut(df['平均薪资'], q=3, labels=['低', '中', '高'])
print(f'33.新增一列根据“平均薪资”将数据分为三组:\n{df}')
print("---------------------")
print("---------------------")
# 34.按照‘平均薪资’列对数据降序排序
df_sorted = df.sort_values(by='平均薪资', ascending=False)
print(f'34.按照“平均薪资”列对数据降序排序:\n{df_sorted}')
print("---------------------")
print("---------------------")
# 35.取出第13行数据
print(f'35.取出第13行数据:\n{df.iloc[12]}')
print("---------------------")
print("---------------------")
# 36.计算‘平均薪资’列的中位数
print(f'36.计算“平均薪资”列的中位数:\n{df["平均薪资"].median()}')
print("---------------------")
print("---------------------")
# 37.绘制薪资水平频率分布直方图
# x横轴是薪资水平，y纵轴是人数
print(f'37.打印现在表格\n{df}')
# df['平均薪资'].value_counts().plot(kind='bar')
# plt.show()
print("---------------------")
print("---------------------")
# 38.绘制薪资水平密度曲线
a = df['平均薪资'].value_counts()
print(f'value_conts:\n{a}')
# df['平均薪资'].value_counts().plot(kind='kde',xlim=(0,8))
# plt.show()
print("---------------------")
print("---------------------")
# 39.删除最后一列
df.drop(df.columns[-1], axis=1, inplace=True)
# 40.将df的第一列与第二列合并为新的一列
# df['合并薪资'] = df['薪资']+df['平均薪资']
df['合并字符串'] = df['姓名'] + df['学历']
print(f'40.将df的第一列与第二列合并为新的一列:\n{df}')
print("---------------------")
print("---------------------")
# 41-45.空缺
# 46.将‘日期’列设置为索引
df_data = df.set_index('日期', inplace=False)
print(f'46.将“日期”列设置为索引:\n{df_data}')
# 47.生成一个和df长度相同的随机数dataframe
df_random = pd.DataFrame(pd.Series(np.random.randint(1,8,len(df))))
print(f'47.生成一个和df长度相同的随机数dataframe:\n{df_random}')
print('---------------------')
print("---------------------")
# 48.将上一题生成dataframe与df合并
df_data = pd.concat([df_data, df_random], axis=1)
print(f'48.将上一题生成dataframe与df合并:\n{df_data}')
print('---------------------')
print("---------------------")
# 49.生成新的一列new用‘合并薪资’列减去之前生成随机数列
# df_data['平均薪资'] - df_data[0]
print(f'49.生成新的一列new用“合并薪资”列减去之前生成随机数列:\n{df_data}')
print("---------------------")
print("---------------------")
# 50.检查数据中是否含有任何缺失值
print(f'50.检查数据中是否含有任何缺失值:\n{df_data.isnull().any()}')
print("---------------------")
print("---------------------")
# 51.将‘0’列类型转换为浮点数
df_data[0] = df_data[0].astype(float)
print(f'51.将“0”列类型转换为浮点数:\n{df_data}')
print("---------------------")
print("---------------------")
# 52.计算‘平均薪资’大于5.0的次数
print(f'52.计算“平均薪资”大于5.0的次数:\n{df_data[df_data["平均薪资"] > 5.0]}')
print("---------------------")
print("---------------------")
# 53.查看每种学历出现的次数
print(f'53.查看每种学历出现的次数:\n{df["学历"].value_counts()}')
# 54.查看‘学历’共有几种
print(f'53.查看‘学历’共有几种:\n{df["学历"].value_counts().count()}')
print("---------------------")
print("---------------------")
# 55.提取‘薪资’与‘新的一列’的和大于15的最后3行
# print(f'55.提取“薪资”与“新的一列”的和大于15的最后3行:\n{df_data[(df_data["薪资"] + df_data[0]) > 15].tail(3)}')
# df1 = df['平均薪资','新的一列']
# row_sum = df1.sum(axis=1)
# row_sums = df1.apply(np.sum, axis=1)
# result = df1.iloc[row_sum > 15].tail(3)
# results = df.iloc[np.where(row_sums > 15)[0][-3:],:]
# print(f'55.提取“薪资”与“新的一列”的和大于15的最后3行:\n{results}')
# 56.读取本地excel股票表格数据
data = pd.read_csv('五粮液股票历史数据_20250728_165237.csv',encoding='utf-8')
print('56.读取本地excel股票表格数据完成，查看57题验证是否成功')
print("---------------------")
print("---------------------")
# 57.查看数据前三行
print(f'57.查看数据前三行:\n{data.head(3)}')
print(f'57.查看数据后三行:\n{data.tail(3)}')
print("---------------------")
print("---------------------")
# 58.查看每列数据缺失值情况
print(f'58.查看每列数据缺失值情况:\n{data.isnull().sum()}')
print("---------------------")
print("---------------------")
# 59.提取交易日期列含有空值的行
print(f'59.提取交易日期列含有空值的行:\n{data[data["交易日期"].isnull()]}')
print("---------------------")
print("---------------------")
# 60.输出每列缺失值具体行数
print('60.输出每列缺失值具体行数:')
for colum_name in data.columns:
    if data[colum_name].count() != len(data):
        loc = data[colum_name][data[colum_name].isnull().values==True].index.tolist()
        print(f'在"{colum_name}"列,具体第{loc}行数缺失值')
# print(f'60.输出每列缺失值具体行数:\n{data[data.isnull().any(axis=1)]}')
print("---------------------")
print("---------------------")
# 61.删除所有存在缺失值的行
data_del = data.dropna(axis=0,how='any',inplace=False)
print(f'61.删除所有存在缺失值的行:\n{data_del}')
print("---------------------")
print("---------------------")
# 62.绘制收盘价的折线图
plt.rc('font',size=8)
plt.rc('figure',figsize=(10,5),dpi=100)
# plt.plot(data['收盘价'])
print('62.查看63的图 \n')
# plt.show()
print("---------------------")
print("---------------------")
# 63.同时绘制开盘价与收盘价
# data[['开盘价', '收盘价']].plot()
print('63.同时绘制开盘价与收盘价 \n')
# plt.show()
print("---------------------")
print("---------------------")
# 64.绘制涨跌幅的直方图
# plt.hist(data['涨跌幅（%）'])
print('64.绘制涨跌幅的直方图 \n')
# plt.show()
# 65.让直方图更细致
# data['涨跌幅（%）'].hist(bins=90)
print('65.让直方图更细致 \n')
# plt.show()
# 66.以data的列名创建一个dataframe
temp = pd.DataFrame(columns=data.columns)
print(f'66.以data的列名创建一个dataframe:\n{temp}')
print("---------------------")
print("---------------------")
# 67.打印所有成交额不是数字的行
data['成交额（万元）'] = pd.to_numeric(data["成交额（万元）"], errors="coerce")
rows = data[data["成交额（万元）"].isnull()]
print(f'67.打印所有成交额不是数字的行:\n{rows}')
print("---------------------")
print("---------------------")
# 68.打印所有成交额为--的行
print(f'68.打印所有成交额为--的行:\n{data[data["涨跌额"] == "--"]}')
print("---------------------")
print("---------------------")
# 69.重置data的行号
data = data.reset_index(drop=True)
print(f'69.重置data的行号:\n{data}')
print("---------------------")
print("---------------------")
# 70.删除所有成交额（千元）为非数字的行
data = data[data["成交额（万元）"].apply(lambda x: str(x).replace(".","").isdigit())]
print(f'70.删除所有成交额（千元）为非数字的行:\n{data}')
print("---------------------")
print("---------------------")
# 71.绘制成交量的密度曲线
# data['成交量'].plot(kind='kde')
print('71.绘制成交量的密度曲线 \n')
# plt.show()
print("---------------------")
print("---------------------")
# 72.计算前一天与后一天收盘价的差值
data['收盘价差'] = data['收盘价'].diff()
print(f'72.计算前一天与后一天收盘价的差值:\n{data}')
print("---------------------")
print("---------------------")
# 73.计算前一天与后一天收盘价变化率
data['收盘价变化率'] = data['收盘价'].pct_change(fill_method=None)
print(f'73.计算前一天与后一天收盘价变化率:\n{data}')
print("---------------------")
print("---------------------")
# 74.设置日期为索引
data.set_index('交易日期',inplace=True)
print(f'74.设置日期为索引:\n{data}')
print("---------------------")
print("---------------------")
# 75.以5个数据作为一个数据滑动窗口，计算这5个数据上均值（收盘价）
data['5日均线'] = data['收盘价'].rolling(5).mean()
print(f'75.以5个数据作为一个数据滑动窗口，计算这5个数据上均值（收盘价）:\n{data}')
print("---------------------")
print("---------------------")
# 76.以5个数据作为一个数据滑动窗口，计算这5个数据总和（收盘价）
data['5日总和'] = data['收盘价'].rolling(5).sum()
print(f'76.以5个数据作为一个数据滑动窗口，计算这5个数据总和（收盘价）:\n{data}')
print("---------------------")
print("---------------------")
# 77.将收盘价5日均线、20均线与原始数据绘制在同一个图上
# data['20日均线'] = data['收盘价'].rolling(20).mean()
# data[['收盘价','5日均线','20日均线']].plot()
print('77.将收盘价5日均线、20均线与原始数据绘制在同一个图上 \n')
# plt.show()
print("---------------------")
print("---------------------")
# 78.按周为采样规则，取一周收盘价最大值
data['周最高价'] = data['最高价'].rolling(5).max()
print(f'78.按周为采样规则，取一周收盘价最大值:\n{data}')
# data['日期时间'] = pd.to_datetime(data['交易日期'])
# data.set_index('日期时间',inplace=True)
# data.index = pd.DatetimeIndex(data.index)
# res_data2 = data['收盘价'].resample('W').max()
# print(f'78.按周为采样规则，取一周收盘价最大值:\n{res_data2}')
print("---------------------")
print("---------------------")
# 79.绘制重采样数据与原始数据
plt.rcParams['font.sans-serif'] = ['SimHei'] # 解决中文乱码
plt.rcParams['axes.unicode_minus'] = False  # 解决负号'-'显示为方块的问题

# data['收盘价'].plot()
# data['收盘价'].resample('7D').max().plot()
print('79.绘制重采样数据与原始数据 \n')
# plt.show()
print("---------------------")
print("---------------------")
# 80.将数据往后移动5天
data.shift(5)
print(f'80.将数据往后移动5天:\n{data}')
print("---------------------")
print("将所有数据重新保存Excel文件")
data.to_excel('五粮液数据修改.xlsx',index=False)
