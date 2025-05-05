import asyncio
import aiofiles

async def task1():
    print("Task 1 started")
    await asyncio.sleep(3)
    print("Task 1 finished")

async def task2():
    print("Task 2 started")
    await asyncio.sleep(2)
    print("Task 2 finished")

async def task3():
    print("Task 3 started")
    await asyncio.sleep(1)
    print("Task 3 finished")

async def main():
    await asyncio.gather(task1(), task2(), task3())  # Runs both tasks together
    #results = await asyncio.gather(task3(), task1(), task2())
    #print(type(results))

    #task1_instance = asyncio.create_task(task1())
    #task2_instance = asyncio.create_task(task2())
    #task3_instance = asyncio.create_task(task3())
    #await task1_instance
    #await task2_instance
    #await task3_instance

asyncio.run(main())

async def write():
    async with aiofiles.open(r"aiofile-test.txt", "w") as f:
        await f.write("Poetries ain't just words but but a consipiracy theory !!!\n")
        await f.write("And most skills acquired thru experience.")

async def read():
    async with aiofiles.open(r"aiofile-test.txt", "r") as f:
        print(await f.read())

asyncio.run(write())
asyncio.run(read())