/*
 *   Title: Hamming Weight
 *   Leetcode Link: https://leetcode.com/problems/number-of-1-bits/
 *
 *   Problem: Write a function that takes an unsigned integer and return the
 *   number of '1' bits it has (also known as the Hamming weight).
 *
 *   Input:
 *      int n       => Unsigned integer
 *   Output:
 *      int         => Number of 1 bits in n
 *
 *   Execution: javac HammingWeight.java && java -ea HammingWeight
 */

public class HammingWeight {

    /*
     * Solution #1: Brute force solution using bit shifting
     *
     * Continually shift bits right and check whether the lowest order bit is 1
     *
     * Time Complexity: O(log(n))
     * Space Complexity: O(1)
     */
    public static int hammingWeightBF(int n) {
        int sum = 0;
        while (n > 0) {
            // Check if the lowest-order bit is 1
            if ((n & 1) > 0) sum++;

            // Do an unsigned bitshift
            n >>>= 1;
        }
        return sum;
    }

    /*
     * Solution #2: Optimized solution
     *
     * n & n-1 removes the lowest-order 1 bit in the number. Repeat this until
     * n == 0
     *
     * Time Complexity: O(log(n))  => More optimal when few 1 bits
     * Space Complexity: O(1)
     */
    public static int hammingWeight(int n) {
        int sum = 0;
        while (n != 0) {
            // This removes the lowest-order 1 bit
            n &= n-1;
            sum++;
        }
        return sum;
    }

    public static void main(String[] args) {
        assert hammingWeight(0b1011) == 3;
        assert hammingWeight(0b1000000) == 1;
        assert hammingWeight(0b11111111111111111111111111111101) == 31;

        // ADD TEST CASES HERE

        System.out.println("Passed all test cases");
    }

}
