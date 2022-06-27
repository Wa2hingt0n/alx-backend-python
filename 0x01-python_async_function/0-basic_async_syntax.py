#!/usr/bin/env python3
""" Defines a function wait_random """
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ Takes an integer argument and waits for a random delay before
        returning the delay duration
    """
    delay: float = random.uniform(0, max_delay + 1)
    await asyncio.sleep(delay)
    return delay
