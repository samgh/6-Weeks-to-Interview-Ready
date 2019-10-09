/*
 *   Title: Max Profit
 *
 *   Problem:
        Say you have an array for which the ith element is the price of a given
        stock on day i.

        If you were only permitted to complete at most one transaction (i.e., buy one
        and sell one share of the stock), design an algorithm to find the maximum
        profit.

        Note that you cannot sell a stock before you buy one.
 *
 *   Execution: javac MaxProfit.java && java MaxProfit
 */


public class MaxProfit {
    public static int maxProfit(int prices[]) {
        int min_price = Integer.MAX_VALUE;
        int max_profit = 0;
        for (int i = 0; i < prices.length; i++) {
            if (prices[i] < min_price)
                min_price = prices[i];
            else if (prices[i] - min_price > max_profit)
                max_profit = prices[i] - min_price;
        }
        return max_profit;
    }

    public static void main(String[] args) {
        int[] test_input_1 = new int[]{7, 1, 5, 3, 6, 4};
        assert maxProfit(test_input_1) == 5;
        String explanation_1 = "Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6 - 1 = 5.";
        System.out.println(explanation_1);

        int[] test_input_2 = new int[]{7, 6, 4, 3, 1};
        assert maxProfit(test_input_2) == 0;
        String explanation_2 = "In this case, no transaction is  done, i.e. max profit = 0.";
        System.out.println(explanation_2);

        System.out.println("Passed all test cases");
    }
    
}
