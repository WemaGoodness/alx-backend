#!/usr/bin/env python3
"""
Module for pagination of a dataset using a Server class.
"""

import csv
from typing import List
index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip header row
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Return the appropriate page of the dataset.
        Args:
            page (int): The page number.
            page_size (int): The number of items per page.
        Returns:
            List[List]: The list of rows for the requested page.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        
        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()
        
        if start_index >= len(dataset):
            return []
        return dataset[start_index:end_index]

# Uncomment to test
# server = Server()
# print(server.get_page(1, 3))  # Expected output: First 3 rows of the dataset
# print(server.get_page(3, 2))  # Expected output: Rows 4 to 5 of the dataset
