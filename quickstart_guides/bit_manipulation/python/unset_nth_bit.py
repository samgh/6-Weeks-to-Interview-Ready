"""
Title: Unset n^th bit

Problem: 
    Write a program  that takes an integer and
    unsets the n-th bit in the binary representation of
    that integer
    For instance, the binary representation of 6 is:
        110
    The least significant bit is the bit on the far right
    of the binary representation and the most significant
    bit is the bit on the far left. We order the bits as
    b2, b1, b0
    1   1   0
    For our function, if we unset the 1st bit, we should obtain
    the binary representation:
        1 0 0

Execution: python unset_nth_bit.py
"""
from typing import List
import unittest


def unset_nth_bit(x: int, n: int) -> int:
    return x & ~(1 << n)


class TestSetNthBit(unittest.TestCase):
    """Unit test for unset_nth_bit."""

    def test_1(self):
        self.assertEqual(unset_nth_bit(6, 1), 4)

    def test_2(self):
        self.assertEqual(unset_nth_bit(6, 2), 2)

if __name__ == '__main__':
    unittest.main()

