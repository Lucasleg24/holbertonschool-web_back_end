#!/usr/bin/env python3

"""
module 4-tasks
"""


import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random

"""
import asyncio ans task 3
"""


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """

    Args:
        n (int): number of time wait_number will be call
        max_delay (int): max_delay to wait. Defaults to 10.

    Returns:
        List[float]: list of all delays in ascending order
    """
    # Crée une liste de coroutines `wait_random`
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    # execute et attend que toutes les taches soient complétées
    # et rassemble les résulat dans delays
    delays = await asyncio.gather(*tasks)
    # trie les items de la liste delays
    return [x for x in sorted(delays)]