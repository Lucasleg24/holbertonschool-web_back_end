#!/usr/bin/env python3

"""
module 2-measure_runtime
"""


import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension

"""
import asyncio, time and task 1
"""


async def measure_runtime() -> float:
    """
    Measures the total runtime of running async_comprehension
    four times in parallel using asyncio.gather.
    """
    start_time = time.perf_counter()  # Démarre le chronomètre
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    end_time = time.perf_counter()  # Arrête le chronomètre
    return end_time - start_time
