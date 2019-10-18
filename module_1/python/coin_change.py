"""
Title: Coin change problem.

Problem: You are given coins of different denominations and a total amount of
         money amount. Write a function to compute the fewest number of coins that you
         need to make up that amount. If that amount of money cannot be made up by any
         combination of the coins, return -1.

Execution: python coin_change.py
"""
import unittest
from typing import List


def coin_change(coins: List[int], amount: int):
    """Function for generating coin change."""
    if amount < 1:
        return 0
    return coin_change_recur(coins, amount, [0]*amount)


def coin_change_recur(coins: List[int], rem: int, count: List[int]):
    if rem < 0:
        return -1
    if rem == 0:
        return 0
    if count[rem - 1] != 0:
        return count[rem - 1]
    min_val = float("inf")
    for coin in coins:
        res = coin_change_recur(coins, rem - coin, count)
        if res >= 0 and res < min_val:
            min_val = 1 + res
    if min_val == float("inf"):
        count[rem - 1] = -1
    else:
        count[rem - 1] = min_val
    return count[rem - 1]


class TestCoinChange(unittest.TestCase):
    """Unit test for CoinChange."""

    def test_1(self):
        self.assertEqual(coin_change(coins=[1, 2, 5], amount=11), 3)

    def test_2(self):
        self.assertEqual(coin_change(coins=[2], amount=3), -1)


if __name__ == '__main__':
    unittest.main()
