# 并发编程 -- 线程进阶
# 通过继承创建线程
# 守护线程
# 守护线程会在主线程结束的时候自动结束
# 主线程则需要等到所有非守护线程结束才能结束
# 守护线程一般用于非关键性的线程，比如日志
# 线程安全队列
# 线程安全队列是线程安全的队列，可以在多个线程之间共享
# queue模块中的Queue类提供了线程安全队列功能
# queue.put(item, block=True) 向队列中添加元素item，如果队列已满，则阻塞并且等待(False则是不阻塞，如果满了直接抛出异常），直到队列中有空位
# queue.put(item, timeout=3) 向队列中添加元素item，如果队列已满，则阻塞并且等待3秒，如果3秒后队列中还有空位则添加，否则抛出异常
# queue.get(block=False) 从队列中取出元素，如果队列为空，则抛出异常
# queue.get(timeout=10) 从队列中取出元素，如果队列为空，则阻塞并且等待10秒，如果10秒后队列中还有元素则取出，否则抛出异常
# queue.qsize() 返回队列中元素的个数
# queue.empty() 判断队列是否为空
# queue.full()  判断队列是否已满
# 生产者消费者线程实例
# 生产者：产生消息
# 消费者：处理消息

import time
from threading import Thread
from queue import Queue


class MyThread(Thread):
    def __init__(self, name: str, count: int):
        super().__init__()

        self.name = name
        self.daemon = True  # 设置为守护线程
        # self.setName(name)
        # self.setDaemon(True)    setDaemon和setName已经被弃用
        self.count = count

    # 重写run方法，并且在run方法里面完成你想要这条线程干的事情
    def run(self) -> None:
        for n in range(self.count):
            print(f"MyThread run:{self.name} - {n}\n", end='')
            # print(f"{self.getName()} - {n}\n", end='')
            time.sleep(0.01) # sleep单位是秒 


t_1 = MyThread("A", 10)
t_2 = MyThread("B", 10)
# t_3 = Thread(target=t_1.run, name="C", daemon=True) 等效与在init方法中添加的name和daemon参数

t_1.start()
t_2.start()

t_1.join()

class MsgProducer(Thread):
    def __init__(self, name: str, count: int, queue: Queue):

        # 初始化函数，设置线程名称、计数和队列
        super().__init__()

        # 设置线程名称
        # self.setName(name)
        self.name = name
        self.count = count
        self.queue = queue

    def run(self) -> None:
        # 运行函数，循环计数，将消息放入队列
        for n in range(self.count):
            msg = f"{self.name} - {n}"
            # msg = f"{self.getName()} - {n}"
            self.queue.put(msg, block=True)

class MsgConsumer(Thread):

    # 定义一个消息消费者类，继承自Thread类
    def __init__(self, name: str, queue: Queue):

        # 初始化方法，传入线程名称和队列
        # 调用父类的初始化方法
        super().__init__()

        # 设置线程名称
        # self.setName(name)
        self.name = name

        # 设置线程队列
        self.queue = queue

        # 设置线程为守护线程
        # self.setDaemon(True)
        self.daemon = True

    def run(self) -> None:

        # 定义线程运行方法
        while True:
            msg = self.queue.get(block=True, timeout=3)    # 循环获取队列中的消息
            print(f"MsgConsumer run:{self.name} - {msg}\n", end='')     # 从队列中获取消息
            # print(f"{self.getName()} - {msg}\n", end='')    
            if self.queue.empty():
                print(f"MsgConsumer run:{self.name} - 队列已取完\n", end='')
                break


queue = Queue(3)
threads = list()
threads.append(MsgProducer("PA", 10, queue))
threads.append(MsgProducer("PB", 10, queue))
threads.append(MsgProducer("PC", 10, queue))

threads.append(MsgConsumer("CA", queue))
threads.append(MsgConsumer("CB", queue))

for t in threads:
    t.start()