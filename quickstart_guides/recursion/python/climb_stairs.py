"""
Title: Climb stairs

Problem:
    You are climbing a stair case. It takes n steps to reach to the top.

    Each time you can either climb 1 or 2 steps. In how many distinct ways
    can you climb to the top?

    Note: Given n will be a positive integer.

Execution: python climb_stairs.py
"""
import unittest


class ClimbStairsBruteForce:
    """Brute-force implementation of climb stairs problem."""

    def climb_stairs(self, n: int) -> int:
        """Call recursive helper for climb stairs."""
        return self.climb_stairs_recur(0, n)

    def climb_stairs_recur(self, i: int, n: int) -> int:
        """Climb stairs recursive helper."""
        if i > n:
            return 0
        if i == n:
            return 1
        return self.climb_stairs_recur(i + 1, n) + self.climb_stairs_recur(i + 2, n)


class ClimbStairsDP:
    """Dynamic programming implementation of climb stairs problem."""

    def climb_stairs(self, n: int) -> int:
        if n == 1:
            return 1

        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]


class TestClimbStairs(unittest.TestCase):
    """Unit test for climb stairs function."""

    def test_1(self):
        bf = ClimbStairsBruteForce()
        dp = ClimbStairsDP()

        self.assertEqual(bf.climb_stairs(2), 2)
        self.assertEqual(dp.climb_stairs(2), 2)

        print("Explanation: There are two ways to climb to the top:")
        print("1. 1 step + 1 step.")
        print("2. 2 steps")

    def test_2(self):
        bf = ClimbStairsBruteForce()
        dp = ClimbStairsDP()

        self.assertEqual(bf.climb_stairs(3), 3)
        self.assertEqual(dp.climb_stairs(3), 3)

        print("Explanation: There are three ways to climb to the top.")
        print("1. 1 step + 1 step + 1 step.")
        print("2. 1 step + 2 steps.")
        print("3. 2 steps + 1 step.")


if __name__ == "__main__":
    unittest.main()
