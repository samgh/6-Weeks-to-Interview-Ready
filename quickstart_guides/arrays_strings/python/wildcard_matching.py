"""
Title: Wildcard matching

Problem: 
    Given an input string (s) and a pattern (p), implement wildcard pattern
    matching with support for '?' and '*'.

    '?' Matches any single character.  '*' Matches any sequence of characters
    (including the empty sequence). The matching should cover the entire input
    string (not partial).

    Note:

    s could be empty and contains only lowercase letters a-z.  p could be empty
    and contains only lowercase letters a-z, and characters like ? or *.

Execution: python wildcard_matching.py
"""
import unittest


def wildcard_matching(a: str, b: str) -> bool:
    if len(a) == len(b) == 0:
        return True
    res = False
    seen = set()
    dfs(a, b, 0, 0, seen, res)
    return res


def dfs(s, p, i, j, seen, res) -> None:
    if (i, j) in seen:
        return

    # Recursion exit condition.
    if j > len(p) - 1:
        return

    # Generate multiple cases.
    if p[j] == "*":
        for i in range(i, len(s)):
            if (i, j + 1) not in seen:
                dfs(s, p, i, j + 1, seen, res)
                seen.add((i, j + 1))
            else:
                return

    elif i < len(s) and (p[j] == "?" or s[i] == p[j]):
        if (i + 1, j + 1) not in seen:
            dfs(s, p, i + 1, j + 1, seen, res)
            seen.add((i + 1, j + 1))
        else:
            return


class TestWildcardMatching(unittest.TestCase):
    """Unit test for wildcard_matching."""

    def test_1(self):
        a = "aa"
        p = "a"
        self.assertEqual(wildcard_matching(a, p), False)

    def test_2(self):
        a = "acdcb"
        p = "a*c?b"
        self.assertEqual(wildcard_matching(a, p), False)


if __name__ == "__main__":
    unittest.main()
