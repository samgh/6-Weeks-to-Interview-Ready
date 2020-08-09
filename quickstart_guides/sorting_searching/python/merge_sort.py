"""
Title: Merge sort

Problem:
    Implement merge sort.

Execution: python merge_sort.py
"""
from typing import List
import unittest


def merge_sort(arr: List[int]) -> None:
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


class TestMergeSort(unittest.TestCase):
    """Unit test for MergeSort."""

    def test_1(self):
        input_arr = [12, 11, 13, 5, 6, 7]
        expected_arr = [5, 6, 7, 11, 12, 13]
        merge_sort(input_arr)
        self.assertEqual(expected_arr, input_arr)

    def test_2(self):
        input_arr = [34, 2, 32, 33]
        expected_arr = [2, 32, 33, 34]
        merge_sort(input_arr)
        self.assertEqual(expected_arr, input_arr)


if __name__ == "__main__":
    unittest.main()
