"""
Title: Missing number.

Problem: 
    Given an array containing n distinct numbers taken from 0, 1, 2, ..., n,
    find the one that is missing from the array.

Execution: python missing_number.py
"""
from typing import List
import unittest


def missing_number_sorting(nums: List[int]) -> int:
    """Function for calculating the missing number using sorting."""
    nums.sort()

    # Ensure that n is at the last index
    if nums[-1] != len(nums):
        return len(nums)
    # Ensure that 0 is at the first index
    elif nums[0] != 0:
        return 0

    # If we get here, then the missing number is on the range (0, n)
    for i in range(1, len(nums)):
        expected_num = nums[i - 1] + 1
        if nums[i] != expected_num:
            return expected_num


def missing_number_hash_set(nums: List[int]) -> int:
    """Function for calculating the missing number using sorting."""
    num_set = set(nums)
    n = len(nums) + 1
    for number in range(n):
        if number not in num_set:
            return number


def missing_number_bit_manip(nums: List[int]) -> int:
    """Function for calculating the missing number using sorting."""
    missing = len(nums)
    for i, num in enumerate(nums):
        missing ^= i ^ num
    return missing


class TestHammingDistance(unittest.TestCase):
    """Unit test for hamming_distance."""

    def test_1(self):
        input_list = [3, 0, 1]
        self.assertEqual(missing_number_sorting(input_list), 2)
        self.assertEqual(missing_number_hash_set(input_list), 2)
        self.assertEqual(missing_number_bit_manip(input_list), 2)

    def test_2(self):
        input_list = [9, 6, 4, 2, 3, 5, 7, 0, 1]
        self.assertEqual(missing_number_sorting(input_list), 8)
        self.assertEqual(missing_number_hash_set(input_list), 8)
        self.assertEqual(missing_number_bit_manip(input_list), 8)


if __name__ == "__main__":
    unittest.main()
