"""
Title: Reverse string

Problem:
    Write a function that reverses a string. The input string is given as an
    array of characters char[].

    Do not allocate extra space for another array, you must do this by modifying
    the input array in-place with O(1) extra memory.

    You may assume all the characters consist of printable ascii characters.

Execution: python reverse_string.py
"""
from typing import List
import unittest


def reverse_string(s: List[str]) -> List[str]:
    def helper(left, right):
        if left < right:
            s[left], s[right] = s[right], s[left]
            helper(left + 1, right - 1)

    helper(0, len(s) - 1)
    return s


class TestReverseString(unittest.TestCase):
    """Unit tests for reverse_string."""

    def test_1(self):
        test_input = ["h", "e", "l", "l", "o"]
        expected_output = ["o", "l", "l", "e", "h"]
        self.assertEqual(reverse_string(test_input), expected_output)

    def test_2(self):
        test_input = ["H", "a", "n", "n", "a", "h"]
        expected_output = ["h", "a", "n", "n", "a", "H"]
        self.assertEqual(reverse_string(test_input), expected_output)


if __name__ == "__main__":
    unittest.main()
