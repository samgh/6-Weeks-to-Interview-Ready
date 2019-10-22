"""
Title: Merge intervals

Problem: Given a collection of intervals, merge all overlapping intervals.

Execution: python merge_intervals.py
"""
import unittest
from typing import List


def merge_intervals(intervals: List[int]):
    """Function for merging intervals."""
    intervals.sort(key=lambda interval: interval[0])
    merged = [intervals[0]]
    for current in intervals:
        previous = merged[-1]
        if current[0] <= previous[1]:
            previous[1] = max(previous[1], current[1])
        else:
            merged.append(current)
    return merged


class TestMergeIntervals(unittest.TestCase):
    """Unit test for merge intervals problem."""

    def test_1(self):
        test_input_1 = [[1,3],[2,6],[8,10],[15,18]]
        expected_output_1 = [[1,6],[8,10],[15,18]]
        self.assertEqual(merge_intervals(test_input_1), expected_output_1)
        print("Explanation:")
        print("Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].")

    def test_2(self):
        test_input_2 = [[1,4],[4,5]]
        expected_output_2 = [[1,5]]
        self.assertEqual(merge_intervals(test_input_2), expected_output_2)
        print("Explanation:")
        print("Intervals [1,4] and [4,5] are considered overlapping.")


if __name__ == '__main__':
    unittest.main()
