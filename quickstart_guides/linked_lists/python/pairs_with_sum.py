"""
Title: Pairs with sum.

Problem:
    Given an array of integers, and a number ‘sum’, find the number of pairs of
    integers in the array whose sum is equal to ‘sum’.

Execution: python pairs_with_sum.py
"""
from typing import List
import unittest


def pairs_with_sum(arr: List[int], s: int) -> int:
    """
    Returns number of pairs in arr[0..n-1] with sum equal to 'sum'
    """
    # Initialize result.
    count = 0
    # Consider all possible pairs and check their sums.
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == s:
                count += 1
    return count


class TestPairsWithSum(unittest.TestCase):
    """Unit test for pairs_with_sum."""

    def test_1(self):
        x = [1, 5, 7, -1, 5]
        self.assertEqual(pairs_with_sum(x, 6), 3)


if __name__ == "__main__":
    unittest.main()
