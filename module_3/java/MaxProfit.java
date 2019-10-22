/*
 *   Title: Max profit
 *
 *   Problem: 
 *
 *   Say you have an array for which the ith element is the price of a
 *   given stock on day i.
 *
 *   If you were only permitted to complete at most one transaction (i.e., buy one
 *   and sell one share of the stock), design an algorithm to find the maximum
 *   profit.
 *
 *   Note that you cannot sell a stock before you buy one.
 *
 *   Execution: javac MaxProfit.java && java MaxProfit
 */


public class MaxProfit {

    public static int maxProfitBF(int prices[]) {
        /* Brute-force implementation of max profit. */
        int maxprofit = 0;
        for (int i = 0; i < prices.length - 1; i++) {
            for (int j = i + 1; j < prices.length; j++) {
                int profit = prices[j] - prices[i];
                if (profit > maxprofit)
                    maxprofit = profit;
            }
        }
        return maxprofit;
    }

    public static int maxProfitOnePass(int prices[]) {
        /* One-pass implementation of max profit. */
        int minprice = Integer.MAX_VALUE;
        int maxprofit = 0;
        for (int i = 0; i < prices.length; i++) {
            if (prices[i] < minprice)
                minprice = prices[i];
            else if (prices[i] - minprice > maxprofit)
                maxprofit = prices[i] - minprice;
        }
        return maxprofit;
    }

    public static void main(String[] args) {
        int[] arr_1 = {7, 1, 5, 3, 6, 4};
        assert maxProfitOnePass(arr_1) == 5;
        assert maxProfitBF(arr_1) == 5;
        System.out.println("Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5. Not 7-1 = 6, as selling price needs to be larger than buying price.");

        int[] arr_2 = {7, 6, 4, 3, 1};
        assert maxProfitOnePass(arr_2) == 0;
        assert maxProfitBF(arr_2) == 0;
        System.out.println("In this case, no transaction is done, i.e. max profit = 0.");

        System.out.println("Passed all test cases");
    }
    
}
