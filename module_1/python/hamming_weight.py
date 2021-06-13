"""
Title: Hamming Weight
Leetcode Link: https://leetcode.com/problems/number-of-1-bits/

Problem: Write a function that takes an unsigned integer and return the
number of '1' bits it has (also known as the Hamming weight).

Input:
    int n   => Unsigned integer
Output:
    int     => Number of 1 bits in n

Execution: python hamming_weight.py
"""
import unittest

"""
Solution #1: Brute force solution using bit shifting

Continually shift bits right and check whether the lowest order bit is 1

Time Complexity: O(log(n))
Space Complexity: O(1)
"""
def hamming_weight_bf(n: int) -> int:
    sum = 0
    while n > 0:
        # Check if lowest order bit is 1
        if (n & 1) > 0:
            sum = sum+1

        # Do a bitshift
        n = n>>1

    return sum

"""
Solution #2: Optimized solution

n & n-1 removes the lowest-order 1 bit in the number. Repeat this until
n == 0

Time Complexity: O(log(n))  => More optimal when few 1 bits
Space Complexity: O(1)
"""
def hamming_weight(n: int) -> int:
    sum = 0
    while n != 0:
        # This removes the lowest-order 1 bit
        n &= (n - 1)
        sum = sum+1

    return sum

class TestHammingWeight(unittest.TestCase):
    """Unit test for Hamming weight."""

    def test_1(self):
        self.assertEqual(hamming_weight(int("0b1011", 2)), 3)

    def test_2(self):
        self.assertEqual(hamming_weight(int("0b100000", 2)), 1)

    def test_3(self):
        self.assertEqual(hamming_weight(int("0b11111111111111111111111111111101", 2)), 31)

    # ADD YOUR TESTS HERE

if __name__ == '__main__':
    unittest.main()
