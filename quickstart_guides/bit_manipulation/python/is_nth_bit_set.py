"""
Title: Is n^th bit set.

Problem: 
    Write a program that takes an integer and tests whether
    the n-th bit in the binary representation of that integer
    is set of not.

    For instance, the binary representation of 6 is:
        110
    The least significant bit is the bit on the far right
    of the binary representation and the most significant
    bit is the bit on the far left. We order the bits as

    b2, b1, b0
    1   1   0

    For our function, if we check the 0th bit, we should obtain
    "False" as the binary value at b0 is 0.
    Alternatively, if we check the 1st bit, we should obtain
    "True" as the binary value at b1 is 1.

Execution: python is_nth_bit_set.py
"""
from typing import List
import unittest


def is_nth_bit_set(x: int, n: int) -> bool:
    if x & (1 << n):
        return True
    return False


class TestIsNthBitSet(unittest.TestCase):
    """Unit test for is_nth_bit_set."""

    def test_1(self):
        self.assertEqual(is_nth_bit_set(6, 2), True)

    def test_2(self):
        self.assertEqual(is_nth_bit_set(6, 0), False)


if __name__ == '__main__':
    unittest.main()

