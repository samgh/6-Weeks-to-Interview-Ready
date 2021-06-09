"""
Title: Coin Change
Leetcode Link: https://leetcode.com/problems/coin-change/

Problem: You are given coins of different denominations and a total amount
of money amount. Write a function to compute the fewest number of coins
that you need to make up that amount. If that amount of money cannot be
made up by any combination of the coins, return -1.

Input:
    coins: List[int]    => denominations of coins available
    amount: int         => amount of change to make
Output:
    int                 => minimum number of coins needed

Execution: python coin_change.py
"""

import unittest
from typing import List

"""
Solution #1: Brute Force

Recursively find every combination of coins and find the combination that
uses the fewest number of coins.

Time Complexity: O(len(coins)^amount)
Space Complexity: O(amount)
"""
def coin_change_bf(coins: List[int], amount: int) -> int:
    # Base case. Invalid combination of coins
    if amount < 0:
        return -1

    #Base case. Found a valid combination
    if amount == 0:
        return 0

    # Try subtracting each coin from the total amount and see how many coins it
    # would take to generate the remaining amount of change
    min_coins = float('inf')

    for c in coins:
        curr_change = coin_change_bf(coins, amount-c)

        # If the result is -1, that means there is no valid combination if we
        # remove coin c from the current amount
        if curr_change >= 0:
            min_coins = min(min_coins, curr_change+1)

    if min_coins == float('inf'):
        return -1
    return min_coins

"""
Solution #2: Top-down (memoized) DP Solution

Recursively find every combination of coins and find the combination that
uses the fewest number of coins. Use memoization to optimize duplicated
recusive calls

Time Complexity: O(coins * amount)
Space Complexity: O(amount)
"""
def coin_change_td(coins: List[int], amount: int) -> int:
    dp = [0]*(amount+1)
    return coin_change_td_inner(coins, amount, dp)

def coin_change_td_inner(coins: List[int], amount: int, dp: List[int] = {}):
    # Base case. Invalid combination of coins
    if amount < 0:
        return -1

    #Base case. Found a valid combination
    if amount == 0:
        return 0

    # Check the dp list to make sure we haven't already computed the value
    if dp[amount] == 0:
        # If we haven't already computed the value, this is the same as the
        # brute force solution: Try subtracting each coin from the total amount
        # and see how many coins it would take to generate the remaining amount
        # of change
        min_coins = float('inf')

        for c in coins:
            curr_change = coin_change_td_inner(coins, amount-c, dp)

            # If the result is -1, that means there is no valid combination if we
            # remove coin c from the current amount
            if curr_change >= 0:
                min_coins = min(min_coins, curr_change+1)

        # Save computed value to dp array
        if min_coins == float('inf'):
            dp[amount] = -1
        else:
            dp[amount] = min_coins

    # Return the computed value from the dp array
    return dp[amount]

"""
Solution #3: Bottom-up (tabulated) DP Solution

Iteratively compute the solutions to each incremental subproblem from 1 to
amount. Highly recommend starting with recursive solution to better understand
this solution

Time Complexity: O(coins * amount)
Space Complexity: O(amount)
"""
def coin_change_bu(coins: List[int], amount: int) -> int:
    if amount < 0:
        return -1

    dp = [0]*(amount+1)

    # Iteratively generate results of subproblems. This is the same as the
    # recursive solution, except that we look in our dp array for the
    # solutions to subproblems rather than making recursive calls
    for i in range(1, len(dp)):
        min_coins = float('inf')

        # For each coin, see how many coins it would take to compute the
        # remaining change if we remove it from amount
        for c in coins:
            # We can only remove coin if it is less than the amount and there is
            # a valid way to make amount-coin change
            if i-c >= 0 and dp[i-c] >= 0:
                min_coins = min(min_coins, dp[i-c]+1)

        # Once we find the minimum number of coins, update dp
        if min_coins == float('inf'):
            dp[i] = -1
        else:
            dp[i] = min_coins

    print(dp)
    return dp[amount]


class TestCoinChange(unittest.TestCase):
    """Unit test for CoinChange."""

    def test_1(self):
        self.assertEqual(coin_change_bu(coins=[1, 2, 5], amount=11), 3)

    def test_2(self):
        self.assertEqual(coin_change_bu(coins=[2], amount=3), -1)

    def test_3(self):
        self.assertEqual(coin_change_bu(coins=[1,6,10], amount=12), 2)

    # ADD YOUR OWN TESTS HERE

if __name__ == '__main__':
    unittest.main()
