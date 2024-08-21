#!/usr/bin/env python3
""" BasicCache module
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """BasicCache defines a basic caching system without limit."""

    def put(self, key, item):
        """Assign the item value to the key in the cache_data dictionary."""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Return the value associated with key in cache_data."""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
