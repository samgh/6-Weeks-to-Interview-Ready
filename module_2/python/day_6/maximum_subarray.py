"""
Title: Maximum Sum Subarray

Problem:
    Given an integer array nums, find the contiguous subarray (containing at
    least one number) which has the largest sum and return its sum.

Execution: python max_sum_subarray.py
"""
import unittest
from typing import List


def maximum_subarray(nums: List[int]):
    """Function for calculating max sum in subarray. 
    Brute force solution that takes O(n^2) time."""
    max_val = float("-inf")

    for i in range(len(nums)):
        sum_val = 0
        for j in range(i, len(nums)):
            sum_val += nums[j]

            if sum_val > max_val:
                max_val = sum_val
    return max_val


class TestMaximumSubarray(unittest.TestCase):
    """Unit test for maximum_subarray."""

    def test_1(self):
        test_input_1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        self.assertEqual(maximum_subarray(test_input_1), 6)
        print("Explanation: [4,-1,2,1] has the largest sum = 6.")


if __name__ == '__main__':
    unittest.main()
