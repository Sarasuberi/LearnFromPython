import time
# 上下文管理器
# 什么是上下文管理器
# context manager
# 一个上下文管理器是一个对象，他定义了运行时的上下文，使用with语句来执行进入和退出上下文管理器。
# 上下文管理器协议包含方法 __enter__ 和 __exit__。
# __enter__ 方法在进入上下文管理器时被调用，__exit__ 方法在退出（释放）上下文管理器时被调用。
# 上下文管理器的主要作用是管理资源，比如文件、网络连接、锁等。
# 开 - 关   # 锁 - 释放     # 启动 - 停止   # 改变 - 重置
#
# with语句
# with context as ctx:
#     # 代码块
# 上下文对象已经被清除了
#
# 上下文管理器的协议
# 上下文管理的应用

# instance = open('sample.txt', 'r')
# with instance as f:
#     print(f.read())
# print(instance.closed)

start = time.perf_counter()
num = []
for n in range(100000):
    num.append(n ** 2)
end = time.perf_counter()
print(end - start)

class Timer:
    def __init__(self):
        self.elasped = 0

    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.perf_counter()
        self.elapsed = self.end - self.start
        return True

with Timer() as t:
    num = []
    for n in range(100000):
        num.append(n**2)
print(t.elapsed)