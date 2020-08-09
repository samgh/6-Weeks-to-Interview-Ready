"""
Title: Find first duplicate entry

Problem:
    Write a function that takes an array of sorted integers and a key and
    returns the index of the first occurrence of that key from the array.
    Example:
        idx   0     1  2   3    4    5    6    7    8    9
        A = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
        target = 108
        Returns index 3 since 108 appears for the first time at
        index 3.

Execution: python find_first_duplicate_entry.py
"""
from typing import List
import unittest


def find_first_duplicate_entry(input_list: List[int], target: int) -> int:
    low = 0
    high = len(input_list) - 1

    while low <= high:
        mid = (low + high) // 2

        if input_list[mid] < target:
            low = mid + 1
        elif input_list[mid] > target:
            high = mid - 1
        else:
            if mid - 1 < 0:
                return mid
            if input_list[mid - 1] != target:
                return mid
            high = mid - 1


class TestFindFirstDuplicateEntry(unittest.TestCase):
    """Unit tests for find_first_duplicate_entry."""

    def test_1(self):
        input_list = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
        target = 108
        self.assertEqual(find_first_duplicate_entry(input_list, target), 3)


if __name__ == "__main__":
    unittest.main()
