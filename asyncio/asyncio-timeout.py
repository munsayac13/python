import asyncio

async def long_running_task():
    await asyncio.sleep(60)
    return "Task completed"

async def faulty_task():
    await asyncio.sleep(1)
    raise ValueError("An error occurred")


async def main():
    try:
        # TimeOutError
        result = await asyncio.wait_for(long_running_task(), timeout=5)
        print(result)
    except asyncio.TimeoutError:
        print("Task timed out!")
    

    try:
        # ValueError
        await faulty_task()
    except ValueError as e:
        print(f"Caught an error: {e}")

asyncio.run(main())
