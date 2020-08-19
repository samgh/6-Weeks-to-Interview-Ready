"""
Title: Remove duplicates

Problem:
    Given a sorted array nums, remove the duplicates in-place such that each
    element appear only once and return the new length.

    Do not allocate extra space for another array, you must do this by modifying
    the input array in-place with O(1) extra memory.

Execution: python remove_duplicates.py
"""
from typing import List
import unittest


def remove_duplicates(nums: List[int]) -> int:
    if len(nums) == 0:
        return 0
    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    return i + 1


class TestRemoveDuplicates(unittest.TestCase):
    """Unit tests for remove_duplicates."""

    def test_1(self):
        self.assertEqual(remove_duplicates([1, 1, 2]), 2)

    def test_2(self):
        self.assertEqual(remove_duplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]), 5)


if __name__ == "__main__":
    unittest.main()
