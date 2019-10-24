"""
Title: First missing number

Problem: Given an unsorted integer array, find the smallest missing positive
integer.


Execution: python first_missing_positive.py
"""
import unittest
from typing import List


def first_missing_positive(nums: List[int]):
    """First missing positive position."""
    nums.append(0)
    n = len(nums)

    for i in range(len(nums)):
        # Delete useless elements.
        if nums[i] < 0 or nums[i] >= n:
            nums[i] = 0
    for i in range(len(nums)):
        # Use the index as the hash to record frequency of each number.
        nums[nums[i] % n] += n
    for i in range(1, len(nums)):
        if nums[i]/n == 0:
            return i
    return n


class TestFirstMissingPositive(unittest.TestCase):
    """Unit test for first_missing_positive."""

    def test_1(self):
        self.assertEqual(first_missing_positive([1, 2, 0]), 3)

    def test_2(self):
        self.assertEqual(first_missing_positive([3, 4, -1, 1]), 2)

    def test_3(self):
        self.assertEqual(first_missing_positive([7, 8, 9, 11, 12]), 1)


if __name__ == '__main__':
    unittest.main()
