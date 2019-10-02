"""
Title: Search in a rotated array.

Problem: Suppose an array sorted in ascending order is rotated at some pivot
         unknown to you beforehand.

        (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

        You are given a target value to search. If found in the array return its index,
        otherwise return -1.

        You may assume no duplicate exists in the array.

        Your algorithm's runtime complexity must be in the order of O(log n).

Execution: python search_rotated_array.py
"""
import unittest
from typing import List


def search_rotated_array(nums: List[int], target: int):
    """Function for searching a rotated array."""
    if not nums:
        return -1
    low, high = 0, len(nums) - 1

    while low <= high:
        mid = (low + high) // 2
        if target == nums[mid]:
            return mid
        if nums[low] <= nums[mid]:
            if nums[low] <= target <= nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if nums[mid] <= target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1


class TestSearchRotatedArray(unittest.TestCase):
    """Unit test for SearchRotatedArray."""

    def test_1(self):
        """Test for: Input: nums = [4,5,6,7,0,1,2], target = 0 Output: 4."""
        self.assertEqual(
                search_rotated_array(
                    nums=[4, 5, 6, 7, 0, 1, 2],
                    target=0
                ), 4)
    
    def test_2(self):
        """Test for: Input: nums = [4,5,6,7,0,1,2], target = 3 Output: -1."""
        self.assertEqual(
                search_rotated_array(
                    nums=[4, 5, 6, 7, 0, 1, 2],
                    target=3
                ), -1)


if __name__ == '__main__':
    unittest.main()
