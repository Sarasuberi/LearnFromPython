"""初级练习题"""
# %%
import numpy as np
"""数组创建与基本操作"""
print("数组创建与基本操作")
print("---------------------")
# 1.创建一个长度为10的一维全零数组
zero_ten = np.zeros(10, dtype=int)
print(f"1.一维全零数组：{zero_ten}")
print("---------------------")
# 2.创建一个3x3的二维全1数组
three_three = np.ones((3, 3), dtype=int)
print(f"2.3x3二维全1数组：\n{three_three}")
print("---------------------")
# 3.创建一个5x5的单位矩阵
matrix = np.eye(5, dtype=int)
print(f"3.5x5单位矩阵：\n{matrix}")
print("---------------------")
# 4.创建一个从0到9的一维数组
one_array = np.arange(10)
print(f"4.从0到9的一维数组：{one_array}")
print("---------------------")
# 5.创建一个从10到49的一维数组
ten_four_nine = np.arange(10, 50)
print(f"5.从10到49的一维数组：{ten_four_nine}")
print("---------------------")
# 6.创建一个包含20个元素的等差数列，从0到1
arithmetic = np.linspace(0, 1, 20)
print(f"6.包含20个元素的等差数列：{arithmetic}")
# 7.创建一个3x3的随机数组(值在0-1之间)
random_three_three = np.random.rand(3, 3)
print(f"7.3x3随机数组：\n{random_three_three}")
print("---------------------")
# 8.创建一个10x10的随机数组并找出最大值和最小值
random_ten_ten = np.random.rand(10, 10)
print(f"8.10x10随机数组：\n{random_ten_ten}")
print(f"8.最大值：{random_ten_ten.max()}")
print(f"8.最小值：{random_ten_ten.min()}")
print(f"8.视频最大值：{np.max(random_ten_ten)}")
print(f"8.视频最小值：{np.min(random_ten_ten)}")
print("---------------------")
# 9.创建一个8x8的棋盘式数组(黑白相间)
chessboard = np.zeros((8, 8), dtype=int)
chessboard[1::2, ::2] = 1  # 奇数行的偶数索引位置设为1
chessboard[::2, 1::2] = 1  # 偶数行的奇数索引位置设为1
print(f"9.8x8棋盘式数组：\n{chessboard}")
print("---------------------")
# 10.创建一个自定义的5x5数组并打印其数据类型
customize = np.arange(25).reshape(5, 5)
print(f"10.自定义5x5数组：\n{customize}\n数据类型：{customize.dtype}")
print("---------------------")
# %%
import numpy as np
"""数组索引与切片"""
print("数组索引与切片")
print("---------------------")
# 1.创建一个10x10数组，并提取第3行第5列的元素
ten_ten = np.arange(100).reshape(10, 10)
print(f"1.10x10数组：\n{ten_ten}")
print("---------------------")
three_five = ten_ten[2, 4]
print(f"1.第3行第5列的元素：{three_five}")
print("---------------------")
# 2.提取一个数组的所有偶数索引元素
# 在行上：从0开始，步长为2，取所有偶数索引行。 在列上：从0开始，步长为2，取所有偶数索引列。
even_index = ten_ten[::2, ::2]
print(f"2.所有偶数索引元素：\n{even_index}")
print("---------------------")
# 3.将一个数组的所有大于5的元素替换为1，其余为0
replace = np.where(ten_ten > 5, 1, 0)
print(f"3.替换后的数组：\n{replace}")
print("---------------------")
# 4.提取一个二维数组的第2列
second_column = ten_ten[:, 1]
print(f"4.第2列：\n{second_column}")
print("---------------------")
# 5.反转一个一维数组
change_one_array = one_array[::-1]
print(f"5.反转后的一维数组：{change_one_array}")
print("---------------------")
# 6.反转一个二维数组的行
change_two_array_row = customize[::-1, :]
print(f"6.反转行后的二维数组：\n{change_two_array_row}")
print("---------------------")
# 7.反转一个二维数组的列
change_two_array_column = customize[:, ::-1]
print(f"7.反转列后的二维数组：\n{change_two_array_column}")
print("---------------------")
# 8.创建一个10x10数组，并提取其中3x3的子数组
sub_array = ten_ten[2:5, 2:5]
print(f"8.3x3子数组：\n{sub_array}")
print("---------------------")
# 9.使用布尔索引提取数组中大于5的元素
bool_index = change_two_array_column[change_two_array_column > 5]
print(f"9.bool索引大于5的元素：{bool_index}")
print("---------------------")
# 10.使用花式索引从数组中提取特定位置的元素
aa = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
# 提取1,3,5个元素
b = [0, 2, 4]
print(f"10.提取1,3,5个元素：{aa[b]}")
print("---------------------")
# %%
import numpy as np
"""数组操作"""
print("数组操作")
print("---------------------")
# 1.将两个一维数组垂直堆叠
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = np.vstack((a, b))
print(f"1.垂直堆叠后的数组：\n{c}")
print("---------------------")
# 2.将两个一维数组水平堆叠
d = np.hstack((a, b))
print(f"2.水平堆叠后的数组：\n{d}")
print("---------------------")
# 3.将一个一维数组转换为二维行向量
two_array_from_one = one_array.reshape(1, -1)
print(f"3.将一维数组转换为二维行向量：\n{two_array_from_one}")
print("---------------------")
# 4.将一个二维数组转换为一维列向量
one_vector_from_two = customize.reshape(-1, 1)
print(f"4.将二维数组转换为一维列向量：\n{one_vector_from_two}")
print("---------------------")
# 5.计算两个数组的点积
dot = np.dot(a, b)
print(f"5.点积：{dot}")
print("---------------------")
# 6.计算两个数组的元素乘积
element_multiply = np.multiply(a, b)
print(f"6.元素乘积：{element_multiply}")
print("---------------------")
# 7.计算数组的转置
print(f"7.计算数组的转置:{c.T}")
print("---------------------")
# 8.展平一个多维数组
flatten_c = c.flatten()
print(f"8.展平后的数组：{flatten_c}")
print("---------------------")
# 9.改变数组的形状而不改变数据
print("9.T属性转置数组，不改变数组数据")
print("reshape方法改变数组形状，不改变数组数据")
print("flatten方法返回一份数组拷贝，对拷贝所做的修改不会影响原始数组")
print("---------------------")
# 10.计算数组的维度
array_size = customize.ndim
print(f"10.数组是：{customize}")
print(f"10.数组的维度：{array_size}")
print("---------------------")
# %%
import numpy as np
"""综合练习"""
# 1.创建一个形状为(3,4)的二维数组，所有元素初始化为 5
arr = np.full((3, 4), 5)
print(f"1.形状为(3,4)的二维数组，所有元素初始化为 5：\n{arr}")
print("---------------------")
# 2.给定数组 arr = np.array([10，20，30，40，50])，如何获取第2个和第4个元素
arr = np.array([10, 20, 30, 40, 50])
print(f"2.第2个和第4个元素：{arr[1:4:2]}")
print("---------------------")
# 3.将一维数组 np.arange(12)转换为形状为(3,4)的二维数组
arr = np.arange(12).reshape(3, 4)
print(f"3.将一维数组转换为形状为(3,4)的二维数组：\n{arr}")
print("---------------------")
# 4.将两个数组 a = np.array([1，2，3])和b= np.array([4，5，6])垂直堆叠成一个二维数组
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = np.vstack((a, b))
print(f"4.垂直堆叠后的数组：\n{c}")
print("---------------------")
# 5.计算数组 np.array([1，2，3，4])中所有元素的平方和
arr = np.array([1, 2, 3, 4])
sum = np.sum(arr**2)
print(f"5.数组中所有元素的平方和：{sum}")
print("---------------------")
# 6.给定矩阵 A= np.array([[1，2]，[3，4]])和B= np.array([[5，6]，[7，8]]),计算它们的矩阵乘积
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
c = np.dot(a, b)
print(f"6.矩阵乘积：\n{c}")
print("---------------------")
# 7.计算数组 np.array([1，2，3，4，5，6，7，8，9])的平均值和标准差
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
mean = np.mean(arr)  # 平均值
std = np.std(arr)  # 标准差
print(f"7.平均值：{mean}\n标准差：{std}")
print("---------------------")
# 8.从数组 np.array([1，2，3，4，5，6，7，8，9])中选出所有大于5的元素
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
arr = arr[arr > 5]
print(f"8.选出所有大于5的元素：{arr}")
print("---------------------")
# 9.将一维数组 np.array([1，2，3])与二维数组 np.array([[1]，[2]，[3]])相加，解释结果
# 用到了广播机制来解决不同形状的数组之间的运算问题
a = np.array([1, 2, 3])
b = np.array([[1], [2], [3]])
# 触发广播机制
c = a + b
print(f"9.一维数组与二维数组相加：\n{c}")
print("---------------------")
# 10.生成一个形状为(3,3)的数组，其中的元素是从标准正态分布中随机抽取的
arr = np.random.randn(3, 3)
print(f"10.生成一个形状为(3,3)的数组：\n{arr}")
print("---------------------")
# %%
import numpy as np
"""基本数学运算"""
print("基本数学运算")
print("---------------------")
# 1.计算数组所有元素的和
sum = customize.sum()
print(f"1.数组所有元素的和：{sum}")
print("---------------------")
# 2.计算数组每列的和
sum_column = customize.sum(axis=0)
print(f"2.数组每列的和：{sum_column}")
print("---------------------")
# 3.计算数组每行的平均值
mean_row = customize.mean(axis=1)
print(f"3.数组每行的平均值：{mean_row}")
print("---------------------")
# 4.计算数组的标准差
std = customize.std()
print(f"4.数组的标准差：{std}")
print("---------------------")
# 5.计算数组的累积和
cumsum = customize.cumsum()
print(f"5.数组的累积和：{cumsum}")
print("---------------------")
# 6.计算数组元素的绝对值
abs_array = np.abs(customize)
print(f"6.数组元素的绝对值：\n{abs_array}")
print("---------------------")
# 7.计算数组元素的平方根
sqrt_array = np.sqrt(customize)
print(f"7.数组元素的平方根：\n{sqrt_array}")
print("---------------------")
# 8.计算数组元素的平方
square_array = np.square(customize)
print(f"8.数组元素的平方：\n{square_array}")
print("---------------------")
# 9.计算数组元素的指数
exp_array = np.exp(customize)
print(f"9.数组元素的指数：\n{exp_array}")
print("---------------------")
# 10.计算两个数组的欧几里得距离
euclidean_distance = np.linalg.norm(a - b)
print(f"10.两个数组的欧几里得距离：{euclidean_distance}")
print("---------------------")
# %%
"""中级练习题"""
# %%
import numpy as np
"""数组操作进阶"""
print("数组操作进阶")
print("---------------------")
# 1.找到数组中最大值的索引
arr = np.array([9, 7, 8, 6, 4, 5, 1, 2, 3])
max_index = np.argmax(arr)
print(f"1.数组中最大值的索引：{max_index}")
print("---------------------")
# 2.找到数组中前5个最大值的索引
top_five_max_index = np.argpartition(arr, -5)[-5:]
print(f"2.数组中前5个最大值的索引：{top_five_max_index}")
print("---------------------")
# 3.对一个数组进行归一化(0-1范围)
arr = np.array([10, 20, 30, 40, 50])
normalize_array = (arr - arr.min()) / (arr.max() - arr.min())
print(f"3.数组归一化(0-1范围)：\n{normalize_array}")
print("---------------------")
# 4.对一个数组进行标准化(均值为0，标准差为1)
standardize_array = (arr - arr.mean()) / arr.std()
print(f"4.数组标准化(均值为0，标准差为1)：\n{standardize_array}")
print("---------------------")
# 5.计算数组的移动平均值
arr = np.array([9, 7, 8, 6, 4, 5, 1, 2, 3])
avage_array = np.convolve(arr, np.ones(3) / 3, mode='valid')
print(f"5.数组的移动平均值：\n{avage_array}")
print("---------------------")
# 6.计算数组的差分
diff_array = np.diff(arr)
print(f"6.数组的差分：\n{diff_array}")
print("---------------------")
# 7.计算数组的梯度
gradient_array = np.gradient(arr)
print(f"7.数组的梯度：\n{gradient_array}")
print("---------------------")
# 8.对数组进行排序
sort_array = np.sort(arr)
print(f"8.数组的排序：\n{sort_array}")
print(f"直接调用sort的排序：\n{a.sort()}")
print("---------------------")
# 9.对数组的每行进行排序
a = np.array([[3, 1, 4], [1, 5, 9], [2, 6, 5]])
sort_row = np.sort(a, axis=1)
print(f"9.对数组的每行进行排序：\n{sort_row}")
print("---------------------")
# 10.对数组的每列进行排序
sort_column = np.sort(a, axis=0)
print(f"10.对数组的每列进行排序：\n{sort_column}")
print("---------------------")
# %%
"""逻辑操作与过滤"""
import numpy as np

