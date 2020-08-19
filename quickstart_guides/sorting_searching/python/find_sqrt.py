"""
Title: Square root.

Problem:
    Implement int sqrt(int x).

    Compute and return the square root of x, where x is guaranteed to be a
    non-negative integer.

    Since the return type is an integer, the decimal digits are truncated and
    only the integer part of the result is returned.

Execution: python find_sqrt.py
"""
import unittest


def find_sqrt(x: int) -> int:
    guess = x
    epsilon = 10 ** (-4)

    while abs(x - guess * guess) > epsilon:
        guess = (guess + x / guess) / 2

    return int(guess)


class TestFindSqrt(unittest.TestCase):
    """Unit test for find_sqrt."""

    def test_1(self):
        self.assertEqual(find_sqrt(4), 2)

    def test_2(self):
        self.assertEqual(find_sqrt(16), 4)


if __name__ == "__main__":
    unittest.main()
