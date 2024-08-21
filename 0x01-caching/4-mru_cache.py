#!/usr/bin/env python3
""" MRUCache module
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """MRUCache defines a Most Recently Used (MRU) caching system."""

    def __init__(self):
        """Initialize the class with the parent's init method and MRU
        tracking."""
        super().__init__()
        self.mru_key = None  # To keep track of the most recently used key

    def put(self, key, item):
        """Assign the item value to the key in the cache_data dictionary.
        If the cache exceeds the MAX_ITEMS, discard the most recently
        used entry.
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS and key not in self.cache_data:
            if self.mru_key:
                del self.cache_data[self.mru_key]
                print(f"DISCARD: {self.mru_key}")

        self.cache_data[key] = item
        self.mru_key = key

    def get(self, key):
        """Return the value associated with key in cache_data.
        Mark the accessed key as the most recently used.
        """
        if key is None or key not in self.cache_data:
            return None

        self.mru_key = key
        return self.cache_data[key]
