#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""


import csv
import math
from typing import List, Dict, Optional

"""
import csv, math ans typing
"""


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Returns a dictionary containing pagination information:
        - index: the starting index for the page
        - next_index: the index for the next page
        - page_size: number of items per page
        - data: the actual data in the page
        """
        # Validate inputs
        assert isinstance(index, int) and index >= 0, (
            "index should be a non-negative integer"
        )
        assert isinstance(page_size, int) and page_size > 0, (
            "page_size should be a positive integer"
        )

        # Fetch the indexed dataset
        indexed_data = self.indexed_dataset()
        total_data = len(indexed_data)

        # Calculate the start and end indexes for the requested page
        data = []
        current_index = index
        while len(data) < page_size and current_index < total_data:
            if current_index in indexed_data:
                data.append(indexed_data[current_index])
            current_index += 1

        # Calculate the next index
        next_index = current_index if current_index < total_data else None

        return {
            "index": index,
            "data": data,
            "page_size": page_size,
            "next_index": next_index
        }
