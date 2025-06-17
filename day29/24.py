# yield from
# yield from用法1：在一个生成器中yield另一个生成器的内容
# yield与send：调用生成器的send相当于调用next的同时给生成器发送数据
# yield from与send：当生成器的yield frim部分收到数据会分发给子生成器


# %%
def magic_number(exponent: int):
    for n in range(3):
        yield (n + 1)**exponent

def magic_data():

    yield from magic_number(2)
    #上下两段代码等价
    # for n in magic_number(2):
    #     yield n

    yield from magic_number(3)

for n in magic_data():
    print(n)

def magic_two():

    # 使用yield关键字生成一个值，并等待接收一个值
    exponent = yield 'Please give an exponent based on two'
    while True:
        # 循环里面完成两件事情，给send返回一个数，并且把send发送过来的数赋值给exponent

        # 使用yield关键字生成一个值，并等待接收一个值
        exponent = yield 2**exponent
        if exponent is None:
            break


m = magic_two()
print(next(m))

# 相当于把2作为消息送给了magic_two，并且调用next
print(m.send(2))

print(m.send(3))

try:
    m.send(None)
except StopIteration:
    pass

def magic_three():
    # 生成一个值，并等待用户输入一个指数
    exponent = yield 'Please give an exponent based on three'

    # 无限循环
    while True:
        # 生成一个值，并等待用户输入一个指数
        exponent = yield 3**exponent

        # 如果指数为None，则跳出循环
        if exponent is None:
            break

def magic_switch():
    # 使用yield语句生成一个字符串，提示用户选择1或2
    option = yield 'Please choose, 1 - two, 2 - three'

    while True:

        # 如果用户选择1，则调用magic_two函数，并使用yield from语句将结果返回
        if option == 1:
            yield from magic_two()

        # 如果用户选择2，则调用magic_three函数，并使用yield from语句将结果返回
        elif option == 2:
            yield from magic_three()
        else:
            break


mm = magic_switch()
print(next(mm))
print(mm.send(2))
print(mm.send(2))
print(mm.send(3))
try:
    mm.send(None)
except StopIteration:
    pass