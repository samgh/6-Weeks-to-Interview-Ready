"""
Title: Sum of two integers

Problem:
    Calculate the sum of two integers a and b, but you are not allowed to use
    the operator + and -.


Execution: python sum_two_ints.py
"""
from typing import List
import unittest


def sum_two_ints(A: int, B: int) -> int:
    """Sum two integers"""
    carry = 0
    r = 0
    for i in range(32):
        a = (A & 1 << i)
        b = (B & 1 << i)
        t = a ^ b ^ carry

        r |= t

        # Case when both bits are 1.
        if (a & b) != 0:
            carry = 1 << (i + 1)
        # Case when a's or b's bit 1 and carry.
        elif (carry != 0 and t == 0):
            carry = 1 << (i + 1)
        else:
            carry = 0

    return r


class TestSumTwoInts(unittest.TestCase):
    """Unit test for sum_two_ints."""

    def test_1(self):
        a = 1
        b = 2
        self.assertEqual(sum_two_ints(a, b), 3)

    def test_2(self):
        a = -2
        b = 3
        self.assertEqual(sum_two_ints(a, b), 1)


if __name__ == '__main__':
    unittest.main()

