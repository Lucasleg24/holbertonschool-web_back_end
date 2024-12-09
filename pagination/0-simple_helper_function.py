#!/usr/bin/env python3

"""
module 0-simple_helper_function
"""


def index_range(page, page_size) -> tuple:
    """
    Calculate the start and end indexes for pagination

    Args:
        page (int): The page number (1-indexed)
        page_size (int): The number of items per page

    Returns:
        tuple[int, int]: A tuple containing the start and end indexes
    """
    start_index = (page - 1) * page_size  # Calcul de l'index de début
    end_index = page * page_size         # Calcul de l'index de fin
    return (start_index, end_index)