print("逻辑操作与过滤")
print("---------------------")
# 1.提取数组中所有唯一元素
arr = np.array([1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6])
print(f"1.数组中所有唯一元素：\n{np.unique(arr)}")
print("---------------------")
# 2.计算数组中每个元素的出现次数
print(f"2.数组中每个元素的出现次数：\n{np.bincount(arr)}")
print("---------------------")
# 3.提取数组中所有非零元素的索引
arr = np.array([0, 1, 2, 0, 3, 0, 4, 0, 5])
print(f"3.数组中所有非零元素的索引：\n{np.nonzero(arr)}")
print("---------------------")
# 4.检查两个数组是否相等
a = np.array([1, 2, np.nan, 3])
b = np.array([1, 2, 0, 3])
print(f"4.两个数组是否相等：{np.array_equal(a, b, equal_nan=True)}"
      )  # equal_nan=True表示将nan值视为相等,有可能出错
print("---------------------")
# 5.检查数组是否有NaN值
arr = np.array([1, 2, np.nan, 4, 5])
print(f"5.数组是否有NaN值：{np.isnan(arr)}")
print(f"数组是否有NaN值的.any()方法：{np.isnan(arr).any()}")
print("---------------------")
# 6.替换数组中的所有NaN值为0
arr_nam = np.nan_to_num(arr, 0)
print(f"6.替换数组中的所有NaN值为0，方法一：\n{arr_nam}")
arr[np.isnan(arr)] = 0
print(f"替换数组中的所有NaN值为0，方法二：\n{arr}")
print("---------------------")
# 7.提取数组中所有大于平均值的数据
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
mean = np.mean(arr)
nanmean = np.nanmean(arr)  # 计算时忽略NaN值
print(f"7.数组的平均值：{mean, nanmean}")
print(f"数组中所有大于平均值的数据：\n{arr[arr > mean]}")
print("---------------------")
# 8.计算数组中满足条件的元素数量
print(f"8.数组中满足条件的元素数量：{np.nansum(arr > 7)}")
print("---------------------")
# 9.对数组应用自定义函数
print(f"9.对数组应用自定义函数：\n{np.vectorize(lambda x: x + 10)(arr)}")
print("---------------------")
# 10.使用where函数替换数组元素
print(f"10.使用where函数替换数组元素：\n{np.where(arr < 5, -1, arr)}")
print("---------------------")
# %%
"""随机数与统计"""
import numpy as np

