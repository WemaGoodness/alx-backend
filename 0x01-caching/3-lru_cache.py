#!/usr/bin/env python3
""" LRUCache module
"""

from collections import OrderedDict
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRUCache defines a Least Recently Used (LRU) caching system."""

    def __init__(self):
        """Initialize the class with the parent's init method and LRU
        tracking."""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Assign the item value to the key in the cache_data dictionary.
        If the cache exceeds the MAX_ITEMS, discard the least recently
        used entry.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data.move_to_end(key)
        self.cache_data[key] = item

        if len(self.cache_data) > self.MAX_ITEMS:
            oldest_key, _ = self.cache_data.popitem(last=False)
            print(f"DISCARD: {oldest_key}")

    def get(self, key):
        """Return the value associated with key in cache_data.
        Move the accessed key to the end to mark it as recently used.
        """
        if key is None or key not in self.cache_data:
            return None

        self.cache_data.move_to_end(key)
        return self.cache_data[key]
