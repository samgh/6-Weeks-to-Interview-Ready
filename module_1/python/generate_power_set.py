"""
Title: Subsets
Leetcode Link: https://leetcode.com/problems/subsets/

Problem: Given a set of distinct integers, nums, return all possible
subsets (the power set).
Note: The solution set must not contain duplicate subsets.

Input:
    List[int] nums  => List of numbers
Output:
    List[List[int]] => All subsets of nums

Execution: python generate_power_set.py
"""
import unittest
from typing import List
import copy

"""
Solution #1: Recurisve using a passed list

For each element in the array there are two options: Either it is included in
given subset or not. Recursively we will generate every possible combination

Time Complexity: O(2^n)
Space Complexity: O(n)
"""
def generate_power_set_passed_var(nums: List[int]) -> List[List[int]]:
    results = []
    generate_power_set_passed_var_inner(nums, results, 0, [])
    return results

"""
Inner function

Input:
    List[int] nums          => List of numbers
    List[List[int] results  => All results get stored here
    int i                   => Current index. Find all powersets from
                               here to the end
    List[int] curr_result    => Current powerset from index 0-(i-1)

"""
def generate_power_set_passed_var_inner(nums: List[int], results: List[List[int]], i: int, curr_result: List[int]):
    # Base case. At the end of the array
    if i == len(nums):
        results.append(copy.deepcopy(curr_result))
        return

    # Find all combinations excluding nums[i]
    generate_power_set_passed_var_inner(nums, results, i+1, curr_result)

    # Find all combinations including nums[i]
    curr_result.append(nums[i])
    generate_power_set_passed_var_inner(nums, results, i+1, curr_result)

    # Backtracking
    curr_result.pop()

"""
Solution #1: Recurisve building up result as we return (used for DP)

We find all combinations from index i+1 to the end of the list. Then each
those combos can either include or exclude nums[i].et or not. Recursively we will generate every possible combination

Time Complexity: O(2^n)
Space Complexity: O(n)
"""
def generate_power_set_built_up(nums: List[int], i: int = 0) -> List[List[int]]:
    # Base case. If i == nums.length, we are computing powerset of [] which is [[]]
    if i == len(nums):
        return [[]]

    # Recursiv  ely compute all combinations from i+1 to end of array
    results = generate_power_set_built_up(nums, i+1)

    # We need to add nums[i] into results. Each result in results can either
    # include or exclude nums[i]
    updated_results = []
    for result in results:
        # Copy result as-is
        updated_results.append(copy.deepcopy(result))

        # Prepend nums[i] and make another copy
        result.insert(0, nums[i])
        updated_results.append(copy.deepcopy(result))

    return updated_results

"""
Solution #3: Iterative approach

This is basically the inverse of Solution #2. We repeatedly copy and
expand our list of results until we go through all the values.

Time Complexity: O(2^n)
Space Complexity: O(n)
"""
def generate_power_set_iter(nums: List[int]) -> List[List[int]]:
    # We start with the powerset of [] and then add in additional values
    results = [[]]

    # Each time we add a value, all the existing subsets still exist.
    # We could also have every existing subset including the current value
    for num in nums:
        new_results = []
        for result in results:
            # Copy the subset as-is
            new_results.append(copy.deepcopy(result))

            # Add nums[i] to result and make another copy
            result.append(num)
            new_results.append(copy.deepcopy(result))

        results = new_results

    return results

class TestGeneratePowerSet(unittest.TestCase):
    """Unit test for generate power set."""

    def test_1(self):
        """Test for generate power set."""
        expected_output = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
        # Note the order of the output matters here
        self.assertEqual(generate_power_set_built_up([1,2,3]), expected_output)

    # ADD YOUR TESTS HERE

if __name__ == '__main__':
    print(generate_power_set_built_up([1,2,3]))
    print(generate_power_set_iter([1,2,3]))
    print(generate_power_set_passed_var([1,2,3]))
    unittest.main()
