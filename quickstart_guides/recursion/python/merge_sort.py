"""
Title: Merge sort.

Problem:
    Merge sort is a divide-and-conquer algorithm based on the idea of breaking
    down a list into several sub-lists until each sublist consists of a single
    element and merging those sublists in a manner that results into a sorted
    list.

Execution: python merge_sort.py
"""
from typing import Any, List
import unittest


def merge_sort(data: List[Any]):
    """Perform merge sort recursively on list."""
    if len(data) > 1:
        mid = len(data) // 2
        left = data[:mid]
        right = data[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                data[k] = left[i]
                i += 1
            else:
                data[k] = right[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(left):
            data[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            data[k] = right[j]
            j += 1
            k += 1


class TestMergeSort(unittest.TestCase):
    """Unit tests for merge_sort."""

    def test_1(self):
        data = [12, 11, 13, 5, 6, 7]
        expected_out = [5, 6, 7, 11, 12, 13]
        merge_sort(data)
        self.assertEqual(data, expected_out)


if __name__ == "__main__":
    unittest.main()