print("随机数与统计")
print("---------------------")
# 1.生成10个0-1之间的随机数
random_ten = np.random.rand(10)
print(f"1.10个0-1之间的随机数：{random_ten}")
print("---------------------")
# 2.生成10个符合正态分布的随机数
arr = np.random.randn(10)
print(f"2.10个符合正态分布的随机数：{arr}")
print("---------------------")
# 3.生成10个整数随机数（范围1-100）
random_int = np.random.randint(1, 101, 10)
print(f"3.10个整数随机数：{random_int}")
print("---------------------")
# 4.随机打乱一个数组
random_array = np.random.permutation(random_int)
print(f"4.随机打乱数组方：{random_array}")
np.random.shuffle(random_int)
print(f"视频打乱方法：{random_int}")
print("---------------------")
# 5.从数组中进行随机抽样
random_sample = np.random.choice(random_array, 3, replace=False)
print(f"5.从数组中进行随机抽样：{random_sample}")
print("---------------------")
# 6.计算数组的百分位数
percentile_array = np.percentile(random_int, [25, 50, 75])
print(f"6.数组的百分位数：{percentile_array}")
print("---------------------")
# 7.计算数组的协方差矩阵
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
covariance_matrix = np.cov(a, rowvar=False)
print(f"7.数组的协方差矩阵：\n{covariance_matrix}")
print("---------------------")
# 8.计算数组的相关系数矩阵
correlation_matrix = np.corrcoef(a, rowvar=False)
print(f"8.数组的相关系数矩阵：\n{correlation_matrix}")
print("---------------------")
# 9.计算数组的直方图
data = np.random.normal(0, 1, 100)
histogram, bin_edges = np.histogram(data, bins=10)
print(f"9.直方图的计数：\n{histogram}")
print(f"直方图的边界：\n{bin_edges}")
print("---------------------")
# 10.计算数组的累计分布函数
data = np.random.normal(0, 1, 100)
so = np.sort(data)
df = np.arange(1, len(so) + 1) / len(so)
print(f"10.视频的方法结果：\n{df}")
cumulative_distribution = np.cumsum(histogram)
print(f"数组的累计分布函数：\n{cumulative_distribution}")
print("---------------------")
# %%
import numpy as np
"""线性代数运算"""
print("线性代数运算")
print("---------------------")
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
c = np.array([[2, -1], [-1, 2]])
# 1.计算矩阵的行列式
print(f"1.矩阵的行列式：{np.linalg.det(a)}")
print("---------------------")
# 2.计算矩阵的逆
print(f"2.矩阵的逆：\n{np.linalg.inv(a)}")
print("---------------------")
# 3.计算矩阵的特征值和特征向量
eigenvalues, eigenvectors = np.linalg.eig(a)
print(f"3.矩阵的特征值：{eigenvalues}")
print(f"3.矩阵的特征向量：\n{eigenvectors}")
print("---------------------")
# 4. 解线性方程组
print(f"4.解线性方程组：\n{np.linalg.solve(a, b)}")
print("---------------------")
# 5.计算矩阵的奇异值分解
u, s, v = np.linalg.svd(a)
print(f"5.矩阵的奇异值分解：\n u:{u},s:{s},v:{v}")
print("---------------------")
# 6.计算矩阵的QR分解
q, r = np.linalg.qr(a)
print(f"6.矩阵的QR分解：\n q:{q},r:{r}")
print("---------------------")
# 7.计算矩阵的Cholesky分解
# 需要正定矩阵
print(f"7.矩阵的Cholesky分解：\n{np.linalg.cholesky(c)}")
print("---------------------")
# 8.计算矩阵的迹
print(f"8.矩阵的迹：{np.trace(a)}")
print("---------------------")
# 9.计算矩阵的范数
print(f"9.矩阵的范数：{np.linalg.norm(a)}")
print("---------------------")
# 10.计算矩阵的秩
print(f"10.矩阵的秩：{np.linalg.matrix_rank(a)}")
print("---------------------")
# %%
"""高级练习题"""
# %%
import numpy as np
from scipy.signal import convolve2d
from scipy.ndimage import gaussian_filter
"""高级应用"""
print("高级应用")
print("---------------------")


