"""
Title: Convert string into binary sequence

Problem:
    Given a string of character the task is to convert each character of a
    string into the equivalent binary number.

Execution: python string_to_binary.py
"""
import unittest


def string_to_binary(s: str) -> str:
    bin_conv = list()
    for c in s:
        ascii_val = ord(c)
        binary_val = bin(ascii_val)
        bin_conv.append(binary_val[2:])

    return " ".join(bin_conv)


class TestStringToBinary(unittest.TestCase):
    """Unit tests for string_to_binary."""

    def test_1(self):
        self.assertEqual(string_to_binary("BbB"), "1000010 1100010 1000010")


if __name__ == "__main__":
    unittest.main()
