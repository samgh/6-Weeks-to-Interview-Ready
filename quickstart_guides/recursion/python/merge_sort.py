"""
Title: Merge sort.

    Merge sort is a divide-and-conquer algorithm based on the idea of breaking
    down a list into several sub-lists until each sublist consists of a single
    element and merging those sublists in a manner that results into a sorted
    list.

Execution: python merge_sort.py
"""
from typing import Any, List
import unittest


def merge_sort(data: List[Any]):
    if len(data) > 1:
        mid = len(data) // 2
        L = data[:mid]
        R = data[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                data[k] = L[i]
                i += 1
            else:
                data[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            data[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            data[k] = R[j]
            j += 1
            k += 1


class TestMergeSort(unittest.TestCase):
    """Unit tests for merge_sort."""

    def test_1(self):
        data = [12, 11, 13, 5, 6, 7]  
        expected_out = [5, 6, 7, 11, 12, 13]
        merge_sort(data)
        self.assertEqual(data, expected_out)


if __name__ == '__main__':
    unittest.main()
