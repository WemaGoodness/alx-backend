#!/usr/bin/env python3
""" LFUCache module
"""

from collections import OrderedDict
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """LFUCache defines a Least Frequently Used (LFU) caching system."""

    def __init__(self):
        """Initialize the class with the parent's init method and LFU
        tracking."""
        super().__init__()
        self.frequency = {}
        self.order = OrderedDict()

    def put(self, key, item):
        """Assign the item value to the key in the cache_data dictionary.
        If the cache exceeds the MAX_ITEMS, discard the least frequently used
        entry.
        In case of a tie in frequency, use the Least Recently Used (LRU)
        policy.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            # Update the value and move the key to the end of order
            # (most recently used)
            self.cache_data[key] = item
            self.frequency[key] += 1
            self.order.move_to_end(key)
        else:
            # If cache is full, remove the least frequently used
            # (and least recently used if tie)
            if len(self.cache_data) >= self.MAX_ITEMS:
                # Find the least frequently used key(s)
                min_freq = min(self.frequency.values())
                lfu_keys = [k for k, v in self.frequency.items()
                            if v == min_freq]

                # If there's a tie, use the LRU policy among those keys
                if len(lfu_keys) > 1:
                    for k in self.order:
                        if k in lfu_keys:
                            lfu_key = k
                            break
                else:
                    lfu_key = lfu_keys[0]

                # Remove the LFU key
                del self.cache_data[lfu_key]
                del self.frequency[lfu_key]
                del self.order[lfu_key]
                print(f"DISCARD: {lfu_key}")

            # Add the new item to the cache
            self.cache_data[key] = item
            self.frequency[key] = 1
            self.order[key] = True

    def get(self, key):
        """Return the value associated with key in cache_data.
        Increment the access frequency and mark the key as recently used.
        """
        if key is None or key not in self.cache_data:
            return None

        self.frequency[key] += 1
        self.order.move_to_end(key)
        return self.cache_data[key]
