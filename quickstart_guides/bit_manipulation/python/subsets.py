"""
Title: Subsets

Problem: 
    Given a set of distinct integers, nums, return all possible subsets (the
    power set).

    Note: The solution set must not contain duplicate subsets.

Execution: python subsets.py
"""
from typing import List
import unittest


def subsets(nums: List[int]) -> List[List[int]]:
    out = []
    def helper(nums_1: List[int], nums_2: List[int]):
        out.append(nums_2)
        for i, n in enumerate(nums_1):
            helper(nums_1[i+1:], nums_2 + [n])
        return out
    return helper(nums, [])

class TestHammingDistance(unittest.TestCase):
    """Unit test for hamming_distance."""

    def test_1(self):
        input_list = [1, 2, 3]
        output_list = [
                [],
                [1],
                [1, 2],
                [1, 2, 3],
                [1, 3],
                [2],
                [2, 3],
                [3],
        ]
        self.assertEqual(subsets(input_list), output_list)


if __name__ == '__main__':
    unittest.main()

