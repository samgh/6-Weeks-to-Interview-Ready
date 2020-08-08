"""
Title: Array Combinations

Problem:
    Given two strings, write a function that determines the minimum edit
    distance between the two strings. You can insert and modify
    characters. eg.

    ```
    editDistance("ABCD", "ACBD") = 2 (ABCD->ACCD->ACBD)
    editDistance("AC", "ABCD") = 2 (AC->ABC->ABCD)
    ```

Execution: python edit_distance.py
"""
import unittest
from typing import Dict


def brute_force_edit_distance(s1: str, s2: str) -> float:
    return brute_force_edit_distance_helper(s1, s2, 0, 0)


def brute_force_edit_distance_helper(s1: str, s2: str, i: int, j: int) -> float:
    if i == len(s1):
        return len(s2) - j
    if j == len(s2):
        return len(s1) - i

    # We can swap the characters if they're unequal or do nothing otherwise.
    min_val = brute_force_edit_distance_helper(s1, s2, i + 1, j + 1)
    if s1[i] != s2[j]:
        min_val += 1

    # We can insert a character into s1 or s2
    min_val = min(min_val, brute_force_edit_distance_helper(s1, s2, i + 1, j) + 1)
    min_val = min(min_val, brute_force_edit_distance_helper(s1, s2, i, j + 1) + 1)

    return min_val


def top_down_edit_distance(s1: str, s2: str) -> Dict[int, int]:
    dp = dict()
    for i in range(len(s1) + 1):
        for j in range(len(s2) + 1):
            dp[(i, j)] = -1
    return top_down_edit_distance_helper(s1, s2, 0, 0, dp)


def top_down_edit_distance_helper(
    s1: str, s2: str, i: int, j: int, dp: dict
):
    if dp[(i, j)] == -1:
        if i == len(s1):
            return len(s2) - j
        if j == len(s2):
            return len(s1) - i

        min_val = top_down_edit_distance_helper(s1, s2, i + 1, j + 1, dp)
        if s1[i] != s2[j]:
            min_val += 1

        min_val = min(min_val, top_down_edit_distance_helper(s1, s2, i + 1, j, dp) + 1)
        min_val = min(min_val, top_down_edit_distance_helper(s1, s2, i, j + 1, dp) + 1)
        dp[(i, j)] = min_val

    return dp[(i, j)]


def bottom_up_edit_distance(s1: str, s2: str) -> Dict[int, int]:
    dp = dict()
    for i in range(len(s1) + 1):
        for j in range(len(s2) + 1):
            if i == 0:
                dp[(i, j)] = j
            elif j == 0:
                dp[(i, j)] = i
            else:
                min_val = dp[(i - 1), (j - 1)]
                if s1[i - 1] != s2[j - 1]:
                    min_val += 1
                min_val = min(min_val, dp[(i - 1, j)] + 1)
                min_val = min(min_val, dp[(i, j - 1)] + 1)
                dp[(i, j)] = min_val
    return dp[(len(s1), len(s2))]


class TestEditDistance(unittest.TestCase):
    """Unit test for edit_distance."""

    def test_brute_force(self):
        self.assertEqual(brute_force_edit_distance("A", "A"), 0)
        self.assertEqual(brute_force_edit_distance("A", "B"), 1)
        self.assertEqual(brute_force_edit_distance("ABC", "ACB"), 2)
        self.assertEqual(brute_force_edit_distance("AC", "ABCD"), 2)
        self.assertEqual(brute_force_edit_distance("", "ABCD"), 4)

    def test_top_down(self):
        self.assertEqual(top_down_edit_distance("A", "A"), 0)
        self.assertEqual(top_down_edit_distance("A", "B"), 1)
        self.assertEqual(top_down_edit_distance("ABC", "ACB"), 2)
        self.assertEqual(top_down_edit_distance("AC", "ABCD"), 2)
        self.assertEqual(top_down_edit_distance("", "ABCD"), 4)

    def test_bottom_up(self):
        self.assertEqual(bottom_up_edit_distance("A", "A"), 0)
        self.assertEqual(bottom_up_edit_distance("A", "B"), 1)
        self.assertEqual(bottom_up_edit_distance("ABC", "ACB"), 2)
        self.assertEqual(bottom_up_edit_distance("AC", "ABCD"), 2)
        self.assertEqual(bottom_up_edit_distance("", "ABCD"), 4)


if __name__ == "__main__":
    unittest.main()
