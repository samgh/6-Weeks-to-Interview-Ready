/*
 * Title: Pairs with sum
 *
 * Problem:
 *  Given an array of integers, and a number ‘sum’, find the number of pairs of
 *  integers in the array whose sum is equal to ‘sum’.
 *
 * Execution: javac PairsWithSum.java && java PairsWithSum
 */
public class PairsWithSum {

    public static int pairsWithSum(int[] arr, int sum) {
        int count = 0;

        // Consider all possible pairs and check their sums
        for (int i = 0; i < arr.length; i++)
            for (int j = i + 1; j < arr.length; j++)
                if ((arr[i] + arr[j]) == sum)
                    count++;

        return count;
    }
    public static void main(String args[]) {
        int[] arr = { 1, 5, 7, -1, 5 };
        int sum = 6;
        assert pairsWithSum(arr, sum) == 3;
    }
}