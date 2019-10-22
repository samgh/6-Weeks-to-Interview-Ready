/*
 *   Title: Coin change
 *
 *   Problem: You are given coins of different denominations and a total amount
 *   of money amount. Write a function to compute the fewest number of coins
 *   that you need to make up that amount. If that amount of money cannot be
 *   made up by any combination of the coins, return -1.
 *
 *   Execution: javac XX && java XX
 */


public class CoinChange {
    public static int coinChange(int[] coins, int amount) {
        if (amount < 1) return 0;
        return coinChange(coins, amount, new int[amount]);
    }

    private static int coinChange(int[] coins, int rem, int[] count) {
        if (rem < 0) return -1;
        if (rem == 0) return 0;
        if (count[rem - 1] != 0) return count[rem - 1];
        int min = Integer.MAX_VALUE;
        for (int coin : coins) {
            int res = coinChange(coins, rem - coin, count);
            if (res >= 0 && res < min)
                min = 1 + res;
        }
        count[rem - 1] = (min == Integer.MAX_VALUE) ? -1 : min;
        return count[rem - 1];
    }

    public static void main(String[] args) {
        
        int[] testInputCoins1 = {1, 2, 5};
        int testAmount1 = 11;
        assert coinChange(testInputCoins1, testAmount1) == 3;
        System.out.println("Explanation: 11 = 5 + 5 + 1");

        int[] testInputCoins2 = {2};
        int testAmount2 = 3;
        assert coinChange(testInputCoins1, testAmount1) == -1;

        System.out.println("Passed all test cases");
    }
    
}
