#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0."""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Return a dictionary with deletion-resilient pagination information.
        Args:
            index (int): The start index.
            page_size (int): The number of items per page.
        Returns:
            Dict: A dictionary with pagination details.
        """
        assert isinstance(index, int) and index >= 0
        assert isinstance(page_size, int) and page_size > 0

        dataset = self.indexed_dataset()
        data = []
        next_index = index

        for _ in range(page_size):
            while next_index not in dataset and next_index < len(dataset):
                next_index += 1
            if next_index >= len(dataset):
                break
            data.append(dataset[next_index])
            next_index += 1

        return {
            "index": index,
            "data": data,
            "page_size": len(data),
            "next_index": next_index if next_index < len(dataset) else None
        }

# Uncomment to test the code
# server = Server()
# server.indexed_dataset()
# print(server.get_hyper_index(3, 2))
# print(server.get_hyper_index(5, 2))
# del server._Server__indexed_dataset[3]
# print(server.get_hyper_index(3, 2))
# print(server.get_hyper_index(5, 2))
