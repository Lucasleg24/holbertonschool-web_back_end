#!/usr/bin/env python3

"""
module 0-basic_async_syntax
"""


import asyncio
import random

"""
import asyncio and random
1- functions async
2- randomize generation value
"""


async def wait_random(max_delay: int = 10) -> float:
    """
    Coroutine qui attend un délai aléatoire entre 0 et max_delay secondes
    et retourne ce délai.

    Args:
        max_delay (int): La durée maximale du délai (par défaut 10).

    Returns:
        float: La durée du délai.
    """
    delay = random.uniform(0, max_delay)  # Générer un délai aléatoire.
    await asyncio.sleep(delay)           # Attendre ce délai sans bloquer.
    return delay                         # Retourner le délai.
