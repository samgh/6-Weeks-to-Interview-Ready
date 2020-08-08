"""
Title: Longest substring without repeating characters.

Problem:
    Given a string, find the length of the longest substring without repeating
    characters.

Execution: python length_of_longest_substring.py
"""
import unittest


def length_of_longest_substring(s: str) -> int:
    """Given a string, determine the length of the longest substring."""
    last, res, st = dict(), 0, 0
    for i, v in enumerate(s):
        if v not in last or last[v] < st:
            res = max(res, i - st + 1)
        else:
            st = last[v] + 1
        last[v] = i
    return res


class TestLengthOfLongestSubstring(unittest.TestCase):
    """Unit tests for length_of_longest_substring."""

    def test_1(self):
        """Test for string: abcabcbb."""
        self.assertEqual(length_of_longest_substring("abcabcbb"), 3)
        print("Explanation: The answer is 'abc', with the length of 3.")

    def test_2(self):
        """Test for string: bbbbb."""
        self.assertEqual(length_of_longest_substring("bbbbb"), 1)
        print("Explanation: The answer is 'b', with the length of 1.")

    def test_3(self):
        """Test for string: pwwkew."""
        self.assertEqual(length_of_longest_substring("pwwkew"), 3)
        print("Explanation: The answer is 'wke', with the length 3.")
        print("Note that the answer must be a substring, 'pwke' ")
        print("is a subsequence and not a substring.")


if __name__ == "__main__":
    unittest.main()
