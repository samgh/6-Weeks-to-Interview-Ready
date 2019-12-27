"""
Title: Is even or odd

Problem: 
    Write a program to determine if a given number is even or odd.
    Do not make use of the modulus operator.

Execution: python is_even_odd.py
"""
from typing import List
import unittest


def is_even_odd(x: int) -> str:
    if x & 1 == 0:
        return "Even"
    else:
        return "Odd"


class TestIsEvenOdd(unittest.TestCase):
    """Unit test for is_even_odd."""

    def test_1(self):
        self.assertEqual(is_even_odd(26), "Even")

    def test_2(self):
        self.assertEqual(is_even_odd(25), "Odd")


if __name__ == '__main__':
    unittest.main()

