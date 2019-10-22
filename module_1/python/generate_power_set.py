"""
Title: Subsets.

Problem: Given a set of distinct integers, nums, return all possible subsets
         (the power set).

Execution: python generate_power_set.py
"""
import unittest
from typing import List


class PowerSet:
    """Class to generate the power set."""

    def __init__(self):
        self.result = []

    def generate_power_set(self, nums: List[int]):
        results = []
        self.dfs(sorted(nums), 0, [], results)
        return results

    def dfs(self, nums, index, path, res):
        res.append(path)
        for i in range(index, len(nums)):
            self.dfs(nums, i+1, path+[nums[i]], res)


class TestGeneratePowerSet(unittest.TestCase):
    """Unit test for generate power set."""

    def test_1(self):
        """Test for generate power set."""
        expected_output = [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]

        ps = PowerSet()
        results = ps.generate_power_set([1, 2, 3])

        self.assertEqual(results, expected_output)


if __name__ == '__main__':
    unittest.main()

