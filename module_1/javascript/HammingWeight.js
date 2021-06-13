/*
 *   Title: Hamming Weight
 *   Leetcode Link: https://leetcode.com/problems/number-of-1-bits/
 *
 *   Problem: Write a function that takes an unsigned integer and return the
 *   number of '1' bits it has (also known as the Hamming weight).
 *
 *   Input:
 *      number n       => Unsigned integer
 *   Output:
 *      number         => Number of 1 bits in n
 *
 *   Execution: node HammingWeight.js
 */

/**
 * Solution #1: Brute force solution using bit shifting
 *
 * Continually shift bits right and check whether the lowest order bit is 1
 *
 * Time Complexity: O(log(n))
 * Space Complexity: O(1)
 *
 * @param {number} n
 * @return {number}
 */
var hammingWeightBF = function(n) {
     var sum = 0;
     while (n > 0) {
        // Check if the lowest-order bit is 1
        if ((n & 1) > 0) sum++;

        // Do an unsigned bitshift
        n >>>= 1;
    }
    return sum;
}

/**
 * Solution #2: Optimized solution
 *
 * n & n-1 removes the lowest-order 1 bit in the number. Repeat this until
 * n == 0
 *
 * Time Complexity: O(log(n))  => More optimal when few 1 bits
 * Space Complexity: O(1)
 *
 * @param {number} n
 * @return {number}
 */
var hammingWeight = function(n) {
    var sum = 0;
    while (n != 0) {
        // This removes the lowest-order 1 bit
        n &= n-1;
        sum++;
    }
    return sum;
}

var tester = function() {
    console.assert(hammingWeight(0b1011) == 3);
    console.assert(hammingWeight(0b100000) == 1);
    console.assert(hammingWeight(0b11111111111111111111111111111101) == 31);

    // ADD YOUR OWN TESTS HERE
}

tester();
