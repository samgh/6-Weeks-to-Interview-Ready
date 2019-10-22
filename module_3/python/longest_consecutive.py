"""
Title: Longest consecutive sequence.

Problem: 
    Given an unsorted array of integers, find the length of the longest
    consecutive elements sequence.

    Your algorithm should run in O(n) complexity.

Execution: python longest_consecutive.py
"""
import unittest
from typing import List


def longest_consecutive_bf(nums: List[int]):
    """Function for brute-force longest consecutive."""
    longest_streak = 0

    for num in nums:
        current_num = num
        current_streak = 1

        while current_num + 1 in nums:
            current_num += 1
            current_streak += 1

        longest_streak = max(longest_streak, current_streak)

    return longest_streak


def longest_consecutive_sorting(nums: List[int]):
    """Function for sorting approach for longest consecutive."""
    if not nums:
        return 0

    nums.sort()

    longest_streak = 1
    current_streak = 1

    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:
            if nums[i] == nums[i-1]+1:
                current_streak += 1
            else:
                longest_streak = max(longest_streak, current_streak)
                current_streak = 1
    return max(longest_streak, current_streak)


def longest_consecutive_hashset(nums: List[int]):
    """Function for hashset approach for longest consecutive."""
    longest_streak = 0
    num_set = set(nums)

    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

    return longest_streak


class TestLongestConsecutive(unittest.TestCase):
    """Unit test for longest consecutive."""

    def test_bf(self):
        self.assertEqual(longest_consecutive_bf([100, 4, 200, 1, 3, 2]), 4)
        print("Brute-force approach: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.")

    def test_sorting(self):
        self.assertEqual(longest_consecutive_sorting([100, 4, 200, 1, 3, 2]), 4)
        print("Sorting approach: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.")

    def test_hashset(self):
        self.assertEqual(longest_consecutive_hashset([100, 4, 200, 1, 3, 2]), 4)
        print("Hashset approach: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.")


if __name__ == '__main__':
    unittest.main()
