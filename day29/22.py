# 异步IO -- 创建任务
# 使用asyncio.create_task()创建任务


import asyncio
import time


async def call_api(name: str, delay: float):
    print(f"{name} - step 1")
    # 模拟等待
    await asyncio.sleep(delay)
    print(f"{name} - step 2")

async def main():

    # 记录开始时间
    time_1 = time.perf_counter()

    print("start A coroutine")
    # 创建A协程任务
    task_1 = asyncio.create_task(call_api("A", 2))

    print("start B coroutine")
    # 创建B协程任务
    task_2 = asyncio.create_task(call_api("B", 5))

    # 等待A协程任务完成
    await task_1
    print("task A completed")

    # 等待B协程任务完成
    await task_2
    print("task B completed")

    # 记录结束时间
    time_2 = time.perf_counter()

    # 打印花费时间
    print(f"Spent {time_2 - time_1}")


if __name__ == '__main__':
    asyncio.run(main())