#!/usr/bin/env python3
"""
Module that provides a helper function for pagination.
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end indexes for the items to be displayed
    on a given page.
    Args:
        page (int): The page number (1-indexed).
        page_size (int): The number of items per page.
    Returns:
        Tuple[int, int]: A tuple containing the start and end indexes.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index

# Uncomment to test
# print(index_range(1, 7))  # Expected output: (0, 7)
# print(index_range(3, 15))  # Expected output: (30, 45)
