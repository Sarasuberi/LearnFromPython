# 闭包
# 我们把内嵌的函数和外部函数中被内嵌函数使用的变量的组合叫闭包
# 形成条件是函数中嵌套了函数并且内部函数使用了nonlocal参数


def greeting():
    message = "hello"
    value = 20

    def inner():
        print(f'{value} - {message}')

    message = "second"

    return inner


f = greeting()
print(f.__closure__)
f()