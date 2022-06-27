#!/usr/bin/env python3
""" Defines a function wait_n """
import asyncio
from typing import List


wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ Returns a list of delays after spawning wait_random n times """
    delay_list: List[float] = []
    for i in range(0, n):
        #delay: float = await wait_random(max_delay)
        delay_list.append(await (wait_random(max_delay)))
        i += 1
    return delay_list
