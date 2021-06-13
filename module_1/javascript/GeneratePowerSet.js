/**
 *   Title: Subsets
 *   Leetcode Link: https://leetcode.com/problems/subsets/
 *
 *   Problem: Given a set of distinct integers, nums, return all possible
 *   subsets (the power set).
 *   Note: The solution set must not contain duplicate subsets.
 *
 *   Input:
 *      number[] nums   => List of numbers
 *   Output:
 *      number[][]      => All subsets of nums
 *
 *   Execution: node generatePowerSet.js
 */

/**
 * Solution #1: Recurisve using a passed list
 *
 * For each element in the array there are two options: Either it is included in
 * given subset or not. Recursively we will generate every possible combination
 *
 * Time Complexity: O(2^n)
 * Space Complexity: O(n)
 *
 * @param {number[]} nums
 * @return {number[][]}
 */
var generatePowerSetPassedVar = function(nums) {
    var results = [];
    generatePowerSetPassedVarInner(nums, 0, [], results);
    return results;
}

/**
 * Inner function
 *
 * @param {number[]} nums       => List of numbers
 * @param {number} i            => Current index. Find all powersets from here to the end
 * @param {number[]} currResult => Current powerset from index 0-(i-1)
 * @param {number[][]} results  => All results get stored here
 */
var generatePowerSetPassedVarInner = function(nums, i, currResult, results) {
    // Base case. At the end of the array
    if (i == nums.length) {
        // Make a copy of the current result into results
        results.push(JSON.parse(JSON.stringify(currResult)));
        return;
    }

    // Find all combinations excluding nums[i]
    generatePowerSetPassedVarInner(nums, i+1, currResult, results);

    // Find all combinations including nums[i]
    currResult.push(nums[i]);
    generatePowerSetPassedVarInner(nums, i+1, currResult, results);

    // Backtracking
    currResult.pop();
}

/**
 * Solution #2: Recurisve building up result as we return (used for DP)
 *
 * We find all combinations from index i+1 to the end of the list. Then each
 * those combos can either include or exclude nums[i].
 *
 * Time Complexity: O(2^n)
 * Space Complexity: O(n)
 *
 * @param {number[]} nums
 * @return {number[][]}
 */
var generatePowerSetBuiltUp = function(nums){
    return generatePowerSetBuiltUpInner(nums, 0);
}

/**
 * Inner function
 *
 * @param {number[]} nums   => List of numbers
 * @param {number} i        => Current index. Find all powersets from here to the end
 * @return {number[][]}
 */
var generatePowerSetBuiltUpInner = function(nums, i) {
    // Base case. If i == nums.length, we are computing powerset of [] which
    // is [[]]
    if (i == nums.length) return [[]];

    // Recursively compute all combinations from i+1 to end of array
    var results = generatePowerSetBuiltUpInner(nums, i+1);

    // We need to add nums[i] into results. Each result in results can either
    // include or exclude nums[i]
    var updatedResults = [];
    results.forEach(function(result){
        // Copy result as-is
        updatedResults.push(JSON.parse(JSON.stringify(result)));

        // Prepend nums[i] and make another copy
        result.unshift(nums[i]);
        updatedResults.push(JSON.parse(JSON.stringify(result)));
    });

    return updatedResults;
}

/**
 * Solution #3: Iterative approach
 *
 * This is basically the inverse of Solution #2. We repeatedly copy and
 * expand our list of results until we go through all the values.
 *
 * Time Complexity: O(2^n)
 * Space Complexity: O(n)
 *
 * @param {number[]} nums
 * @return {number[][]}
 */
var generatePowerSetIter = function(nums) {
    var results = [[]];

    nums.forEach(function(num){
        var newResults = [];
        results.forEach(function(result){
            // Copy the subset as is
            newResults.push(JSON.parse(JSON.stringify(result)));

            // Add nums[i] to result and make another copy
            result.push(num);
            newResults.push(JSON.parse(JSON.stringify(result)));
        });

        results = newResults;
    });

    return results;
}


var tester = function() {
    console.log(generatePowerSetBuiltUp([1,2,3]));

    // ADD YOUR OWN TESTS HERE
}

tester();
