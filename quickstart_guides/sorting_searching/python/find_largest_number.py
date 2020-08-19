"""
Title: Find largest number

Problem:
    Given a list of non negative integers, arrange them such that they form the
    largest number.

Execution: python find_largest_number.py
"""
from typing import List
import unittest


class LargerNumKey(str):
    def __lt__(x, y):
        return x + y > y + x


def find_largest_number(nums: List[int]) -> str:
    largest_num = "".join(sorted(map(str, nums), key=LargerNumKey))
    return "0" if largest_num[0] == "0" else largest_num


class TestFindLargest(unittest.TestCase):
    """Unit test for find_sqrt."""

    def test_1(self):
        self.assertEqual(find_largest_number([10, 2]), "210")

    def test_2(self):
        self.assertEqual(find_largest_number([3, 30, 34, 5, 9]), "9534330")


if __name__ == "__main__":
    unittest.main()
