"""
Title: Calculate the Hamming weight.

Problem:
    Write a function that takes an unsigned integer and return the number of
    '1' bits it has (also known as the Hamming weight).

Execution: python hamming_weight.py
"""
import unittest


def hamming_weight(n: int) -> int:
    """Function for calculating the Hamming distance."""
    s = 0
    while n != 0:
        s += 1
        n &= n - 1
    return s


class TestHammingWeight(unittest.TestCase):
    """Unit test for hamming_weight."""

    def test_1(self):
        input_list = int("00000000000000000000000000001011", 2)
        self.assertEqual(hamming_weight(input_list), 3)

    def test_2(self):
        input_list = int("00000000000000000000000010000000", 2)
        self.assertEqual(hamming_weight(input_list), 1)

    def test_3(self):
        input_list = int("11111111111111111111111111111101", 2)
        self.assertEqual(hamming_weight(input_list), 31)


if __name__ == "__main__":
    unittest.main()
