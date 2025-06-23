# %%
# 判断某两个对象是否相同is&isnot
# 数字/字符串/元组     都是不可变数据类型  表面一样    完全一样
# 列表/字典/集合       都是可变数据类型    表面一样    完全不一样   其实不是同一个对象

a = "慕舟"
b = "Python"
print("String:")
print(a is b)
print(a is not b)

print("String with space:")
c = " 111"
d = "111"
print(c is d)
print(c is not d)

print("List:")
f = [1]
g = [1]
print(f is g)
print(f is not g)

aa = {"名字": "慕舟"}
bb = aa  # {"名字": "慕舟"}
print("Dict:")
print(aa is bb)
print(aa is not bb)

# %%
# 自动类型转换
# 当两个不同类型的数据进行运算时，结果会向更高精度进行计算
# 精度等级：布尔 < 整数 < 浮点数

a = 10
b = True  # 代表数字1
print(a + b)  # 11

c = 10
d = 3.14
print(c + d)  # 13.14

# %%
# 检测方法type()

a = "123"
b = 123
c = [1, 2, 3]
d = (1, 2, 3)
e = {1, 2, 3}
f = {"名字": "慕舟", "年龄": 18, "性别": "男"}
g = True
h = 3.14
print(a)  # 123
print(b)  # 123
print(c)  # [1,2,3]
print(d)  # (1,2,3)
print(e)  # {1,2,3}
print(f)  # {'名字': '慕舟', '性别': '男', '年龄': 18}
print(g)  # True
print(h)  # 3.14
print(type(a))  # <class 'str'> -> 数据是字符串类型
print(type(b))  # <class 'int'> -> 数据是整数类型
print(type(c))  # <class 'list'> -> 数据是列表类型
print(type(d))  # <class 'tuple'> -> 数据是元组类型
print(type(e))  # <class 'set'> -> 数据是集合类型
print(type(f))  # <class 'dict'> -> 数据是字典类型
print(type(g))  # <class 'bool'> -> 数据是布尔类型
print(type(h))  # <class 'float'> -> 数据是浮点数类型
print(type("123"))  # <class 'str'>

# %%
# 强制类型转换str()
# str()函数可以将其他所有类型的数据转换为字符串类型

a = "123"
b = 123
c = [1, 2, 3]
d = (1, 2, 3)
e = {1, 2, 3}
f = {"名字": "慕舟", "年龄": 18, "性别": "男"}
g = True
h = 3.14
print(str(a))  # 123
str_b = str(b)
print(str_b, type(str_b))  # 123 , <class 'str'>
str_c = str(c)
print(str_c, type(str_c))  # [1, 2, 3] , <class 'str'>
str_d = str(d)
print(str_d, type(str_d))  # (1, 2, 3) , <class 'str'>
print()  #
str_e = str(e)
print(str_e, type(str_e))  # {1, 2, 3} , <class 'str'>
str_f = str(f)
print(str_f, type(str_f))  # {'名字': '慕舟', '性别': '男', '年龄': 18} , <class 'str'>
str_g = str(g)
print(str_g, type(str_g))  # True , <class 'str'>
str_h = str(h)
print(str_h, type(str_h))  # 3.14 , <class 'str'>
print(str([1, 2, 3]))  # 实际上是"[1, 2, 3]"这样的字符串

# %%
# 强制类型转换int()&float()
# 数字类型之间可以互相转换
# 只有字符串可以转换为数字类型
# 并且字符串中的元素必须为纯数字，否则无法转换

a = 123
b = 3.67
c = True
d = "123"
e = "12.21"
rueslt_a = float(a)
print(rueslt_a)
rueslt_b = int(b)  # 不遵守四舍五入
print(rueslt_b)
rueslt_int_c = int(c)  # True -> 1, False -> 0
print(rueslt_int_c)
rueslt_float_c = float(c)  # True -> 1.0, False -> 0.0
print(rueslt_float_c)
rueslt_d = int(d)
print(rueslt_d, type(rueslt_d))  # 123 <class 'int'>
rueslt_int_e = int(e)
rueslt_float_e = float(e)
print(rueslt_int_e,
      type(rueslt_int_e))  # invalid literal for int() with base 10: '12.21'
print(rueslt_float_e, type(rueslt_float_e))  # 12.21 <class 'float'>

# %%
# 强制类型转换bool()
# 容器类型转布尔类型
#  容器类型数据：字符串，列表，元祖，字典，集合
#  非容器类型数据：数字类型，布尔类型
#  容器中为空 --> False
#  容器中有元素 --> True
# 数字类型转布尔类型
# int类型中，0为False，其他为真
# float类型中，0.0为False，其他为真
# 空格也被视为是一个字符

a = ""  # 空字符串
b = []  # 空列表
c = ()  # 空元祖
d = {}  # 空字典
e = set()  # 空集合
print(bool(a), bool(b), bool(c), bool(d),
      bool(e))  # False False False False False
bb = [123]
print(bool(bb))  # True

aa = 0
bb = 0.0
print(bool(aa), bool(bb))  # False False
cc = 233
dd = 3.14
print(bool(cc), bool(dd))  # True True

# %%
# 强制类型转换list()
# 数字类型是非容器类型，不能转换为列表
# 字符串转列表，会把字符串中的每一个字符当做列表的元素
# 元祖转列表时，会把元组中的每一个字符当做列表的元素
# 字典转列表时，只保留字典中的键
# 集合转列表时，结果是无序的，因为集合本身就是无序的

