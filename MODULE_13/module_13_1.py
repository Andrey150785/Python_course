import asyncio
from time import sleep


async def start_strongman(name, power):
    balls = 1
    print(f'Силач {name} начал соревнования')
    while balls != 5:
        await asyncio.sleep(1 / power)
        print(f'Силач {name} поднял {balls}')
        balls += 1
    print(f'Силач {name} закончил соревнования.')


async def start_tournament():
    task1 = asyncio.create_task(start_strongman('Силач 1', 10))
    task2 = asyncio.create_task(start_strongman('Силач 2', 5))
    task3 = asyncio.create_task(start_strongman('Силач 3', 3))

    await task1
    await task2
    await task3


asyncio.run(start_tournament())
