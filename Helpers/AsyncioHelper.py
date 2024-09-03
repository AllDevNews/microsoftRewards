import asyncio
import random


class AsyncioHelper:

    @staticmethod
    async def wait_random_duration():
        duration = random.uniform(1, 3)
        await asyncio.sleep(duration)
        print(f"Waited for {duration} seconds")
