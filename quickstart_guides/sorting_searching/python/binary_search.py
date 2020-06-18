"""
Title: Binary search

    Binary search is a search algorithm that finds the position of a target
    value within a sorted array. Binary search compares the target value to the
    middle element of the array.

    If they are not equal, the half in which the target cannot lie is
    eliminated and the search continues on the remaining half, again taking the
    middle element to compare to the target value, and repeating this until the
    target value is found. If the search ends with the remaining half being
    empty, the target is not in the array.

Execution: python binary_search.py
"""
from typing import List


def binary_search_iterative(data: List[int], target: int) -> bool:
    """Iterative binary search."""
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False


def binary_search_recursive(data: List[int], target: int, low: int, high: int) -> bool:
    """Recursive binary search."""
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_search_recursive(data, target, low, mid-1)
        else:
            return binary_search_recursive(data, target, mid+1, high)


input_data = [2, 4, 5, 7, 8, 9, 12, 14, 17, 19, 22, 25, 27, 28, 33, 37]
input_target = 37

print(binary_search_recursive(input_data, input_target, 0, len(input_data)-1))
print(binary_search_iterative(input_data, input_target))
