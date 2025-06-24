# %%
# Python函数的创建及调用以及参数传递
# 创建函数的关键字def
# def 函数名(参数1,参数2,...):
# 位置参数：按照参数定义的数量和顺序进行传递，传入参数与函数列表时一一对应的
# 默认参数：在函数定义时，给参数设置默认值，如果调用没有传参则会使用默认参数,默认值只会传递一次。如果参数是可变对象例如列表，字典，则每次调用都会使用同一个对象且不会清除
# 可选参数：在函数定义时，给参数赋值
# 可变参数：在函数定义时，使用*args（多个参数）或者**kwargs（多个关键字参数）来进行传递
# 关键字参数：在函数定义时，使用“key=”给参数赋值
# 传入的参数可以是任意类型，可以是数字、字符串、列表、字典等


def abc(str: str):
    print(str)


abc("hello world")

# %%
# Python函数的位置参数


def abcd(a: int, b: int, c: int):
    print(a + b + c)


abcd(1, 2, 3)

# %%
# Python函数的默认参数
# 默认参数必须放在位置参数之后


def add(a: int, b=1, c=2):
    print(a + b + c)


add(1)
add(1, 2)
add(1, 2, 3)


# %%
# Python的关键字参数


def addkey(a: int, b=1, c=2):
    print(a + b + c)


addkey(1)
addkey(1, c=2)
addkey(1, c=3, b=4)

# %%
# Python命名关键字参数
# 命名关键字参数必须放在可变参数之后
# *表示位置参数结束，只是占用符号，没有实际意义，后面参数必须使用“key=value”的形式进行传递


def namekey(a: int, *, c, d):
    print(a)
    print(c)
    print(d)


namekey(1, c=2, d=3)

# %%
# Python的可变参数星号加参数
# *args表示可变参数，可以传递任意数量的参数，参数类型可以是任意类型
# *args会自动收集所有未匹配的位置参数到一个tuple对象中，变量名args指向了此tuple对象


def args(a, *b):
    print(a)
    print(b)


args(1, 2, 3, 4, 5)

# %%
# Python的可变参数双星号加参数
# **kwargs表示可变参数，可以传递任意数量的参数，参数类型可以是任意类型
# **kwargs会自动收集所有未匹配的关键字参数到一个dict对象中，变量名kwargs指向了此dict对象


def kwargs(a, **kwargs):
    print(a)
    print(kwargs)


kwargs(1, name="zhangsan", age=18)

# %%
# Python参数解包
# 参数数据类型是：字符串/列表/元组/集合/字典的时候可以解包
# 传递实参时，可以在序列类型的参数前添加星号，这样会自动将序列中的元素一次作为参数传递
# 传递的参数需要和函数定义的参数数量一致


str_s = "123"
list_l = [11,12,13]
tuple_t = (21,22,23)
set_s = {31,32,33}
dict_d = {"a":41,"b":42,"c":43}     # 字典解包的时候键值要和函数定义的参数名保持一致，提取键不需要名称一致
def abcc(a,b,c):
    print(a)
    print(b)
    print(c)


abcc(*str_s)
abcc(*list_l)
abcc(*tuple_t)
abcc(*set_s)
abcc(*dict_d)   # 解包字典的时候使用一个*只会提取键值，如果需要提取键值对需要使用**
abcc(**dict_d)  # 字典解包时，需要**

# %%
# 参数解包和可变参数配合使用


def abab(a,*args):
    print(a)
    print(args)


abab(1,*(2,3,4),5)

# %%
# Python函数中各种参数排列的事项
# 位置参数必须在默认参数之前，默认参数必须在命名关键字参数之前，命名关键字参数必须在可变参数之前


def aaaa(a,b=1,*args,**kwargs):
    pass

# %%
# Python的return关键字


def aaa():
    return 1, 2, 3


aaa()

# %%
# 函数的返回函数
# 函数的返回值可以用变量接收


def xyz():
    print("hello world")


rueslt = xyz()
print(rueslt)
# %%
