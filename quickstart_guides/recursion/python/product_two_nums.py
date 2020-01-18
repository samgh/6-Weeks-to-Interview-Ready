"""
Title: Product two numbers.

Problem:
    Product of two numbers recursively.

Execution: python product_two_nums.py
"""
import unittest


def product_two_nums(x: int, y: int) -> int:

    # This cuts down on the total number of
    # recursive calls:
    if x < y:
        return product_two_nums(y, x)
    if y == 0:
        return 0
    return x + product_two_nums(x, y-1)


class TestProductTwoNums(unittest.TestCase):
    """Unit test for product_two_nums."""

    def test_1(self):
        x = 500
        y = 2000
        self.assertEqual(product_two_nums(x, y), 1000000)


if __name__ == '__main__':
    unittest.main()

