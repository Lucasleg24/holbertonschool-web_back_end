#!/usr/bin/env python3

"""
module 3-tasks
"""


import asyncio
wait_random = __import__ ('0-basic_async_syntax').wait_random

"""
import asyncio and wait_random
"""


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Crée une tâche asyncio pour exécuter la coroutine wait_random.

    Args:
        max_delay (int): Le délai maximum pour la fonction wait_random.

    Returns:
        asyncio.Task: Une tâche asyncio qui exécute wait_random(max_delay).
    """
    return asyncio.create_task(wait_random(max_delay))
