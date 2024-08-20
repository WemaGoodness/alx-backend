#!/usr/bin/env python3
"""
Module for hypermedia pagination of a dataset using a Server class.
"""

import math
from typing import Dict
Server = __import__('1-simple_pagination').Server


class Server(Server):
    """Server class with hypermedia pagination capabilities."""

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Return a dictionary with pagination information.
        Args:
            page (int): The page number.
            page_size (int): The number of items per page.
        Returns:
            Dict: A dictionary with pagination details.
        """
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)

        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages
        }

# Uncomment to test
# server = Server()
# print(server.get_hyper(1, 2))
