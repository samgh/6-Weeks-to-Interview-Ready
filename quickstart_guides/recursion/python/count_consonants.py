"""
Title: Count consonants.

Problem:
    Count consonants recursively.

Execution: python count_consonants.py
"""
from typing import List
import unittest



def count_consonants(input_str: str) -> int:
    vowels = "aeiou"

    if input_str == '':
        return 0

    if input_str[0].lower() not in vowels and input_str[0].isalpha():
        return 1 + count_consonants(input_str[1:])
    else:
        return count_consonants(input_str[1:])

class TestCountConsonants(unittest.TestCase):
    """Unit test for count_consonants."""

    def test_1(self):
        input_str = "abc de"
        self.assertEqual(count_consonants(input_str), 3)


if __name__ == '__main__':
    unittest.main()

