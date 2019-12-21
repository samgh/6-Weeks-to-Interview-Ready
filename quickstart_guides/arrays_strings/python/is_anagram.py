"""
Title: Is Anagram

Problem: 
    Given two strings s and t , write a function to determine if t is an
    anagram of s.

Execution: python is_anagram.py
"""
import unittest


def is_anagram_sorting(s: str, t: str) -> bool:
    """Check if string s is anagram of string t."""
    if len(s) != len(t):
        return False
    s = sorted(s)
    t = sorted(t)
    return s == t


class TestIsAnagram(unittest.TestCase):
    """Unit test for is_anagram."""

    def test_1(self):
        s = "anagram"
        t = "nagaram"
        self.assertEqual(is_anagram_sorting(s, t), True)

    def test_2(self):
        s = "rat"
        t = "car"
        self.assertEqual(is_anagram_sorting(s, t), False)


if __name__ == '__main__':
    unittest.main()

