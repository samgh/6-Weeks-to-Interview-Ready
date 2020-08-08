"""
Title: Power of two

Problem: 
    Given an integer, write a function to determine if it is a power of two.

Execution: python power_of_two.py
"""
import unittest


def power_of_two(n: int) -> bool:
    """Determine if integer is power of 2."""
    if n <= 0:
        return False
    if n == 1:
        return True
    while n > 1:
        n /= 2
    return n == 1


class TestPowerOfTwo(unittest.TestCase):
    """Unit test for power_of_two."""

    def test_1(self):
        self.assertEqual(power_of_two(1), True)

    def test_2(self):
        self.assertEqual(power_of_two(16), True)

    def test_3(self):
        self.assertEqual(power_of_two(218), False)

    def test_4(self):
        self.assertEqual(power_of_two(64), True)


if __name__ == "__main__":
    unittest.main()
