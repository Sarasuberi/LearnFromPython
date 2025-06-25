# Numpy库的基本介绍与安装
# numpy文档：https://numpy.org/doc/stable/reference/index.html#other-topics
# pandas文档：https://pandas.pydata.org/docs/reference/index.html#api
# %%
# 创建数组的几种方式

import numpy as np

a = np.array([1, 2, 3, 4])  # np.array(列表)
b = np.arange(1, 10, 2)  # np.arange(起点，终点，步长)
c = np.random.random((2, 3))  # np.random.random((行,列))
d = np.random.randint(0, 9, (4, 5))  # np.random.randint(起点，终点，(行,列))

print(a)
print(b)
print(c)
print(d)

# %%
# 数组和列表的区别
# 数组元素要求相同类型，列表元素类型可以不同
# 数组可以与标量进行运算，数组之间也可以进行矢量化运算
# 数组在运算时具有广播能力
# 数组的存储效率更高，节省内存空间

import numpy as np

a = [1, 2, 3]
b = np.array([1, 2, 3])
c = [2, 4, 6]
d = np.array([2, 4, 6])

print(a, type(a))  # [1, 2, 3] <class 'list'>
print(b, type(b))  # [1 2 3] <class 'numpy.ndarray'>

r_a_c = a + c
r_b_d = b + d
print(r_a_c, type(r_a_c))  # [1, 2, 3, 2, 4, 6] <class 'list'>
print(r_b_d, type(r_b_d))  # [3 6 9] <class 'numpy.ndarray'>

# %%
# 特殊函数
# np.zeros((行,列))  生成全0数组
# np.ones((行,列))   生成全1数组
# np.empty((行,列))  生成未初始化的数组
# np.full((行,列), 值)  生成指定值数组
# np.eye((行,列))  生成对角线为1的数组

import numpy as np

a = np.zeros((2, 3))
b = np.ones((2, 3))
c = np.empty((2, 3))
d = np.full((2, 3), 5)
e = np.eye(4)

print(a)
print(b)
print(c)
print(d)
print(e)

# %%
# 数据类型
# bool_  布尔类型
# intc  整数类型与C的int类型一样，一般是int32或者int64
# intp  用于索引的整数类型（类似于C的ssize_t,一般情况下任然是int32或者int64）
# int_  整数类型 int16, int32, int64
# float_  浮点类型 float16, float32, float64
# uint_  无符号整数类型 uint16, uint32, uint64
# complex_  复数类型 complex64, complex128
# numpy的数值类型实际上是dtype对象的实力，并对应唯一的字符

import numpy as np

dt_b = np.dtype("?")
dt_bool = np.dtype(np.bool_)

print(dt_b)  # bool
print(dt_bool)  # bool

# 把数据类型结构化
dt = np.dtype([('score', np.int16)])
a = np.array([10, 20, 30], dtype=dt)

print(dt)
print(a)

# %%
# 结构化数据类型
# 1.定义一个结构化数据类型：字符字段：名字，整数字段：年龄，浮点数字段：身高
# 2.讲这个结构化数据类型应用到ndarray对象

import numpy as np

dt_type = np.dtype([('name', np.str_, 20), ('age', 'i4'),
                    ('height', np.float32)])
ndarray = np.array([('Tom', 21, 178.5), ('Jerry', 18, 165.5)], dtype=dt_type)

print(dt_type)
print(ndarray)

# %%
# 设置以及查询数据类型
# 数组只能有一种是数据类型，如果不设置数据类型的话，类型按最高精度默认

import numpy as np

a = np.array([1, 2, 3, 4], dtype='S20')
r_a = a[0].decode('utf-8')
b = np.array([1, 2.2222, 3, 4])

print(a)  # [b'1' b'2' b'3' b'4'] byte 数据类型 字符串
print(r_a, type(r_a))  # 1 <class 'str'>
print(a.dtype)  # |S20
print(b.dtype)  # float64

# %%
# 修改数据类型
# 不同的数据类型有利于处理海量数据，针对不同数据赋予不同数据类型，从而节省内存空间

import numpy as np

a = np.array([1, 2, 3, 4], dtype=np.int8)
f = a.astype(np.float32)

print(a, a.dtype)  # [1 2 3 4] int8
print(f, f.dtype)  # [1. 2. 3. 4.] float32

# %%
# 数据维度与检测
# 用ndim属性检测数组的维度

import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array([[1, 2], [3, 4]])
c = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

print(f"a:{a}")
print(f"b:{b}")
print(f"c:{c}")
print(a.ndim)  # 1
print(b.ndim)  # 2
print(c.ndim)  # 3

