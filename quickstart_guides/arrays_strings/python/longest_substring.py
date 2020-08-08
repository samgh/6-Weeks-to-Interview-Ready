"""
Title: Longest substring

Problem: 
    Given two strings, write a function that returns the longest common
    substring. e.g.

    ```
    longestSubstring("ABAB", "BABA") = "ABA"
    ```

Execution: python longest_substring.py
"""
from collections import defaultdict
import unittest


def longest_substring(a: str, b: str) -> str:
    out = ""
    if len(a) == 0 or len(b) == 0:
        return out

    str_len = 0
    cache = defaultdict(dict)
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                if i == 0 or j == 0:
                    cache[i][j] = 1
                else:
                    cache[i][j] = cache[i - 1][j - 1] + 1
                if cache[i][j] > str_len:
                    str_len = cache[i][j]
                    out = a[i - str_len + 1 : i + 1]
    return out


class TestLongestSubstring(unittest.TestCase):
    """Unit test for longest_substring."""

    def test_1(self):
        a = "ABAB"
        b = "BABA"
        self.assertEqual(longest_substring(a, b), "ABA")


if __name__ == "__main__":
    unittest.main()
