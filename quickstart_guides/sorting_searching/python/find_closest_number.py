"""
Title: Find closest number

Problem:
    Given an array of sorted integers. We need to find the closest value to
    the given number. Array may contain duplicate values and negative numbers.

Execution: python find_closest_number.py
"""
import unittest
from typing import List, Optional


def find_closest_num(arr: List[int], target: int) -> Optional[int]:
    min_diff = float("inf")
    low = 0
    high = len(arr) - 1
    closest_num = None

    # Edge cases for empty list of list
    # with only one element:
    if len(arr) == 0:
        return None
    if len(arr) == 1:
        return arr[0]

    min_diff_right, min_diff_left = None, None
    while low <= high:
        mid = (low + high) // 2

        # Ensure you do not read beyond the bounds
        # of the list.
        if mid + 1 < len(arr):
            min_diff_right = abs(arr[mid + 1] - target)
        if mid > 0:
            min_diff_left = abs(arr[mid - 1] - target)

        # Check if the absolute value between left and right elements are
        # smaller than any seen prior.
        if min_diff_left < min_diff:
            min_diff = min_diff_left
            closest_num = arr[mid - 1]

        if min_diff_right < min_diff:
            min_diff = min_diff_right
            closest_num = arr[mid + 1]

        # Move the mid-point appropriately as is done via binary search.
        if arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
        # If the element itself is the target, the closest number to it is
        # itself. Return the number.
        else:
            return arr[mid]
    return closest_num


class TestFindClosestNumber(unittest.TestCase):
    """Unit tests for find_closest_number."""

    def test_1(self):
        input_arr = [1, 2, 4, 5, 6, 6, 8, 9]
        self.assertEqual(find_closest_num(input_arr, 4), 4)


if __name__ == "__main__":
    unittest.main()
