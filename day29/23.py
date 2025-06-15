# 异步IO -- 任务进阶
# 取消任务
# Task对象提供了Task.done()方法，用于检查任务是否已经完成
# 还提供了Task.cancel()方法，用于取消任务
# 超时取消任务
# 在一个等待时长超过设定值后进行任务取消
# asyncio.wait_for(task, timeout = 超时时长)
# gather函数
# asyncio.gather(tasks1,tasks2,...)函数用于并发运行多个任务，并返回一个Future对象
# 任务异常
# 如果任务中抛出了异常，gather函数会返回一个异常的Future对象
# return_exceptions参数用于设置是否将异常作为结果返回


import asyncio
from asyncio.exceptions import TimeoutError


async def play_music(music: str):
    print(f"Start playing {music}")
    await asyncio.sleep(5)
    print(f"Finished playing {music}")
    return music

async def call_api():
    print("calling api.....")
    raise Exception("Error calling")

async def my_cancel():
    task = asyncio.create_task(play_music("A"))

    # 等待3秒
    await asyncio.sleep(3)

    # 如果任务没有完成，则取消任务
    if not task.done():
        task.cancel()

async def my_cancel_with_timeout():
    task = asyncio.create_task(play_music("B"))
    try:

        # 等待任务完成，超时时间为2秒
        await asyncio.wait_for(task, timeout=2)
    except TimeoutError:
        print("timeout")


async def my_timeout():
    task = asyncio.create_task(play_music("B"))
    try:

        # 等待任务完成，超时时间为2秒
        # asyncio.shield()用于屏蔽取消操作
        await asyncio.wait_for(asyncio.shield(task), timeout=2)
    except TimeoutError:
        print("timeout")

        # 等待任务完成
        await task

async def my_gather():
    results = await asyncio.gather(play_music("A"), play_music("B"))
    print(results)

async def my_gather_with_exception():

    # 使用asyncio.gather()函数并发执行多个任务，并返回结果
    # 添加return_exceptions=True参数，将异常作为结果返回，保证程序不会崩溃
    results = await asyncio.gather(play_music("A"), play_music("B"), call_api(),
                                   return_exceptions=True)
    print(results)


if __name__ == "__main__":
    # asyncio.run(my_cancel())
    # asyncio.run(my_cancel_with_timeout())
    # asyncio.run(my_timeout())
    # asyncio.run(my_gather())
    asyncio.run(my_gather_with_exception())
