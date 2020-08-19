"""
Title: Sort string

Problem:
    Given a string of lowercase characters from ‘a’ – ‘z’. We need to write a
    program to print the characters of this string in sorted order.

Execution: python sort_string.py
"""
import unittest


def sort_string(s: str) -> str:
    return "".join(sorted(s))


class TestSortString(unittest.TestCase):
    """Unit test for sort_string."""

    def test_1(self):
        s = "bbccdefbbaa"
        self.assertEqual(sort_string(s), "aabbbbccdef")


if __name__ == "__main__":
    unittest.main()
