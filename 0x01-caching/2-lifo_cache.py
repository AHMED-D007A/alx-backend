#!/usr/bin/env python3
"""
LIFO caching
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache class
    """

    def __init__(self):
        """
        Constructor
        """
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                if key not in self.cache_data:
                    discard = self.stack[-1]
                    del self.cache_data[discard]
                    self.stack.pop(-1)
                    print("DISCARD:", discard)
            self.cache_data[key] = item
            self.stack.append(key)

    def get(self, key):
        """
        Get an item by key
        """
        if key in self.cache_data:
            return self.cache_data[key]
        return None


if __name__ == "__main__":
    my_cache = LIFOCache()
    my_cache.put("A", "Hello")
    my_cache.put("B", "World")
    my_cache.put("C", "Holberton")
    my_cache.put("D", "School")
    my_cache.print_cache()
    my_cache.put("E", "Battery")
    my_cache.print_cache()
    my_cache.put("C", "Street")
    my_cache.print_cache()
    my_cache.put("F", "Mission")
    my_cache.print_cache()
    my_cache.put("G", "San Francisco")
    my_cache.print_cache()
