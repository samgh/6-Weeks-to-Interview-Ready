"""
Title: Quick sort

Problem:
    Implement quick sort algorithm.

Execution: python quick_sort.py
"""
from typing import List
import unittest


def partition(arr: List[int], low: int, high: int) -> int:
    idx = low - 1  # index of smaller element
    pivot = arr[high]  # pivot

    for j in range(low, high):
        # If current element is smaller than the pivot
        if arr[j] < pivot:
            # increment index of smaller element
            idx = idx + 1
            arr[idx], arr[j] = arr[j], arr[idx]

    arr[idx + 1], arr[high] = arr[high], arr[idx + 1]
    return idx + 1


def quick_sort(arr: List[int], low: int, high: int) -> None:
    if low < high:
        # pi is partitioning index, arr[p] is now at right place.
        pi = partition(arr, low, high)

        # Separately sort elements before partition and after partition.
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


class TestQuickSort(unittest.TestCase):
    def test_quick_sort(self):
        arr = [10, 7, 8, 9, 1, 5]
        n = len(arr)
        quick_sort(arr, 0, n - 1)

        result = []
        for i in range(n):
            result.append(arr[i])

        self.assertEqual(result, [1, 5, 7, 8, 9, 10])


if __name__ == "__main__":
    unittest.main()
