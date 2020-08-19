"""
Title: Find rotated array

Problem:
    Suppose an array sorted in ascending order is rotated at some pivot unknown
    to you beforehand.

    (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

    You are given a target value to search. If found in the array return its
    index, otherwise return -1.

    You may assume no duplicate exists in the array.

    Your algorithm's runtime complexity must be in the order of O(log n).

Execution: python find_rotated_array.py
"""
from typing import List
import unittest


def binary(nums: List[int], i: int, j: int, target: int) -> int:
    if j - i == 0:
        return i if nums[i] == target else -1

    if j - i == 1:
        if nums[i] == target:
            return i
        elif nums[j] == target:
            return j
        else:
            return -1

    if j - i == 2:
        if nums[j] == target:
            return j
        else:
            return binary(nums, i, i + 1, target)

    mid = i + int((j - i) / 2)
    if nums[i] < nums[mid]:
        # left is in ascending order
        if nums[i] <= target <= nums[mid]:
            # is target in the range?
            return binary(nums, i, mid, target)
        else:
            # it's probably in other half
            return binary(nums, mid + 1, j, target)
    else:
        # right is in ascending order
        if nums[mid + 1] <= target <= nums[j]:
            # is target in the range?
            return binary(nums, mid + 1, j, target)
        else:
            # it's probably in other half
            return binary(nums, i, mid, target)


def find_rotated_array(nums: List[int], target: int) -> int:
    if len(nums) < 1:
        return -1
    return binary(nums, 0, len(nums) - 1, target)


class TestFindRotatedArray(unittest.TestCase):
    """Unit tests for find_rotated_array."""

    def test_1(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 0
        self.assertEqual(find_rotated_array(nums, target), 4)

    def test_2(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 3
        self.assertEqual(find_rotated_array(nums, target), -1)


if __name__ == "__main__":
    unittest.main()
