#!/usr/bin/env python3

"""
module 2-hypermedia_pagination
"""


import csv
from typing import List, Tuple, Dict, Optional
import math

"""
import csv, typing and math
"""


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end indexes for pagination.

    Args:
        page (int): The page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        tuple[int, int]: A tuple containing the start and end indexes.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip the header

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Return a page of the dataset.

        Args:
            page (int): The page number (1-indexed).
            page_size (int): The number of items per page.

        Returns:
            [List]: A list of rows or empty list if out of range.
        """
        # Ensure page and page_size are integers > 0
        assert isinstance(page, int) and page > 0, (
            "Page must be a positive integer."
        )
        assert isinstance(page_size, int) and page_size > 0, (
            "Page size must be a positive integer."
        )

        # Get the range of indexes for the requested page
        start_index, end_index = index_range(page, page_size)

        # Fetch the dataset
        dataset = self.dataset()

        # Return the appropriate slice or an empty list if out of range
        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        Return a dictionary with pagination metadata.

        Args:
            page (int): The current page number (1-indexed).
            page_size (int): The number of items per page.

        Returns:
            Dict[str, Optional[int]]: A dictionary with pagination metadata.
        """
        # Fetch the page data
        data = self.get_page(page, page_size)

        # Calculate total pages
        dataset = self.dataset()
        total_pages = math.ceil(len(dataset) / page_size)

        # Determine next and previous page numbers
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        # Build the metadata dictionary
        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages,
        }
