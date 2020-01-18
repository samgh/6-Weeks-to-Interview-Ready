"""
Title: Find uppercase.

Problem:
    Find uppercase letters in string.

Execution: python find_uppercase.py
"""
import unittest


def find_uppercase(input_str, idx=0):
    if input_str[idx].isupper():
        return input_str[idx]
    if idx == len(input_str) - 1:
        return "No uppercase character found"
    return find_uppercase(input_str, idx+1)


class TestFindUppercase(unittest.TestCase):
    """Unit test for find_uppercase."""

    def test_1(self):
        input_str_1 = "lucidProgramming"
        self.assertEqual(find_uppercase(input_str_1), 1)

    def test_2(self):
        input_str_2 = "LucidProgramming"
        self.assertEqual(find_uppercase(input_str_2), 2)

    def test_3(self):
        input_str_3 = "lucidprogramming"
        self.assertEqual(find_uppercase(input_str_3), 0)


if __name__ == '__main__':
    unittest.main()

