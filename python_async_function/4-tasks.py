#!/usr/bin/env python3

"""
module 4-tasks
"""


import asyncio
task_wait_random = __import__('3-tasks').task_wait_random

"""
import asyncio ans task 3
"""


async def task_wait_n(n: int, max_delay: int) -> list[float]:
    """
    Exécute task_wait_random n fois avec un délai maximum et retourne une liste
    des délais dans l'ordre croissant.

    Args:
        n (int): Nombre de fois où exécuter task_wait_random.
        max_delay (int): Délai maximum.

    Returns:
        list[float]: Liste des délais en ordre croissant.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]  # Créer les tâches
    delays = []

    # Utilisation de asyncio.as_completed pour gérer les tâches dès qu'elles terminent
    for finished_task in asyncio.as_completed(tasks):
        delay = await finished_task  # Attendre la fin de chaque tâche
        delays.append(delay)  # Ajouter le délai terminé à la liste

    return delays  # Retourner les délais
