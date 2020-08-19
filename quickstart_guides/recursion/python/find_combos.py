"""
Title: Find all combinations of a set of inputs

Problem:
    Given an array of size n, generate and print all possible combinations of r
    elements in array. For example, if input array is {1, 2, 3, 4} and r is 2,
    then output should be {1, 2}, {1, 3}, {1, 4}, {2, 3}, {2, 4} and {3, 4}.

Execution: python find_combos.py
"""
from typing import List


def print_combos(arr: List[int], n: int, r: int):
    """Print combinations."""
    data = [0] * r
    return find_combos(arr, n, r, 0, data, 0)


def find_combos(arr: List[int], n: int, r: int, index: int, data: List[int], i: int):
    if index == r:
        x = []
        for j in range(r):
            x.append(data[j])
        print(x)
        return

    # When no more elements are there to put in data[].
    if i >= n:
        return

    # current is included, put
    # next at next location
    data[index] = arr[i]
    find_combos(arr, n, r, index + 1, data, i + 1)

    # current is excluded, replace it
    # with next (Note that i+1 is passed,
    # but index is not changed)
    find_combos(arr, n, r, index, data, i + 1)


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    r = 3
    n = len(arr)
    print_combos(arr, n, r)
