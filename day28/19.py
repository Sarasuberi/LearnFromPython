# 并发编程 -- 多进程
# Python提供了multiprocessing模块来支持多进程
# multiprocessing.Process用于创建进程
# Process类
# start()用于启动进程
# join()用于等待进程结束

import multiprocessing
import time


# 定义一个函数task，接收两个参数name和count
def task(name: str, count: int):

    # 打印name - start，不换行
    print(f"{name} - start\n", end='')

    # 初始化result为0
    result = 0

    # 循环count次
    for n in range(count):
        result += n + 1 # 每次循环将n+1加到result上
    time.sleep(1) # 模拟耗时操作
    
    # 打印name - end with result，换行
    print(f"{name} - end with {result}")

# 定义一个函数，用于启动进程1
def start_process_1():

    # 创建一个进程，目标函数为task，参数为"A"和100
    process = multiprocessing.Process(target=task, args=["A", 100])

    # 启动进程
    process.start()

    # 等待进程结束
    process.join()

    # 打印主进程结束
    print("Main process over")

# 定义一个函数，用于启动进程
def start_process_2():

    # 定义一个列表，包含三个元组，每个元组包含一个名称和对应的计数
    args_list = [("A", 100), ("B", 99), ("C", 98)]

    # 使用列表推导式，创建一个进程列表，每个进程的目标函数为task，参数为名称和计数
    processes = [multiprocessing.Process(target=task, args=[name, count]) for name, count in args_list]

    # 遍历进程列表，启动每个进程
    for p in processes:
        p.start()

    # 遍历进程列表，等待每个进程结束
    for p in processes:
        p.join()


if __name__ == "__main__":
    # start_process_1()
    start_process_2()