# 1.实现一个简单的神经网络前向传播
def forward_pass(x):
    return 1 / (1 + np.exp(-x))


# 第二层神经网络向前传播
def forward_pass2(x, w1, b1, w2, b2):
    df1 = forward_pass(x @ w1 + b1)
    df2 = forward_pass(df1 @ w2 + b2)
    return df2


x = np.random.randn(3, 4)
w1 = np.random.randn(4, 5)
b1 = np.random.randn(5)
w2 = np.random.randn(5, 2)
b2 = np.random.randn(2)

print(f"1.实现一个简单的神经网络前向传播：\n{forward_pass2(x,w1,b1,w2,b2)}")
print("---------------------")
# 2.计算两个矩阵的卷积
a = np.array([1, 2, 3], [4, 5, 6], [7, 8, 9])
b = np.array([[1, 0], [0, 1]])
print(f"2.计算两个矩阵的卷积：\n{convolve2d(a,b,mode = 'valid')}")
print("---------------------")
# 3.实现图像处理中的滤波操作
a = np.random.randn(100, 100) * 255
print(f"3.实现图像处理中的滤波操作：\n{gaussian_filter(a, sigma=1)}")
print("---------------------")
# 4.计算数组的快速傅里叶变换
a = np.array([0, 1, 0, 1, 0, 1, 0, 1])
print(f"4.计算数组的快速傅里叶变换：\n{np.fft.fft(a)}")
print("---------------------")
# 5.计算数组的逆傅里叶变换
print(f"5.计算数组的逆傅里叶变换：\n{np.real(np.fft.ifft(a))}")
print("---------------------")
# 6.实现一个简单的PCA降维
# 7.计算数组的移动窗口统计量
# 8.实现数组的广播机制示例
# 9.使用NumPy实现线性回归
# 10.使用NumPy实现逻辑回归
print("---------------------")
# %%
import numpy as np
import timeit
"""性能优化"""
print("性能优化")
print("---------------------")
# 1.向量化操作替代循环
arr = np.random.rand(10**6)


