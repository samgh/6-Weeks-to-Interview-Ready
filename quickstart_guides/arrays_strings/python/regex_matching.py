"""
Title: Regex matching

Problem: 
    Given an input string (s) and a pattern (p), implement regular expression
    matching with support for '.' and '*'.

    '.' Matches any single character.  '*' Matches zero or more of the
    preceding element.  The matching should cover the entire input string (not
    partial).

    Note:

    s could be empty and contains only lowercase letters a-z.  p could be empty
    and contains only lowercase letters a-z, and characters like . or *.

Execution: python regex_matching.py
"""
from typing import Dict
import unittest


def regex_matching_top_down(text: str, pattern: str) -> Dict[int, int]:
    memo = dict()

    def dp(i, j) -> Dict[int, int]:
        if (i, j) not in memo:
            if j == len(pattern):
                ans = i == len(text)
            else:
                first_match = i < len(text) and pattern[j] in {text[i], "."}
                if j + 1 < len(pattern) and pattern[j + 1] == "*":
                    ans = dp(i, j + 2) or first_match and dp(i + 1, j)
                else:
                    ans = first_match and dp(i + 1, j + 1)

            memo[i, j] = ans
        return memo[i, j]

    return dp(0, 0)


def regex_matching_bottom_up(text: str, pattern: str) -> bool:
    dp = [[False] * (len(pattern) + 1) for _ in range(len(text) + 1)]

    dp[-1][-1] = True
    for i in range(len(text), -1, -1):
        for j in range(len(pattern) - 1, -1, -1):
            first_match = i < len(text) and pattern[j] in {text[i], "."}
            if j + 1 < len(pattern) and pattern[j + 1] == "*":
                dp[i][j] = dp[i][j + 2] or first_match and dp[i + 1][j]
            else:
                dp[i][j] = first_match and dp[i + 1][j + 1]

    return dp[0][0]


class TestRegexMatching(unittest.TestCase):
    """Unit test for regex_matching."""

    def test_1(self):
        a = "aa"
        p = "a"
        self.assertEqual(regex_matching_top_down(a, p), False)
        self.assertEqual(regex_matching_bottom_up(a, p), False)

    def test_2(self):
        a = "aa"
        p = "a*"
        self.assertEqual(regex_matching_top_down(a, p), True)
        self.assertEqual(regex_matching_bottom_up(a, p), True)

    def test_3(self):
        a = "ab"
        p = ".*"
        self.assertEqual(regex_matching_top_down(a, p), True)
        self.assertEqual(regex_matching_bottom_up(a, p), True)

    def test_4(self):
        a = "aab"
        p = "c*a*b"
        self.assertEqual(regex_matching_top_down(a, p), True)
        self.assertEqual(regex_matching_bottom_up(a, p), True)

    def test_5(self):
        a = "mississippi"
        p = "mis*is*p*."
        self.assertEqual(regex_matching_top_down(a, p), False)
        self.assertEqual(regex_matching_bottom_up(a, p), False)


if __name__ == "__main__":
    unittest.main()
