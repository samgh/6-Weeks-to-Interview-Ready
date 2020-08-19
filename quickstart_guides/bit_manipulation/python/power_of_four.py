"""
Title: Power of four

Problem: 
    Given an integer, write a function to determine if it is a power of four.

Execution: python power_of_four.py
"""
from math import log
import unittest


def power_of_four(n: int) -> bool:
    return n > 0 and log(n, 4).is_integer()


class TestPowerOfFourr(unittest.TestCase):
    """Unit test for power_of_four."""

    def test_1(self):
        self.assertEqual(power_of_four(16), True)

    def test_2(self):
        self.assertEqual(power_of_four(5), False)

    def test_3(self):
        self.assertEqual(power_of_four(64), True)

    def test_4(self):
        self.assertEqual(power_of_four(18), False)


if __name__ == "__main__":
    unittest.main()
