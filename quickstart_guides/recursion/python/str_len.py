"""
Title: String length.

Problem:
    Calculate length of string recursively.

Execution: python deletion.py
"""
from typing import List
import unittest


# Recursive length calculation: O(n)
def str_len(input_str):
    if input_str == '':
        return 0
    return 1 + str_len(input_str[1:])


class TestStrLen(unittest.TestCase):
    """Unit test for str_len."""

    def test_1(self):
        input_str = "xyz"
        self.assertEqual(str_len(input_str), 3)

    def test_2(self):
        input_str = "xyzabc"
        self.assertEqual(str_len(input_str), 6)


if __name__ == '__main__':
    unittest.main()

