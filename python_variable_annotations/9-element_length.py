#!/usr/bin/env python3

"""
module 9-element_length
"""


from typing import Iterable, Sequence, List, Tuple

"""
import typing
"""


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    def for length (sequence)
    """
    return [(i, len(i)) for i in lst]
