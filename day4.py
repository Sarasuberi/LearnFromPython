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
