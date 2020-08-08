"""
Title: Reverse bits

Problem:
    Reverse bits of a given 32 bits unsigned integer.

Execution: python reverse_unsigned.py
"""
import unittest


def reverse_unsigned(n: int) -> int:
    """Reverse an unsigned integer."""
    return int("{:032b}".format(n)[::-1], 2)


class TestReverseUnsigned(unittest.TestCase):
    """Unit test for reverse_unsigned."""

    def test_1(self):
        input_1 = int("00000010100101000001111010011100", 2)
        output_1 = int("00111001011110000010100101000000", 2)
        self.assertEqual(int(reverse_unsigned(input_1)), output_1)

    def test_2(self):
        input_1 = int("11111111111111111111111111111101", 2)
        output_1 = int("10111111111111111111111111111111", 2)
        self.assertEqual(int(reverse_unsigned(input_1)), output_1)


if __name__ == "__main__":
    unittest.main()
