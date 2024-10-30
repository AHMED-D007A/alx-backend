#!/usr/bin/env python3
"""
Basic Cache dictionary
for the basic cache class
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache inherits from BaseCaching
    """

    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            keys = list(self.cache_data.keys())
            del self.cache_data[keys[0]]

    def get(self, key):
        """
        Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]


# if __name__ == "__main__":
#     my_cache = BasicCache()
#     my_cache.print_cache()
#     my_cache.put("A", "Hello")
#     my_cache.put("B", "World")
#     my_cache.put("C", "Holberton")
#     my_cache.print_cache()
#     print(my_cache.get("A"))
#     print(my_cache.get("B"))
#     print(my_cache.get("C"))
#     print(my_cache.get("D"))
#     my_cache.print_cache()
#     my_cache.put("D", "School")
#     my_cache.put("E", "Battery")
#     my_cache.put("A", "Street")
#     my_cache.print_cache()
#     print(my_cache.get("A"))
