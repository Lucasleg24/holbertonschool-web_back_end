#!/usr/bin/env python3

"""
module 1-concurrent_coroutines
"""


import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random

"""
import asyncio, List and t0 module
"""


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Exécute wait_random n fois avec un max_delay donné,
    et retourne une liste des délais triés par ordre croissant.

    Args:
        n (int): Nombre d'exécutions de wait_random.
        max_delay (int): Délai maximum pour chaque appel à wait_random.

    Returns:
        List[float]: Liste des délais triés en ordre croissant.
    """
    delays = []  # Liste pour stocker les délais retournés.

    # Lancer n tâches concurrentes
    tasks = [wait_random(max_delay) for _ in range(n)]

    # Attendre que chaque tâche se termine et insérer chaque délai dans l'ordre
    for finished_task in asyncio.as_completed(tasks):
        delay = await finished_task  # Attendre qu'une tâche termine
        # Insertion dans la liste tout en maintenant l'ordre croissant
        inserted = False
        for i in range(len(delays)):
            if delay < delays[i]:
                delays.insert(i, delay)
                inserted = True
                break
        if not inserted:
            delays.append(delay)

    return delays
