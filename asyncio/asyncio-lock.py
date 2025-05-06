import asyncio

lock = asyncio.Lock()

async def access_shared_resource(task_id):
    async with lock:
        print(f"Task {task_id} is accessing the shared resource")
        await asyncio.sleep(4)
        print(f"Task {task_id} is done")

async def access_shared_resource_without_lock(task_id):
    print(f"Task {task_id} is accessing the shared resource without lock")
    await asyncio.sleep(4)
    print(f"Task {task_id} is done")

async def main():
    await asyncio.gather(access_shared_resource(1), access_shared_resource(2), access_shared_resource_without_lock(3))

asyncio.run(main())