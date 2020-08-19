"""
Title: Distinct permutations of the string.

Problem:
    Returns true if str[curr] does not matches with any of the characters
    after str[start].

Execution: python distinct_perms.py
"""
from typing import List, Optional
import unittest


def should_swap(input_str: List[str], start: int, curr: int) -> bool:
    """Determine if a swap should occur."""
    for i in range(start, curr):
        if input_str[i] == input_str[curr]:
            return False
    return True


def find_perms(input_str: List[str], index: int, n: int, perms: list) -> Optional[List[str]]:
    """
    Prints all distinct permutations in str[0..n-1].
    """
    if index >= n:
        perms.append("".join(input_str))
        return

    for i in range(index, n):
        # Proceed further for str[i] only if it doesn't match with any of the
        # characters after str[index].
        check = should_swap(input_str, index, i)
        if check:
            input_str[index], input_str[i] = input_str[i], input_str[index]
            find_perms(input_str, index + 1, n, perms)
            input_str[index], input_str[i] = input_str[i], input_str[index]
    return perms


class TestDistinctPerms(unittest.TestCase):
    """Unit tests for distinct_perms."""

    def test_1(self):
        expected_res = [
            "abca",
            "abac",
            "acba",
            "acab",
            "aacb",
            "aabc",
            "baca",
            "baac",
            "bcaa",
            "cbaa",
            "caba",
            "caab",
        ]
        input_str = list("abca")
        n = len(input_str)
        perms = []
        res = find_perms(input_str, 0, n, perms)
        self.assertEqual(res, expected_res)


if __name__ == "__main__":
    unittest.main()
