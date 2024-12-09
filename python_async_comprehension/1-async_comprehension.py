#!/usr/bin/env python3

"""
module 1-async_comprehension
"""


from typing import List
async_generator = __import__('0-async_generator').async_generator

"""
import typing List and Task 0 async_generator
"""


async def async_comprehension() -> List[float]:
    """
    Coroutine collects 10 random numbers from async_generator
    using async comprehensions and returns the list of numbers
    """
    return [number async for number in async_generator()]
