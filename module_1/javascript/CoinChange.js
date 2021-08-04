/**
 *   Title: Coin Change
 *   Leetcode Link: https://leetcode.com/problems/coin-change/
 *
 *   Problem: You are given coins of different denominations and a total amount
 *   of money amount. Write a function to compute the fewest number of coins
 *   that you need to make up that amount. If that amount of money cannot be
 *   made up by any combination of the coins, return -1.
 *
 *   Input:
 *      number[] coins  => denominations of coins available
 *      number amount   => amount of change to make
 *   Output:
 *      number          => minimum number of coins needed
 *
 *   Execution: node CoinChange.js
 */

 /**
  * Solution #1: Brute Force
  *
  * Recursively find every combination of coins and find the combination that
  * uses the fewest number of coins.
  *
  * Time Complexity: O(len(coins)^amount)
  * Space Complexity: O(amount)
  *
  * @param {number[]} coins
  * @param {number} amount
  * @return {number}
  */
var coinChangeBF = function(coins, amount) {
    // Base case. Invalid combination of coins
    if (amount < 0) return -1;

    // Base case. Found a valid combination
    if (amount == 0) return 0;

    // Try subtracting each coin from the total amount and see how many
    // coins it would take to generate the remaining amount of change
    var minCoins = Number.POSITIVE_INFINITY;
    var foundValid = false;

    coins.forEach(function(c) {
        var currChange = coinChangeBF(coins, amount-c);

        // If the result is -1, that means there is no valid combination if
        // we remove coin c from the current amount
        if (currChange >= 0) {
            minCoins = Math.min(minCoins, (currChange+1));
            foundValid = true;
        }
    });

    if (foundValid) return minCoins;
    return -1;
};

/**
 * Solution #2: Top-down (memoized) DP Solution
 *
 * Recursively find every combination of coins and find the combination that
 * uses the fewest number of coins. Use memoization to optimize duplicated
 * recusive calls
 *
 * Time Complexity: O(coins * amount)
 * Space Complexity: O(amount)
 *
 * @param {number[]} coins
 * @param {number} amount
 * @return {number}
 */
var coinChangeTD = function(coins, amount) {
    if (amount < 0) return -1;

    // Initialize dp array to size amount+1
    var dp = [];
    var arraySize = amount+1;
    while (arraySize--) dp.push(0);

    return coinChangeTDInner(coins, amount, dp);
}

var coinChangeTDInner = function(coins, amount, dp) {
    // Base case. Invalid combination of coins
    if (amount < 0) return -1;

    // Base case. Found a valid combination
    if (amount == 0) return 0;

    // Check the dp array to make sure we haven't already computed the value
    if (dp[amount] == 0) {
        // If we haven't already computed the value, this is the same as the
        // brute force solution: Try subtracting each coin from the total
        // amount and see how many coins it would take to generate the
        // remaining amount of change
        var minCoins = Number.POSITIVE_INFINITY;
        var foundValid = false;

        coins.forEach(function(c) {
            var currChange = coinChangeTDInner(coins, amount-c, dp);

            // If the result is -1, that means there is no valid combination if
            // we remove coin c from the current amount
            if (currChange >= 0) {
                minCoins = Math.min(minCoins, currChange+1);
                foundValid = true;
            }
        });

        // Save computed value to dp array
        if (foundValid) dp[amount] = minCoins;
        else dp[amount] = -1;
    }

    // Return the computed value from the dp array
    return dp[amount];
}

/**
 * Solution #3: Bottom-up (tabulated) DP Solution
 *
 * Iteratively compute the solutions to each incremental subproblem from
 * 1 to amount. Highly recommend starting with recursive solution to
 * better understand this solution
 *
 * Time Complexity: O(coins * amount)
 * Space Complexity: O(amount)
 *
 * @param {number[]} coins
 * @param {number} amount
 * @return {number}
 */
var coinChangeBU = function(coins, amount) {
    if (amount < 0) return -1;

    // Initialize dp array to size amount+1
    var dp = [];
    var arraySize = amount+1;
    while(arraySize--) dp.push(0);

    // Iteratively generate results of subproblems. This is the same as the
    // recursive solution, except that we look in our dp array for the
    // solutions to subproblems rather than making recursive calls
    for (var i = 1; i < dp.length; i++) {
        var minCoins = Number.POSITIVE_INFINITY;
        var foundValid = false;

        // For each coin, see how many coins it would take to compute the
        // remaining change if we remove it from amount
        coins.forEach(function(c) {
            // We can only remove coin if it is less than the amount and
            // there is a valid way to make amount-coin change
            if (i - c >= 0 && dp[i-c] >= 0) {
                minCoins = Math.min(minCoins, dp[i-c]+1);
                foundValid = true;
            }
        });

        // Once we find the minimum number of coins, update dp
        if (foundValid) dp[i] = minCoins;
        else dp[i] = -1;
    }

    return dp[amount];
}

var tester = function() {
    console.assert(coinChangeBU([1,2,5], 11) === 3);
    console.assert(coinChangeBU([2], -3) === -1);
    console.assert(coinChangeBU([1,6,10], 12) === 2);

    // ADD YOUR OWN TESTS HERE
}

tester();