# %%
# 数组形状查询
# 用shape属性查询数组的形状
# shape是个元组，返回每个维度中元素的数量

import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array([[1, 2, 3], [3, 4, 3]])
c = np.array([[[1, 2, 3], [3, 4, 5]], [[5, 6, 7], [7, 8, 9]]])

print(a.shape)  # (4,)
print(b.shape)  # (2, 3)
print(c.shape)  # (2, 2, 3)

# %%
# 修改数组形状
# 用reshape方法修改数组形状
# 不改变数据的条件下修改形状
# numpy.reshape(a, newshape, order='C')
# a: 要修改形状的数组
# newshape: 整数或整数元组，新的形状应该与原始数组元素数量一致
# order: 'C' -- 按行，'F' -- 按列，'A' -- 原顺序，'K' -- 元素在内存中的出现顺序

import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array([[1, 2], [3, 4]])
c = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

print(a.reshape(2, 2))  # [[1 2] [3 4]]
print(b.reshape(1, 4))  # [[1 2 3 4]]
print(c.reshape(4, 2))  # [[1 2] [3 4] [5 6] [7 8]]
print(np.reshape(a, (2, 2), order='F'))  # [[1 3] [2 4]]
print(np.reshape(c, (8, ), order='F'))  # [1 5 3 7 2 6 4 8]

# %%
# 数组元素迭代器
# 用flat属性获取数组元素迭代器
# numpy.flat

import numpy as np

a = np.arange(9)
a2 = a.reshape(3, 3)

for x in a2:
    print(x)

for i in a.flat:
    print(i)

# %%
# 数组扁平化
# 用flatten方法返回一份数组拷贝，对拷贝所做的修改不会影响原始数组
# 用ravel方法返回展开的一维数组

import numpy as np

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
r_a = a.reshape(-1)
r_a[0] = 100
a2 = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
r_a2 = a2.flatten()
r_a2[0] = 200
a3 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
r_a3 = a3.ravel()
r_a3[0] = 300

print(r_a)  # [100 2 3 4 5 6 7 8]
print(a)  # [[100 2 3 4] [5 6 7 8]]
print(r_a2)  # [200 2 3 4 5 6 7 8]
print(a2)  # [[1 2] [3 4] [5 6] [7 8]]
print(r_a3)  # [300 2 3 4 5 6 7 8]
print(a3)  # [[[300 2] [3 4]] [[5 6] [7 8]]]

# %%
# numpy数组元素个数与所占内存
# 用size属性查询数组元素个数
# 用itemsize属性查询数组元素所占字节
# np.size * np.itemsize可以计算数组所占总内存空间

import numpy as np

a = np.array([1, 2, 3, 4])
a_s = a.size
a_i = a.itemsize
a_m = a_s * a_i
b = np.array([[1, 2], [3, 4]])
b_s = b.size
b_i = b.itemsize
b_m = b_s * b_i
c = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
c_s = c.size
c_i = c.itemsize
c_m = c_s * c_i

print(a)  # [1 2 3 4]
print(a_s)  # 4
print(a_i)  # 8
print(a_m)  # 32
print(b)  # [[1 2] [3 4]]
print(b_s)  # 4
print(b_i)  # 8
print(b_m)  # 32
print(c)  # [[[1 2] [3 4]] [[5 6] [7 8]]]
print(c_s)  # 8
print(c_i)  # 8
print(c_m)  # 64

# %%
# numpy数组所占有的实际内存
# 用nbytes属性查询数组所占内存
# sys.getsizeof()这个方法以字节为单位返回对象的大小

import numpy as np
import sys

a = np.array([1, 2, 3, 4])
r_a = sys.getsizeof(a)
b = np.array([[1, 2], [3, 4]])
r_b = sys.getsizeof(b)
c = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
r_c = sys.getsizeof(c)

print(a.nbytes)  # 32
print(r_a)  # 144
print(b.nbytes)  # 32
print(r_b)  # 160
print(c.nbytes)  # 64
print(r_c)  # 208

# %%
# numpy一维数组的索引和切片
# 数组[1,2,3,4,5]
# 索引 0,1,2,3,4
# 正索引 & 负索引
# 正向切片 & 反向切片 [开始：结尾：步长]
# 负索引和反向切片就是从后往前取值

import numpy as np

a = np.arange(1, 10)

print(a[3])  # 4
print(a[-3])  # 7
print(a[1:3])  # [2 3]
print(a[1:3:2])  # [2]
print(a[::2])  # [1 3 5 7 9]
print(a[::-1])  # [9 8 7 6 5 4 3 2 1]
print(a[-5:-1])  # [5 6 7 8]

