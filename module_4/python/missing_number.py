"""
Title: Missing number

Problem:
    Given an array containing n distinct numbers taken from 0, 1, 2, ...,
    n, find the one that is missing from the array.


Execution: python missing_number.py
"""
import unittest
from typing import List


def missing_number(nums: List[int]) -> int:
    """Find missing number."""
    nums.sort()

    # Ensure that n is at the last index
    if nums[-1] != len(nums):
        return len(nums)
    # Ensure that 0 is at the first index
    elif nums[0] != 0:
        return 0

    # If we get here, then the missing number is on the range (0, n)
    for i in range(1, len(nums)):
        expected_num = nums[i-1] + 1
        if nums[i] != expected_num:
            return expected_num


class TestFindMissingNumber(unittest.TestCase):
    """Unit test for find_missing_number."""

    def test_1(self):
        test_1_input = [3, 0, 1]
        self.assertEqual(missing_number(test_1_input), 2)

    def test_2(self):
        test_2_input = [9, 6, 4, 2, 3, 5, 7, 0, 1]
        self.assertEqual(missing_number(test_2_input), 8)


if __name__ == '__main__':
    unittest.main()
