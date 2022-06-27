#!/usr/bin/env python3
""" Defines a function that returns the time taken to complete an async task"""
import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ Returns the total execution time for an async function / n """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end = time.perf_counter()
    t = end - start
    return t / n
