/*
 *   Title: Climb stairs
 *
 *   Problem:
 *      You are climbing a stair case. It takes n steps to reach to the top.
 *
 *      Each time you can either climb 1 or 2 steps. In how many distinct ways can you
 *      climb to the top?
 * 
 *      Note: Given n will be a positive integer.
 *
 *   Execution: javac ClimbStairs.java && java ClimbStairs
 */


public class ClimbStairs {
    public static int climbStairsBF(int n) {
        /* Brute-force implementation of climb stairs.*/
        return climbStairsBF(0, n);
    }
    public static int climbStairsBF(int i, int n) {
        if (i > n) {
            return 0;
        }
        if (i == n) {
            return 1;
        }
        return climbStairsBF(i + 1, n) + climbStairsBF(i + 2, n);
    }
    public static int climbStairsRec(int n) {
        /* Recursion with memoizaition.*/
        int memo[] = new int[n + 1];
        return climbStairsRec(0, n, memo);
    }
    public static int climbStairsRec(int i, int n, int memo[]) {
        if (i > n) {
            return 0;
        }
        if (i == n) {
            return 1;
        }
        if (memo[i] > 0) {
            return memo[i];
        }
        memo[i] = climbStairsRec(i + 1, n, memo) + climbStairsRec(i + 2, n, memo);
        return memo[i];
    }

    public static int climbStairsDP(int n) {
        /* Dynamic programming implementation.*/ 
        if (n == 1) {
            return 1;
        }
        int[] dp = new int[n + 1];
        dp[1] = 1;
        dp[2] = 2;
        for (int i = 3; i <= n; i++) {
            dp[i] = dp[i - 1] + dp[i - 2];
        }
        return dp[n];
    }

    public static void main(String[] args) {
        assert climbStairsBF(2) == 2;
        System.out.println("Brute-force implementation:");
        System.out.println("There are two ways to climb to the top. 1. 1 step + 1 step 2. 2 steps");

        assert climbStairsRec(2) == 2;
        System.out.println("Recursive implementation:");
        System.out.println("There are two ways to climb to the top. 1. 1 step + 1 step 2. 2 steps");

        assert climbStairsDP(2) == 2;
        System.out.println("Dynamic programming implementation:");
        System.out.println("There are two ways to climb to the top. 1. 1 step + 1 step 2. 2 steps");

        System.out.println("Passed all test cases");
    }
    
}
