# 并发编程 -- 线程
# 线程与进程
# 一个进程是操作系统中运行的一个任务
# 1. 当前的操作系统基本都支持多进程并发
# 2. 进程拥有独立的cpu、内存等资源
# 一个线程是一个进程中运行的一个任务
# 1. 一个进程中同样可以同时并发多个任务
# 2.线程之前共享进程的cpu、内存资源
# 创建线程
# 给线程传递参数


from threading import Thread


def task(count: int):
    for n in range(count):
        print(n)

thread1 = Thread(target=task, args=(10,))
thread2 = Thread(target=task, args=(20,))

thread1.start() # 启动线程
thread2.start()

thread1.join()  # 等待thread1线程执行完毕
thread2.join()  # 等待thread2线程执行完毕
print("Main threads is end")