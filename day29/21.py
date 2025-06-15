# 异步IO -- 协程
# asyncio模块
# asyncio模块通过一个线程执行并发任务
# 通过async和await关键字提供支持
# 通过事件循环来实现
# 事件循环
# 主线程 -> 提交任务 -> 事件循环[任务队列 -> （监控任务 -> 执行任务直到阻塞 -> 检查阻塞完成通知）]-> 执行任务
# 定义协程
# 使用async关键字定义一个协程
# 运行协程

import asyncio


async def calculate(n_1: int, n_2: int):
    res = n_1 + n_2
    print(res)

# 定义一个异步函数main
async def main():
    print("main -step 1")
    await calculate(1, 2)
    print("main -step 2")


asyncio.run(main())
