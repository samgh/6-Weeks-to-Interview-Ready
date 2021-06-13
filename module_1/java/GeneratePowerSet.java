/*
 *   Title: Subsets
 *   Leetcode Link: https://leetcode.com/problems/subsets/
 *
 *   Problem: Given a set of distinct integers, nums, return all possible
 *   subsets (the power set).
 *   Note: The solution set must not contain duplicate subsets.
 *
 *   Input:
 *      int[] nums              => List of numbers
 *   Output:
 *      List<List<Integer>>     => All subsets of nums
 *
 *   Execution: javac GeneratePowerSet.java && java -ea GeneratePowerSet
 */

import java.util.*;

public class GeneratePowerSet {

    /*
     * Solution #1: Recurisve using a passed list
     *
     * For each element in the array there are two options: Either it is included in
     * given subset or not. Recursively we will generate every possible combination
     *
     * Time Complexity: O(2^n)
     * Space Complexity: O(n)
     */
    public static List<List<Integer>> generatePowerSetPassedVar(int[] nums) {
        List<List<Integer>> results = new ArrayList<>();
        generatePowerSetPassedVar(nums, 0, new ArrayList<Integer>(), results);
        return results;
    }

    /*
     * Inner function
     *
     * Input:
     *    int[] nums                    => List of numbers
     *    int i                         => Current index. Find all powersets from
     *                                     here to the end
     *    List<Integer> currResult      => Current powerset from index 0-(i-1)
     *    List<List<Integer> results    => All results get stored here
     */
    private static void generatePowerSetPassedVar(int[] nums, int i, List<Integer> currResult, List<List<Integer>> results) {
        // Base case. At the end of the array
        if (i == nums.length) {
            // Make a copy of the current result into results
            results.add(new ArrayList<Integer>(currResult));
            return;
        }

        // Find all combinations excluding nums[i]
        generatePowerSetPassedVar(nums, i+1, currResult, results);

        // Find all combinations including nums[i]
        currResult.add(nums[i]);
        generatePowerSetPassedVar(nums, i+1, currResult, results);

        // Backtracking
        currResult.remove(currResult.size()-1);
    }

    /*
     * Solution #2: Recurisve building up result as we return (used for DP)
     *
     * We find all combinations from index i+1 to the end of the list. Then each
     * those combos can either include or exclude nums[i].
     *
     * Time Complexity: O(2^n)
     * Space Complexity: O(n)
     */
    public static List<List<Integer>> generatePowerSetBuiltUp(int[] nums) {
        return generatePowerSetBuiltUp(nums, 0);
    }

    /*
     * Inner function
     *
     * Input:
     *    int[] nums   => List of numbers
     *    int i        => Current index. Find all powersets from here to the end
     */
    private static List<List<Integer>> generatePowerSetBuiltUp(int[] nums, int i) {
        // Base case. If i == nums.length, we are computing powerset of [] which
        // is [[]]
        if (i == nums.length) {
            List<List<Integer>> result = new ArrayList<>();
            result.add(new ArrayList<Integer>());
            return result;
        }

        // Recursively compute all combinations from i+1 to end of array
        List<List<Integer>> results = generatePowerSetBuiltUp(nums, i+1);

        // We need to add nums[i] into results. Each result in results can either
        // include or exclude nums[i]
        List<List<Integer>> updatedResults = new ArrayList<>();
        for (List<Integer> result : results) {
            // Copy result as-is
            updatedResults.add(new ArrayList<Integer>(result));

            // Prepend nums[i] and make another copy
            result.add(0, nums[i]);
            updatedResults.add(new ArrayList<Integer>(result));
        }

        return updatedResults;
    }

    /*
     * Solution #3: Iterative approach
     *
     * This is basically the inverse of Solution #2. We repeatedly copy and
     * expand our list of results until we go through all the values.
     *
     * Time Complexity: O(2^n)
     * Space Complexity: O(n)
     */
     public static List<List<Integer>> generatePowerSetIter(int[] nums) {
         List<List<Integer>> results = new ArrayList<>();

         // We start with the powerset of [] and then add in additional values
         results.add(new ArrayList<Integer>());

         // Each time we add a value, all the existing subsets still exist.
         // We could also have every existing subset including the current value
         for (int num : nums) {
             List<List<Integer>> newResults = new ArrayList<>();
             for (List<Integer> result : results) {
                 // Copy the subset as is
                 newResults.add(new ArrayList<Integer>(result));

                 // Add nums[i] to result and make another copy
                 result.add(num);
                 newResults.add(new ArrayList<Integer>(result));
             }
             results = newResults;
         }

         return results;
     }

     // Test cases
     public static void main(String[] args) {
        System.out.println(generatePowerSetBuiltUp(new int[]{1,2,3}));

        // ADD YOUR TESTS HERE

        System.out.println("Passed all test cases");
    }

}
