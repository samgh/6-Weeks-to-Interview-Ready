"""
Title: Permutations of set.

Problem:
    A permutation, also called an “arrangement number” or “order,” is a
    rearrangement of the elements of an ordered list S into a one-to-one
    correspondence with S itself. A string of length n has n! permutation.

Execution: python perms_of_set.py
"""
from typing import List
import unittest


def permute(a: List[str], idx_1: int, idx_2: int, perms) -> List[str]:
    """
    Function to print permutations of string.
    """
    if idx_1 == idx_2:
        perms.append("".join(a))
    else:
        for i in range(idx_1, idx_2 + 1):
            a[idx_1], a[i] = a[i], a[idx_1]
            permute(a, idx_1 + 1, idx_2, perms)

            # Backtrack.
            a[idx_1], a[i] = a[i], a[idx_1]
    return perms


class TestPermsOfSet(unittest.TestCase):
    """Unit tests for perms_of_set."""

    def test_1(self):
        expected_res = ["ABC", "ACB", "BAC", "BCA", "CBA", "CAB"]
        tracking_list = []
        input_str = "ABC"
        res = permute(list(input_str), 0, len(input_str) - 1, tracking_list)

        self.assertEqual(res, expected_res)


if __name__ == "__main__":
    unittest.main()
