"""
Title: Recursive factorial

Problem:
    Calculate factorial of integer recursively.

Execution: python factorial.py
"""
from typing import List
import unittest


def factorial(n: int) -> int:
    if n == 1:
        return n
    else:
        return n * factorial(n-1)


class TestFactorial(unittest.TestCase):
    """Unit test for factorial."""

    def test_1(self):
        self.assertEqual(factorial(7), 5040)

    def test_2(self):
        self.assertEqual(factorial(1), 1)

    def test_3(self):
        self.assertEqual(factorial(4), 24)


if __name__ == '__main__':
    unittest.main()

