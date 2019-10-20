"""
Title: LRU Cache

Problem:
    Design and implement a data structure for Least Recently Used (LRU)
    cache. It should support the following operations: get and put.

    get(key) - Get the value (will always be positive) of the key if the key exists
    in the cache, otherwise return -1.  put(key, value) - Set or insert the value
    if the key is not already present. When the cache reached its capacity, it
    should invalidate the least recently used item before inserting a new item.

    The cache is initialized with a positive capacity.

Execution: python lru_cache.py
"""
from collections import OrderedDict

import unittest


class LRUCache():
    def __init__(self, capacity: int):
        self._cache = OrderedDict()
        self._capacity = capacity

    def get(self, key: int) -> int:
        if key not in self._cache:
            return -1
        value = self._cache[key]
        self._cache.move_to_end(key) 
        return value

    def put(self, key: int, value: int) -> None:
        if key in self._cache:
            del self._cache[key]
        self._cache[key] = value
        if len(self._cache) > self._capacity:
            self._cache.popitem(last=False)


class TestLRUCache(unittest.TestCase):
    """Unit test for LRU cache."""

    def test_1(self):
        cache = LRUCache(capacity=2)
        cache.put(1, 1)
        cache.put(2, 2)
        self.assertEqual(cache.get(1), 1)
        cache.put(3, 3)
        self.assertEqual(cache.get(2), -1)
        cache.put(4, 4)
        self.assertEqual(cache.get(1), -1)
        self.assertEqual(cache.get(3), 3)
        self.assertEqual(cache.get(4), 4)


if __name__ == '__main__':
    unittest.main()
