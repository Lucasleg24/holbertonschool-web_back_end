#!/usr/bin/env python3

"""
module 0-async_generator
"""


import asyncio
import random
from typing import Generator

"""
import asyncio, random and generator from typing
"""


async def async_generator() -> Generator[float, None, None]:
    """
    Coroutine that yields 10 random numbers between 0 and 10
    """
    for _ in range(10):
        await asyncio.sleep(1)  # Attente asynchrone de 1 seconde
        yield random.uniform(0, 10)  # Génération d'un nombre aléatoire