a = 123
b = "123"
c = (1, 2, 3)
d = {"名字": "慕舟", 0: 18, (1, 2, 3): "男"}
e = {1, 2, 3, "a", "b", "c"}
print(list(a))  # TypeError: 'int' object is not iterable
print(list(b))  # ['1', '2', '3']
print(list(c))  # [1, 2, 3]
print(list(d))  # ['名字', '年龄', '性别']
print(list(e))  # ['c', 1, 2, 3, 'b', 'a']

# %%
# 强制类型转换turple()
# tuple()其他类型数据转元组类型与其他类型数据转列表类型规则相同
# 数字类型是非容器类型，不能转换为元组
# 字符串转元组，会把字符串中的每一个字符当做元组的元素
# 列表转元组，会把列表中的每一个元素当做元组的元素
# 字典转元组时，只保留字典中的键
# 集合转元组时，结果是无序的，因为集合本身就是无序的

a = 123
b = "123"
c = [1, 2, 3]
d = {"名字": "慕舟", 0: 18, (1, 2, 3): "男"}
e = {1, 2, 3, "a", "b", "c"}
print(tuple(a))  # TypeError: 'int' object is not iterable
print(tuple(b))  # ('1', '2', '3')
print(tuple(c))  # (1, 2, 3)
print(tuple(d))  # ('名字', 0, (1, 2, 3))
print(tuple(e))  # ('c', 1, 2, 3, 'b', 'a')

# %%
# 强制类型转换set()
# set()其他数据类型转集合类型
# 数字类型是非容器类型，不能转换为集合
# 字符串转集合时，结果是无序的
# 列表转集合时，结果是无序的
# 元组转集合时，结果是无序的
# 字典转集合时，只保留字典中的键，结果是无序的

a = 123
b = "123456"
c = [1, 2, 3]
d = {"名字": "慕舟", 0: 18, (1, 2, 3): "男"}
e = {1, 2, 3, "a", "b", "c"}
print(set(a))  # TypeError: 'int' object is not iterable
print(set(b))  # {'4', '5', '3', '2', '6', '1'}
print(set(c))  # {1, 2, 3}
print(set(d))  # {0, '名字', (1, 2, 3)}
print(set(e))  # {'c', 1, 2, 3, 'b', 'a'}

# %%
# 强制类型转换dict()
# dict()其他转字典类型
# 数字类型是非容器类型，不能转换为字典
# 字符串不能转换成字典类型，因为字符串不能生成二级容器
# 列表转字典时，列表必须为等长二级容器，子容器中的元素个数必须为2
# 元组转字典时，元组必须为等长二级容器，子容器中的元素个数必须为2
# 集合不能转字典

a = 123
b = "123321"
c = [1, 2, 3, "abc", "你好"]
cc = [[1, 2], ["a", "b"], ["你", "好"]]
d = (1, 2, 3, "abc", "你好")
dd = ((1, 2), ("a", "b"), ("你", "好"))
e = {1, 2, 3, "a", "b", "c"}
ee = {{1, 2}, {"a", "b"}, {"你", "好"}}
# print(dict(a))    # TypeError: 'int' object is not iterable
# print(dict(b))    # dictionary update sequence element #0 has length 1; 2 is required
# print(dict(c))    # cannot convert dictionary update sequence element #0 to a sequence
print(dict(cc))  # {1: 2, 'a': 'b', '你': '好'}
# print(dict(d))    # cannot convert dictionary update sequence element #0 to a sequence
print(dict(dd))  # {1: 2, 'a': 'b', '你': '好'}
# print(dict(e))    # TypeError: unhashable type: 'set'
# print(dict(ee))   # TypeError: unhashable type: 'set'

# %%
# 判断一个对象是否是已知isinstance()
# isinstance()用来判断一个对象是否是一个已知的类型，返回是布尔值
# 如果对象的类型是已知的类型，那么就范围true，否则返回false
# isinstance(对象，对象类型)
# int(整数)，float(浮点数)，str(字符串)，bool(布尔值)，list(列表)，tuple(元组)，dict(字典)，set(集合)

a = 123
b = 3.14
c = "123"
d = True
e = [1, 2, 3]
f = {"名字": "慕舟", "性别": "男", "年龄": 18}
g = {1, 2, 3}
h = (1, 2, 3)
print(isinstance(a, int))  # True
print(isinstance(b, float))  # True
print(isinstance(c, str))  # True
print(isinstance(d, bool))  # True
print(isinstance(e, list))  # True
print(isinstance(f, dict))  # True
print(isinstance(g, set))  # True
print(isinstance(h, tuple))  # True

# %%
# Python的条件语句if
if 3 > 6:
    print("hello world")
elif 3 > 6:
    print("ni hao")
else:
    print("bye bye")

a = int(input("请输入一个数："))
if a > 0:
    print("正数")
elif a < 0:
    print("负数")
else:
    print("零")

# %%
# Python的for循环

for x in range(1, 10):
    print(f"{x} hello world")

# %%
# 双层for循环提取嵌套列表中的元素

a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in a:
    for j in i:
        print(j)

# %%
# Python的while循环

while True:
    print("hello world")
    break

# %%
# break和continue关键字在for循环中的使用

for i in range(10):
    if i == 2:
        print(i)
        continue
    elif i == 5:
        break

# %%
# break和continue关键字在while循环中的使用
while True:
    for i in range(10):
        if i == 2:
            print(i)
            continue
        elif i == 5:
            break


# %%
# pass语句
def main():
    pass


# %%
