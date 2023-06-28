import asyncio
import time


def log(msg):
    print(str(int(time.time())), asyncio.current_task().get_name(), msg)


def d1(func):
    async def wrapper():
        log("d1 call: " + func.__name__)
        result = await func()
        return result
    return wrapper


async def m1():
    log("> m1. sleep(2)")
    await asyncio.sleep(2)
    log("  m1: after sleep")
    return 5


@d1
async def m2():
    log("> m2. sleep(3)")
    await asyncio.sleep(3)
    log("  m2 after sleep")

    result = await m1()
    log(f"m2 completed with result: {result}")


asyncio.run(m2())
