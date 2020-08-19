"""
Title: Binary search

Problem:
    Binary search is a search algorithm that finds the position of a target
    value within a sorted array. Binary search compares the target value to the
    middle element of the array.

    If they are not equal, the half in which the target cannot lie is
    eliminated and the search continues on the remaining half, again taking the
    middle element to compare to the target value, and repeating this until the
    target value is found. If the search ends with the remaining half being
    empty, the target is not in the array.

Execution: python binary_search.py
"""
from typing import Any, List
import unittest


def binary_search(data: List[Any], target: int, low: int, high: int) -> bool:
    """Recursive implementation of binary search algorithm."""
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_search(data, target, low, mid - 1)
        else:
            return binary_search(data, target, mid + 1, high)


class TestBinarySearch(unittest.TestCase):
    """Unit tests for binary_search."""

    def test_1(self):
        data = [2, 4, 5, 7, 8, 9, 12, 37]
        target = 37
        self.assertEqual(binary_search(data, target, 0, len(data) - 1), True)

    def test_2(self):
        data = [2, 4, 5, 7, 8, 9, 12, 37]
        target = 40
        self.assertEqual(binary_search(data, target, 0, len(data) - 1), False)


if __name__ == "__main__":
    unittest.main()
