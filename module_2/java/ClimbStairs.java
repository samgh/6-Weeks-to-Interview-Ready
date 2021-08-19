/*
 *   Title: Climb Stairs
 *   Leetcode Link: https://leetcode.com/problems/climbing-stairs/
 *
 *   Problem: Given a staircase with n steps, determine the number of different
 *   ways you can climb to the top. You can step up 1 or 2 steps at a time.
 *
 *   Input:
 *      int n   => Total number of steps
 *   Output:
 *      int     -> Total number of unique ways to climb the stairs
 *
 *   Execution: javac ClimbStairs.java && java -ea ClimbStairs
 */

public class ClimbStairs {

    /*
     * Solution #1: Brute force recursive
     *
     * Recursively expand every possible combination of steps. At each step, we
     * can either step up one step or two. Recursively try both possibilites to
     * count the different options.
     *
     * Time Complexity: O(2^n)
     * Space Complexity: O(n)
     */
    public static int climbStairsBF(int n) {
        // Base case. n is the number of steps remaining to the top. If n == 0,
        // then we are at the top of the stairs, so there is exactly 1 way to
        // get to the top of the stairs (aka do nothing)
        if (n == 0) return 1;

        // Base case. If n < 0 then we found an invalid path, so there are no
        // ways to get to the top of the stairs
        if (n < 0) return 0;

        // If we take a single step, how many combinations are there to get the
        // rest of the way to the top?
        int oneStep = climbStairsBF(n-1);

        // If we take 2 steps, how many combinations are there?
        int twoSteps = climbStairsBF(n-2);

        // We can take one step or two so all of these are unique valid paths
        return oneStep + twoSteps;
    }

    /*
     * Solution #2: Top-down DP
     *
     * We can take the brute force solution and cache the values that have
     * been computed to avoid solving the same subproblem multiple times
     *
     * Time Complexity: O(n)
     * Space Complexity: O(n)
     */
    public static int climbStairsTD(int n) {
        // Initialize dp array to size n+1. We need to be able to store dp[n] so
        // we need to ensure the array is big enough
        int[] dp = new int[n + 1];

        return climbStairsTD(n, dp);
    }
    private static int climbStairsTD(int n, int[] dp) {
        // Base case. n is the number of steps remaining to the top. If n == 0,
        // then we are at the top of the stairs, so there is exactly 1 way to
        // get to the top of the stairs (aka do nothing)
        if (n == 0) return 1;

        // Base case. If n < 0 then we found an invalid path, so there are no
        // ways to get to the top of the stairs
        if (n < 0) return 0;

        // Check whether we've already computed the value. If not, we need to
        // compute it
        if (dp[n] == 0) {
            // Compute the result and add it to dp array
            dp[n] = climbStairsTD(n-1, dp) + climbStairsTD(n-2, dp);
        }

        // Now that we've computed and saved the value if necessary, return it
        return dp[n];
    }

    /*
     * Solution #3: Bottom-up DP
     *
     * This is basically the opposite of the top-down approach. Rather than
     * recursively solving smaller and smaller subproblems, we start with the
     * smallest subproblems and iteratively solve bigger and bigger subproblems
     *
     * Time Complexity: O(n)
     * Space Complexity: O(n)
     */
    public static int climbStairsBU(int n) {
        if (n == 1) return 1;

        // Construct our dp array. We ultimately want to solve for and return
        // dp[n], so the length must be n+1
        int[] dp = new int[n + 1];

        // Our base cases. We do both 0 and 1 so we don't have to worry about
        // bounds checking when referencing dp[i-1] and dp[i-2]
        dp[0] = 1;
        dp[1] = 1;

        for (int i = 2; i < dp.length; i++) {
            // We've already solved the smaller subproblems. This is the same as
            // making our recursive calls in the recursive solutions
            dp[i] = dp[i - 1] + dp[i - 2];
        }

        return dp[n];
    }

    public static void main(String[] args) {
        assert climbStairsBF(5) == 8;
        assert climbStairsTD(5) == 8;
        assert climbStairsBU(5) == 8;

        // ADD YOUR TEST CASES HERE
        System.out.println("Passed all test cases");
    }
}
