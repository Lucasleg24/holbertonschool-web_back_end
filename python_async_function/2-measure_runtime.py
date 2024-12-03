#!/usr/bin/env python3

"""
module 2-measure_runtime
"""


import time
import asyncio
wait_n = __import__ ('1-concurrent_coroutines').wait_n

"""
import time asyncio and wait_n
"""


def measure_time(n: int, max_delay: int) -> float:
    """
    Mesure le temps total nécessaire pour exécuter wait_n(n, max_delay)
    et retourne le temps moyen

    Args:
        n (int): Nombre d'exécutions de wait_random.
        max_delay (int): Le délai maximum

    Returns:
        float: Temps moyen
    """
    start_time = time.perf_counter()  # Démarrer le chronomètre
    asyncio.run(wait_n(n, max_delay))  # Exécuter wait_n de manière asynchrone
    end_time = time.perf_counter()  # Arrêter le chronomètre

    total_time = end_time - start_time  # Calculer le temps total avant service
    return total_time / n  # Retourner le temps moyen
