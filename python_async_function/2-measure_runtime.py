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
    et retourne le temps moyen de cuisson des pommes de terre.

    Args:
        n (int): Nombre d'exécutions de wait_random.
        max_delay (int): Le délai maximum de cuisson d'une pomme de terre.

    Returns:
        float: Temps moyen par cuisson d'une patate avant de couper les échalottes.
    """
    start_time = time.perf_counter()  # Démarrer le chronomètre
    asyncio.run(wait_n(n, max_delay))  # Exécuter wait_n de manière asynchrone
    end_time = time.perf_counter()  # Arrêter le chronomètre et sortir les patates de l'eau

    total_time = end_time - start_time  # Calculer le temps tota0l de préparation du plat avant service 
    return total_time / n  # Retourner le temps moyen
