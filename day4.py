import requests

def price_grade_level(grade : int) -> str:
    # grade是形参 传入进来的值是实参
    # ->str 方便阅读代码，表示返回值是字符串类型
    if grade >= 90:
        print('Excellent')
    else:
        return 'Pass'

def display_grade_level(level):
    print(f'your grade level is {level}')

def greeting():
    print('Hello, world!')

price_grade_level(90)
print(price_grade_level(60))
display_grade_level(price_grade_level(60))
greeting()

def send_email(tarfet:str,title:str,body:str,cc=''):
    pass
send_email('test@email.com','hello','body')
send_email('test@email.com','hello','body','cc@email.com')
def pow(num:int,p:int = 2): #默认参数
    return num ** p
pow(2,3)
pow(2)

# %%
# Lanmda表达式
# lambda 定义一个匿名函数
# lambda 参数列表: 表达式
# def anonymous(参数列表):return 表达式
def my_func(name):
    return f'Hello, {name}'

f = my_func
print(f('Tom'))

ff = lambda name: f'Hello, {name}'
print(ff('Jack'))


def display(name, greeting):
    print(greeting(name))


display('Jerry', lambda name: f'Hello, {name}')
# %%
callable_lambda = []
callable = []

for i in range(1, 4):
    callable_lambda.append(lambda: i)
for f in callable_lambda:
    print(f())
for i in range(1, 4):
    callable.append(i)
for ff in callable:
    print(ff)

# %%
name_list = ['Jack', 'Tom', 'Jerry']
print(f'name_list:{name_list}')
print(f'name_list[1]:{name_list[1]}')
print(f'name_list[-1]:{name_list[-1]}')

for name in name_list:
    print(f'for in name:{name}')

name_list.append('Tommy')  #扩充
name_list.insert(1, 'Evan')  #插入
del name_list[0]  #删除
# name_list.pop()  #弹出
# name_list.pop(0)  #弹出指定位置
# name_list.remove('Evan')  #删除指定元素
name_list[0] = 'Eve'  #修改
print(f'name_list after change:{name_list}')

# tuple是一个内容不能改变的list，定义tuple的时候使用（）
# 节省性能，不能修改，不能删除，不能添加
tuple_list = (0, 1, 2, 3, 4, 5)
tuple_name = 6, 7, 8, 9
print(type(tuple_name))
print(tuple_list[1:3])
print(tuple_list[2:])
print(tuple_list[:3])
print(max(tuple_list))
print(min(tuple_list))
print(tuple_list + tuple_name)
print(tuple_name * 2)
print(3 in tuple_name)

age_list = [18, 20, 12, 55, 35, 12, 33, 40]
print(age_list.sort())  #从小到大排序
print(age_list.sort(reverse=True))  #从大到小排序
students = [('Jack', 18), ('Tom', 20), ('Jerry', 12)]
print(students.sort(key=lambda x: x[0]))  #按照名字排序
print(students.sort(key=lambda x: x[1]))  #按照年龄排序
print(sorted(students ,key=lambda x: x[1], reverse=True))  #新建一个list并按照年龄倒序排序

nums = [3, 8, 6, 5]
n1, n2, *n3 = nums  # *表示剩余的元素
print(n1, n2, n3)

for index, n in enumerate(nums, 1):
    print(f'{index}-{n}')
# 迭代器
it = iter(nums)
print(next(it))
for n in it:
    print(n)