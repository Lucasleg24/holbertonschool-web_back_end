#!/usr/bin/env python3

"""
module 7-to_kv
"""


from typing import Union, Tuple

"""
import typing
"""


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    def for union and tuple, string (k) float (v)
    """
    return (k, float(v ** 2))