# 问题：计算数组中每个元素的平方和，分别用循环和向量化操作实现，比较性能
# 循环
def square_sum_loop(arr):
    result = 0
    for x in arr:
        result += x**2
    return result


# 向量化
def square_sum_vectorized(arr):
    return np.sum(arr**2)


# 测试性能
loop_time = timeit.timeit(lambda: square_sum_loop(arr), number=10)
vectorized_time = timeit.timeit(lambda: square_sum_vectorized(arr), number=10)
print(f"循环时间：{loop_time}")
print(f"向量化时间：{vectorized_time}")
print(f"向量化比循环快：{loop_time/vectorized_time:.2f}倍")
print("---------------------")
print("---------------------")
# 2.视图与拷贝的内存优化
arr = np.random.rand(10**7)
# 问题：又一个大叔组，提取前半部分，如何避免不必要的内存拷贝
# 使用视图
view = arr[:len(arr) // 2]  # 共享原数据
print(f"视图内存占用：{view.nbytes:.2f}MB")  # 仅此数据的内存占用

# 使用拷贝
copy = arr[:len(arr) // 2].copy()
print(f"拷贝内存占用：{copy.nbytes:.2f}MB")

# 测试性能
view_time = timeit.timeit(lambda: view.sum(), number=10)
copy_time = timeit.timeit(lambda: copy.sum(), number=10)
print(f"视图时间：{view_time}")
print(f"拷贝时间：{copy_time}")
print(f"视图比拷贝快：{copy_time/view_time:.2f}倍")
print("---------------------")
print("---------------------")
# 3.选择合适的数据类型
a = np.array([100, 200, 300], dtype=np.int8)
b = np.array([100, 200, 300], dtype=np.int16)
c = np.array([100, 200, 300], dtype=np.int32)
# 问题：存储0-255范围内的整数，如何选择合适的数据类型来节省内存
print(f"int8数组：{a},内存占用：{a.nbytes:.2f}MB")
print(f"int16数组：{b},内存占用：{b.nbytes:.2f}MB")
print(f"int32数组：{c},内存占用：{c.nbytes:.2f}MB")
print("---------------------")
print("---------------------")
# 5.避免重复计算中间结果
arr = np.random.rand(10**6)
# 问题： 计算数组中每个元素的平方再求和，如何优化
print(f"正确优化代码行数：{np.sum(arr**2)}")
print("---------------------")
print("---------------------")
# %%
import numpy as np
"""综合项目"""
print("综合项目")
print("---------------------")
# 1.大型数据处理优化
# 题目： 假设你又一亿个元素浮点数组，需要计算滑动平均（窗口大小为100），如何高效实现并避免内存问题？
#   1)可以使用numpy当中的创建滑动窗口视图函数方法去处理而非副本
#   2)大型处理块可以使用将数组拆分成适当大小的块进行处理
#   3)处理边界情况，使用numpy的切片操作
#   4)提供一个内存优化方案：优化浮点数组的字节大小来减少内存占用
# 2.多维数组操作
# 题目： 给定一个形状为（1000,1000,3）的RGB图像数组，如何高效的1）转换为灰度图像？2）应用高斯模糊？3）找出所有亮度大于0.8的像素坐标
# 3.性能关键型计算
# 题目： 实现一个函数巨酸两个大型矩阵的余弦相似度矩阵，并优化性能
# 4.内存高效算法
# 题目：处理两个形状为（1M，256）的矩阵的成对距离计算，如何避免内存错误？
# 5.复杂统计计算
# 题目：实现一个函数计算大型数据集的滚动统计量（均值，标准差，偏度，峰度），窗口为100，步长为10
