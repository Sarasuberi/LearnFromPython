# yield from
# yield from用法1：在一个生成器中yield另一个生成器的内容
# yield与send
# 调用生成器的send相当于调用next的同时给生成器发送数据
# yield from用法2：在一个生成器中yield from一个可迭代对象


# %%
def magic_number(exponent: int):
    for n in range(3):
        yield (n + 1) ** exponent

def magic_data():

    yield from magic_number(2)
    #上下两段代码等价
    # for n in magic_number(2):
    #     yield n

    yield from magic_number(3)

for n in magic_data():
    print(n)
# %%

# 定义一个名为magic_two的函数
def magic_two():
    # 使用yield关键字生成一个值，并等待接收一个值
    exponent = yield 'Please give an exponent based on two'
    while True:
        # 使用yield关键字生成一个值，并等待接收一个值
        exponent = yield 2 ** exponent
        # 如果接收到的值为None，则跳出循环
        if exponent is None:
            break

m = magic_two()
print(next(m))

print(m.send(2))

print(m.send(3))

try:
    m.send(None)
except StopIteration:
    pass
# %%

def magic_three():
    exponent = yield 'Please give an exponent based on three'

    while True:
        exponent = yield 3 ** exponent

        if exponent is None:
            break

def magic_switch():
    option = yield 'Please choose, 1 - two, 2 - three'

    while True:
        if option == 1:
            yield from magic_two()
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
