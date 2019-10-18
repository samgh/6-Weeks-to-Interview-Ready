"""
Title: Calculate the Hamming weight.

Problem: Write a function that takes an unsigned integer and return the number
         of '1' bits it has (also known as the Hamming weight).

Execution: python hamming_weight.py
"""
import unittest


def hamming_weight(n: int):
    """Function for calculating the Hamming weight."""
    sum_val = 0
    while n != 0:
        sum_val += 1
        n &= (n - 1)
    return sum_val


class TestHammingWeight(unittest.TestCase):
    """Unit test for Hamming weight."""

    def test_1(self):
        input_val = "00000000000000000000000000001011"
        self.assertEqual(hamming_weight(int(input_val, 2)), 3)
        output = """
        The input binary string 00000000000000000000000000001011 has a total of
        three '1' bits.
        """
        print(f"Explanation: {output}")

    def test_2(self):
        input_val = "00000000000000000000000010000000"
        self.assertEqual(hamming_weight(int(input_val, 2)), 1)
        output = """
        The input binary string 00000000000000000000000010000000has a total of
        one '1' bit.
        """
        print(f"Explanation: {output}")

    def test_3(self):
        input_val = "11111111111111111111111111111101"
        self.assertEqual(hamming_weight(int(input_val, 2)), 31)
        output = """
        The input binary string 11111111111111111111111111111101 has a total of
        thirty-one '1' bits.
        """
        print(f"Explanation: {output}")


if __name__ == '__main__':
    unittest.main()

