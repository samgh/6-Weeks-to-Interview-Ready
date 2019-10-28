"""
Title: Three Sum

Problem:
    Given an array nums of n integers, are there elements a, b, c in nums such
    that a + b + c = 0? Find all unique triplets in the array which gives the
    sum of zero.

    Note:
    The solution set must not contain duplicate triplets.

Execution: python three_sum.py
"""
import unittest
from typing import List


def three_sum(nums: List[int]):
    """Three-sum problem."""
    nums.sort()
    res = []
    for i in range(len(nums)-2):
        if i == 0 or i > 0 and nums[i] != nums[i-1]:
            low = i + 1
            high = len(nums) - 1
            sum_val = 0 - nums[i]
            while low < high:
                if nums[low] + nums[high] == sum_val:
                    res.append([nums[i], nums[low], nums[high]])
                    while low < high and nums[low] == nums[low + 1]:
                        low += 1
                    while low < high and nums[high] == nums[high - 1]:
                        high -= 1
                    low += 1
                    high -= 1
                elif nums[low] + nums[high] < sum_val:
                    while low < high and nums[low] == nums[low + 1]:
                        low += 1
                    low += 1
                else:
                    while low < high and nums[high] == nums[high - 1]:
                        high -= 1
                    high -= 1
    return res


class TestThreeSum(unittest.TestCase):
    """Unit test for three_sum."""

    def test_1(self):
        """
        Given array nums = [-1, 0, 1, 2, -1, -4],
        A solution set is:
            [
              [-1, 0, 1],
              [-1, -1, 2]
            ]
        """
        nums = [-1, 0, 1, 2, -1, -4]
        expected_out = [
            [-1, -1, 2],
            [-1, 0, 1],
        ]
        out = three_sum(nums)
        self.assertEqual(expected_out, out)


if __name__ == '__main__':
    unittest.main()
