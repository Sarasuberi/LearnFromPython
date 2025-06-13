# 并发编程 -- 线程锁
# 线程锁
# 当多个线程在同一时刻访问相同数据时可能阐释数据丢失，覆盖，不完整等问题
# 锁是用来解决这个问题的重要手段
# Lock，Condition



from threading import Thread, Lock, Condition


task_lock = Lock()

def task(name: str):
    global task_lock
    for n in range(2):
        task_lock.acquire() # 加锁
        print(f"{name} - round {n} - step 1\n", end='')
        print(f"{name} - round {n} - step 2\n", end='')
        print(f"{name} - round {n} - step 3\n", end='')
        task_lock.release() # 解锁


t1 = Thread(target=task, args=("A",))
t2 = Thread(target=task, args=("B",))
t3 = Thread(target=task, args=("C",))

t1.start()
t2.start()
t3.start()


class SafeQueue:
    # 初始化队列，设置队列大小
    def __init__(self, size: int):
        self.__item_list = list()  # 创建一个空列表，用于存储队列中的元素
        self.size = size  # 设置队列大小
        self.__item_lock = Condition()  # 创建一个条件变量，用于线程同步

    # 向队列中添加元素
    def put(self, item):
        with self.__item_lock:  # 使用条件变量进行线程同步
            while len(self.__item_list) >= self.size:  # 如果队列已满，则等待
                self.__item_lock.wait()

            self.__item_list.insert(0, item)  # 将元素插入队列头部
            self.__item_lock.notify_all()  # 通知其他线程队列中有元素了

    # 从队列中获取元素
    def get(self):
        with self.__item_lock:  # 使用条件变量进行线程同步
            while len(self.__item_list) == 0:  # 如果队列为空，则等待
                self.__item_lock.wait()

            result = self.__item_list.pop()  # 从队列尾部取出元素
            self.__item_lock.notify_all()  # 通知其他线程队列中有元素了
        return result  # 返回取出的元素
        
class MsgProducer(Thread):
    def __init__(self, name: str, count: int, queue: SafeQueue):

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
            self.queue.put(msg)

class MsgConsumer(Thread):

    # 定义一个消息消费者类，继承自Thread类
    def __init__(self, name: str, queue: SafeQueue):

        # 初始化方法，传入线程名称和队列
        # 调用父类的初始化方法
        super().__init__()

        # 设置线程名称
        self.name = name

        # 设置线程队列
        self.queue = queue

        # 设置线程为守护线程
        self.daemon = True

    def run(self) -> None:

        # 定义线程运行方法
        while True:
            msg = self.queue.get(timeout=3)    # 循环获取队列中的消息
            print(f"MsgConsumer run:{self.name} - {msg}\n", end='')     # 从队列中获取消息
            if self.queue.empty():
                print(f"MsgConsumer run:{self.name} - 队列已取完\n", end='')
                break


queue = SafeQueue(3)
threads = list()
threads.append(MsgProducer("PA", 10, queue))
threads.append(MsgProducer("PB", 10, queue))
threads.append(MsgProducer("PC", 10, queue))

threads.append(MsgConsumer("CA", queue))
threads.append(MsgConsumer("CB", queue))

for t in threads:
    t.start()