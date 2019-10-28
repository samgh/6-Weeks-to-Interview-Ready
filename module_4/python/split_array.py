"""
Title: Split array

Problem:
    Given an array which consists of non-negative integers and an integer m,
    you can split the array into m non-empty continuous subarrays. Write an
    algorithm to minimize the largest sum among these m subarrays.

    Note: If n is the length of array, assume the following constraints are
    satisfied:

    1 ≤ n ≤ 1000 1 ≤ m ≤ min(50, n)

Execution: python split_array.py
"""
import unittest
from typing import List


def split_array(nums: List[int], m: int) -> int:
    """Split array from index m."""
    max_val, sum_val = 0, 0
    for num in nums:
        max_val = max(num, max_val)
        sum_val += num
    if m == 1:
        return sum_val

    # Perform binary search:
    left, right = max_val, sum_val
    while left <= right:
        mid = (left + right) // 2
        if is_valid(mid, nums, m):
            right = mid - 1
        else:
            left = mid + 1
    return left


def is_valid(target: int, nums: List[int], m: int):
    """Check if entry is valid in array."""
    count, total = 1, 0
    for num in nums:
        total += num
        if total > target:
            total = num
            count += 1
            if count > m:
                return False
    return True


class TestSplitArray(unittest.TestCase):
    """Unit test for split_array."""

    def test_1(self):
        """
        There are four ways to split nums into two subarrays.
        The best way is to split it into [7,2,5] and [10,8],
        where the largest sum among the two subarrays is only 18.
        """
        nums = [7, 2, 5, 10, 8]
        m = 2
        self.assertEqual(split_array(nums, m), 18)


if __name__ == '__main__':
    unittest.main()
