"""
Title: Maximum subarray.

Problem: Given an integer array, nums, find the contiguous subarray (containing
         at least one number) which has the largest sum and return its sum.

Execution: python maximum_subarray.py
"""
import unittest
from typing import List


def maximum_subarray(nums: List[int]):
    """Function for calculating the maximum subarray."""
    if not nums:
        return 0

    cur_sum = max_sum = nums[0]
    for num in nums[1:]:
        cur_sum = max(num, cur_sum + num)
        max_sum = max(max_sum, cur_sum)
    return max_sum


class TestMaximumSubarray(unittest.TestCase):
    """Unit test for calculating the maximum subarray."""

    def test_1(self):
        test_input = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        self.assertEqual(maximum_subarray(test_input), 6)
        print("Explanation: [4, -1, 2, 1] has the largest sum = 6.")


if __name__ == '__main__':
    unittest.main()
