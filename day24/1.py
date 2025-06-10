from functools import wraps
# 装饰器
# 自定义装饰器
# @wraps装饰器
# 在装饰器中的函数名称如果被打印会被装饰器隐藏。使用@wraps装饰器可以使得原有的函数名称显现出来
# 带参数的装饰器

# def welcome(fn):
#     @wraps(fn)
#     def wrapper(*args, **kwargs):
#         print("welcome")
#         return fn(*args, **kwargs)
#     return wrapper

def welcome(name:str)-> None:
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            print(f"welcome {name}")
            return fn(*args, **kwargs)
        return wrapper
    return decorator

@welcome("Alice")
def my_fun(message:str) -> None:
    print(f"Hello {message}")

@welcome("Tom")
def my_fun_2(message:str) -> None:
    print(f"my fun 2 {message}")

# f1 = welcome(my_fun)
# f1("python")

f2 = welcome(my_fun_2)
f2("Jack")

my_fun("python")

print(my_fun.__name__)

my_fun_2("info")