# %%
# numpy二维数组的索引

import numpy as np

a2 = np.array([[1,2],[3,4],[5,6],[7,8]])

# 获取某一行的数据：数组[索引]
print(a2[1])  # [3 4]
# 获取某一列的数据：数组[:,索引]
print(a2[:,1])  # [2 4 6 8]
# 获取某一行某一列的数据：数组[行,列]
print(a2[1,1])  # 4
print(a2[1][0])  # 3
# 获取某几行的数据：数组[开始行:结束行]
print(a2[1:3])  # [[3 4] [5 6]]
# 获取某行和某行的数据：数组[[行索引，行索引]]
print(a2[[0,2]])  # [[3 4] [5 6]]
# 获取某几行的某一列的数据：数组[开始行:结束行,索引]
print(a2[1:3,1])  # [4 6]
# 获取某几行某几列的数据：数组[开始行:结束行,开始列:结束列]
print(a2[1:3,0:2])  # [[3 4] [5 6]]
# 获取多个某行谋列数据：数组[[行索引，行索引]，[列索引]，[列索引]]
print(a2[[1, 2, 3], [0, 1, 0]])  # [3 6 7]


# %%
# 二维数组的切片以及倒索性
# 对行的切片：start:stop:step
# 对列的切片：:，start:stop:step

import numpy as np

a3 = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])

# 切几行数据：数组[索引：索引]
print(a3[1:3])  # [[5 6 7 8] [9 10 11 12]]
# 获取某一列全部数据：数组[:,索引]
print(a3[:, 1])  # [2 6 10 14]
# 获取多列数据：数组[:, [列索引，列索引]]
print(a3[:, [0, 2]])  # [[1 3] [5 7] [9 11] [13 15]]
# 所有行所有列：数组[:, :]
print(a3[:, :])  # [[1 2 3 4] [5 6 7 8] [9 10 11 12] [13 14 15 16]]
# 所有行部分列：数组[：,列索引]
print(a3[:, 1])  # [ 2  6 10 14]
# 所有行的第一列和第二列：数组[：，0:2]
print(a3[:, 0:2])  # [[1 2] [5 6] [9 10] [13 14]]
# 获取第二行所有列：数组[1, :]
print(a3[1, :])  # [5 6 7 8]
# 获取第一和第二行所有列：数组[[0, 1], :]
print(a3[[0, 1], :])  # [[1 2 3 4] [5,6,7,8]]
# 获取奇数行所有列：数组[::2, :]
print(a3[::2, :])  # [[1 2 3 4] [9 10 11 12]]
# 数组[-1] = 最后一行
print(a3[-1])  # [13 14 15 16]
# 数组[::-1] = 行倒序
print(a3[::-1])  # [[13 14 15 16] [9 10 11 12] [5 6 7 8] [1 2 3 4]]
# 数组[::-1,::-1] = 行倒序，列倒序
print(a3[::-1, ::-1])  # [[16 15 14 13] [12 11 10 9] [8 7 6 5] [4 3 2 1]]

# %%
# numpy布尔索引
# 用布尔数组索引数组元素
# 可以通过一个布尔数组来索引目标数组，以此找出布尔数组中值为True的对应目标数组中的数据

import numpy as np

arr = np.arange(7)
arr_bool = np.array([True,False,False,False,True,True,False]) # 用布尔值去索引数组
arr_num = np.array([0,4,5]) # 用数组去索引

print(arr[arr_bool])  # [0 4 5]
print(arr[arr_num])  # [0 4 5]
print(arr)  # [0 1 2 3 4 5 6]

# %%
# numpy二维数组的布尔索引

import numpy as np

arr = np.arange(28).reshape(7,4)
arr_bool = np.array([True, False, True, False, False, False,
                     True])  # 二维当中对应的行

print(arr)
print(arr[arr_bool])  # [[ 0  1  2  3] [ 8  9 10 11] [16 17 18 19]]
# %%
# 数据清洗

import numpy as np

arr = np.arange(28).reshape(7, 4)
arr_name = np.array(['Tom', 'Jerry', 'Tom', 'Jerry', 'Tom', 'Jerry', 'Tom'])
print(arr_name == 'Tom')  # [ True False  True False  True False  True]
arr_bool = np.array([True, False, True, False, True, False, True])
print(arr[arr_bool])  # [[ 0  1  2  3] [ 8  9 10 11] [16 17 18 19] [24 25 26 27]]

# %%
