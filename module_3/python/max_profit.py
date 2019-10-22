"""
Title: Max profit

Problem:
        Say you have an array for which the ith element is the price of a given
        stock on day i.

        If you were only permitted to complete at most one transaction (i.e., buy one
        and sell one share of the stock), design an algorithm to find the maximum
        profit.

        Note that you cannot sell a stock before you buy one.

Execution: python max_profit.py
"""
import unittest
from typing import List


def max_profit(prices: List[int]):
    """Function for calculating the max profit."""
    min_price = float("inf")
    max_profit = 0
    for i in range(len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
        elif prices[i] - min_price > max_profit:
            max_profit = prices[i] - min_price
    return max_profit


class TestMaxProfit(unittest.TestCase):
    """Unit test for Max Profit."""

    def test_1(self):
        test_input_1 = [7, 1, 5, 3, 6, 4]
        self.assertEqual(max_profit(test_input_1), 5)

        explanation = """
            Explanation: Buy on day 2 (price = 1) and
            sell on day 5 (price = 6), profit = 6 - 1 = 5.
        """
        print(explanation)

    def test_2(self):
        test_input_2 = [7, 6, 4, 3, 1]
        self.assertEqual(max_profit(test_input_2), 0)
    
        explanation = """
            In this case, no transaction is  done, i.e. max profit = 0.
        """
        print(explanation)


if __name__ == '__main__':
    unittest.main()
