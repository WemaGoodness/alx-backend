#!/usr/bin/env python3
""" LIFOCache module
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache defines a LIFO caching system."""

    def __init__(self):
        """Initialize the class with the parent's init method and LIFO
        tracking."""
        super().__init__()
        self.last_key = None  # To keep track of the most recently added key

    def put(self, key, item):
        """Assign the item value to the key in the cache_data dictionary.
        If the cache exceeds the MAX_ITEMS, discard the last entry.
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS and key not in self.cache_data:
            if self.last_key:
                del self.cache_data[self.last_key]
                print(f"DISCARD: {self.last_key}")

        self.cache_data[key] = item
        self.last_key = key

    def get(self, key):
        """Return the value associated with key in cache_data."""
        return self.cache_data.get(key) if key in self.cache_data else None
