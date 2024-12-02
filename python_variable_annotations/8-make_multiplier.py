#!/usr/bin/env python3

"""
module 8-make_multiplier
"""


from typing import Callable

"""
import typing
"""


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    def for multiplier float
    """
    return lambda x: x * multiplier
