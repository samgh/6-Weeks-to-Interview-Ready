"""
Title: n-digit sum.

Problem:
    Recursive function to count 'n' digit  numbers with sum of digits as 'sum'
    This function considers leading 0's  also as digits, that is why not
    directly called.

Execution: python n_digit_sum.py
"""
import unittest


def count_rec(n: int, sum_val: int) -> int:
    # Base case.
    if n == 0:
        return sum_val == 0

    if sum_val == 0:
        return 1

    # Initialize answer.
    ans = 0

    # Traverse through every digit and  count numbers beginning with it using
    # recursion.
    for i in range(10):
        if sum_val - i >= 0:
            ans = ans + count_rec(n - 1, sum_val - i)

    return ans


def final_count(n: int, sum_val: int) -> int:
    """
    This is mainly a wrapper over countRec. It explicitly handles leading digit
    and calls countRec() for remaining digits.
    """

    # Initialize final answer.
    ans = 0

    # Traverse through every digit from 1 to 9 and count numbers beginning with
    # it.
    for i in range(1, 10):
        if sum_val - i >= 0:
            ans = ans + count_rec(n - 1, sum_val - i)

    return ans


class TestNDigitSum(unittest.TestCase):
    """Unit tests for n_digit_sum."""

    def test_1(self):
        n = 2
        sum_val = 5
        self.assertEqual(final_count(n, sum_val), 5)


if __name__ == "__main__":
    unittest.main()
