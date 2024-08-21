#!/usr/bin/env python3
""" FIFOCache module
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache defines a FIFO caching system."""

    def __init__(self):
        """Initialize the class with the parent's init method and FIFO
        tracking."""
        super().__init__()
        self.order = []  # To keep track of the order of insertion

    def put(self, key, item):
        """Assign the item value to the key in the cache_data dictionary.
        If the cache exceeds the MAX_ITEMS, discard the oldest entry.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.order.remove(key)
        elif len(self.cache_data) >= self.MAX_ITEMS:
            oldest_key = self.order.pop(0)
            del self.cache_data[oldest_key]
            print(f"DISCARD: {oldest_key}")

        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """Return the value associated with key in cache_data."""
        return self.cache_data.get(key) if key in self.cache_data else None
