"""
Title: Contain with Most Water

Problem:
    Given n non-negative integers a1, a2, ..., an , where each represents a
    point at coordinate (i, ai). n vertical lines are drawn such that the two
    endpoints of line i is at (i, ai) and (i, 0). Find two lines, which
    together with x-axis forms a container, such that the container contains
    the most water.

    Note: You may not slant the container and n is at least 2.

Execution: python max_area.py
"""
import unittest
from typing import List


def max_area(height: List[int]):
    max_area = 0
    for i in range(len(height)):
        for j in range(i+1, len(height)):
            max_area = max(max_area, min(height[i], height[j]) * (j - i))
    return max_area


class TestMaxArea(unittest.TestCase):
    """Unit test for max_area."""

    def test_1(self):
        test_input = [1, 8, 6, 2, 5, 4, 8, 3, 7]
        self.assertEqual(max_area(test_input), 49)


if __name__ == '__main__':
    unittest.main()

