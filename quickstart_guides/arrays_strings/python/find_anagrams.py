"""
Title: Find anagrams

Problem:
    Given a string s and a non-empty string p, find all the start indices of
    p's anagrams in s.

    Strings consists of lowercase English letters only and the length of both
    strings s and p will not be larger than 20,100.

    The order of output does not matter.

Execution: python find_anagrams.py
"""
from collections import Counter
from typing import List
import unittest


def find_anagrams(s: str, p: str) -> List[int]:
    pattern_counter = Counter(p)
    running_counter = Counter()
    len_p = len(p)
    result = []

    for i in range(len(s)):

        # If index  >= length of the pattern.  then decrement the count of the
        # (i - len_p)th character to remove it from the current (sliding)
        # window.
        if i >= len_p:
            running_counter[s[i - len_p]] -= 1

            if running_counter[s[i - len_p]] == 0:
                del running_counter[s[i - len_p]]

        # Default: just increment the count of the current character.
        running_counter[s[i]] += 1

        # At any time, if running_counter == pattern_counter then append the
        # result.
        if running_counter == pattern_counter:
            result.append(i - len_p + 1)

    return result


class TestCompareVersion(unittest.TestCase):
    """Unit tests for compare_version."""

    def test_1(self):
        self.assertEqual(find_anagrams("cbaebabacd", "abc"), [0, 6])

    def test_2(self):
        self.assertEqual(find_anagrams("abab", "ab"), [0, 1, 2])


if __name__ == "__main__":
    unittest.main()
