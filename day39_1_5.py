# Numpy库的基本介绍与安装
# numpy文档：https://numpy.org/doc/stable/reference/index.html#other-topics
# pandas文档：https://pandas.pydata.org/docs/reference/index.html#api
# %%
# 创建数组的几种方式


import numpy as np

a = np.array([1, 2, 3, 4])          # np.array(列表)
b = np.arange(1, 10, 2)             # np.arange(起点，终点，步长)
c = np.random.random((2,3))         # np.random.random((行,列))
d = np.random.randint(0,9,(4,5))    # np.random.randint(起点，终点，(行,列))

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

a = [1,2,3]
b = np.array([1,2,3])
c = [2,4,6]
d = np.array([2,4,6])

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

a = np.zeros((2,3))
b = np.ones((2,3))
c = np.empty((2,3))
d = np.full((2,3), 5)
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

print(dt_b)     # bool
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

dt_type = np.dtype([('name', np.str_,20), ('age', 'i4'), ('height', np.float32)])
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
# %%
# 数据维度与检测
# %%
# 数组形状查询
# %%
# 修改数组形状
# %%
# 数组元素迭代器
# %%
# 数组扁平化
# %%
# numpy数组元素个数与所占内存
# %%
# numpy数组所占有的实际内存
# %%
# numpy一维数组的索引和切片
# %%
# numpy二维数组的索引
# %%
# 二维数组的切片以及倒索性
# %%
# numpy布尔索引
# %%
# numpy二维数组的布尔索引和数据清洗
# %%
