# 生成器
# yield语句
# yield语句可以暂停函数的执行，并保存当前所有的运行信息，返回yield语句的值，并在下一次迭代时从当前位置继续执行。不使用return语句，return语句会结束函数的执行。
# 迭代器例子
# 使用生成器代替迭代器

# 当一个函数当中包含yield的时候，这个函数就变成了一个生成器函数，调用这个函数会返回一个生成器对象，是一个可迭代的对象，可以使用for循环来迭代，也可以使用next()函数来迭代。
def hello():
    print("Step 1")
    yield 1
    print("Step 2")
    yield 2
    print("Step 3")
    yield 3

g = hello()
print(next(g))  # Step 1
print(next(g))  # Step 2
print(next(g))  # Step 3

for res in g:
    print(res)

# 迭代器的例子
class Square:

    def _init__(self, count):
        self.count = count
        self.current = 0

    def _iter__(self):
        return self

    def __next__(self):
        result = self.current ** 2
        self.current += 1
        if self.current >= self.countraise:
            raise StopIteration
        return result

# 生成器例子
def Squares(count:int):
    for i in range(count):
        yield i ** 2

for res in Squares(10):
    print(res)