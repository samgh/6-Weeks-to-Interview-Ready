"""
Title: Climb Stairs
Leetcode Link: https://leetcode.com/problems/climbing-stairs/

Problem: Given a staircase with n steps, determine the number of different
ways you can climb to the top. You can step up 1 or 2 steps at a time.

Input:
    int n   => Total number of steps
Output:
    int     -> Total number of unique ways to climb the stairs

Execution: python climb_stairs.py
"""
import unittest

"""
Solution #1: Brute force recursive

Recursively expand every possible combination of steps. At each step, we
can either step up one step or two. Recursively try both possibilites to
count the different options.

Time Complexity: O(2^n)
Space Complexity: O(n)
"""
def climb_stairs_bf(n: int)->int:
    # Base case. n is the number of steps remaining to the top. If n == 0,
    # then we are at the top of the stairs, so there is exactly 1 way to
    # get to the top of the stairs (aka do nothing)
    if n == 0:
        return 1

    # Base case. If n < 0 then we found an invalid path, so there are no
    # ways to get to the top of the stairs
    if n < 0:
        return 0

    # If we take a single step, how many combinations are there to get the
    # rest of the way to the top?
    one_step = climb_stairs_bf(n-1)

    # If we take 2 steps, how many combinations are there?
    two_steps = climb_stairs_bf(n-2)

    # We can take one step or two so all of these are unique valid paths
    return one_step + two_steps

"""
Solution #2: Top-down DP

We can take the brute force solution and cache the values that have
been computed to avoid solving the same subproblem multiple times

Time Complexity: O(n)
Space Complexity: O(n)
"""
def climb_stairs_td(n: int, dp: dict={})->int:
    # Base case. n is the number of steps remaining to the top. If n == 0,
    # then we are at the top of the stairs, so there is exactly 1 way to
    # get to the top of the stairs (aka do nothing)
    if n == 0:
        return 1

    # Base case. If n < 0 then we found an invalid path, so there are no
    # ways to get to the top of the stairs
    if n < 0:
        return 0

    # Check whether we've already computed the value. If not, we need to
    # compute it
    if not n in dp:
        # Compute the result and add it to dp array
        dp[n] = climb_stairs_td(n-1, dp) + climb_stairs_td(n-2, dp);

    # Now that we've computed and saved the value if necessary, return it
    return dp[n];


"""
Solution #3: Bottom-up DP

This is basically the opposite of the top-down approach. Rather than
recursively solving smaller and smaller subproblems, we start with the
smallest subproblems and iteratively solve bigger and bigger subproblems

Time Complexity: O(n)
Space Complexity: O(n)
"""
def climb_stairs_bu(n: int)->int:
    if n == 1:
        return 1;

    # Construct our dp list. We ultimately want to solve for and return
    # dp[n], so the length must be n+1
    dp = [0]*(n+1);

    # Our base cases. We do both 0 and 1 so we don't have to worry about
    # bounds checking when referencing dp[i-1] and dp[i-2]
    dp[0] = 1;
    dp[1] = 1;

    for i in range(2, len(dp)):
        # We've already solved the smaller subproblems. This is the same as
        # making our recursive calls in the recursive solutions
        dp[i] = dp[i - 1] + dp[i - 2];

    return dp[n];

class TestClimbStairs(unittest.TestCase):
    """Unit test for climb stairs function."""

    def test_1(self):
        self.assertEqual(climb_stairs_bf(2), 2)
        self.assertEqual(climb_stairs_td(2), 2)
        self.assertEqual(climb_stairs_bu(2), 2)

    def test_2(self):
        self.assertEqual(climb_stairs_bf(5), 8)
        self.assertEqual(climb_stairs_td(5), 8)
        self.assertEqual(climb_stairs_bu(5), 8)

    # ADD YOUR TESTS HERE

if __name__ == '__main__':
    unittest.main()
