"""
Title: Max rectangle

Problem:
    Given a 2D binary matrix filled with 0's and 1's, find the largest
    rectangle containing only 1's and return its area.

Execution: python max_rectangle.py
"""
import unittest


def histogram_rectangle(heights):
    if not heights:
        return 0

    stack = []
    i = 0
    maxArea = 0

    while i < len(heights):
        if not stack:
            stack.append(i)
        else:
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                l = stack[-1] if stack else -1
                width = i - l - 1
                maxArea = max(maxArea, width * h)
            stack.append(i)
        i += 1

    while stack:
        h = heights[stack.pop()]
        l = stack[-1] if stack else -1
        width = i - l - 1
        maxArea = max(maxArea, width * h)
    return maxArea


def max_rectangle(matrix):
    """
    :type matrix: List[List[str]]
    :rtype: int
    """

    if not matrix or not matrix[0]:
        return 0

    rows = len(matrix)
    cols = len(matrix[0])
    heights = [0] * cols
    maxArea = 0

    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == '1':
                heights[c] += 1
            else:
                heights[c] = 0
        area = histogram_rectangle(heights)
        maxArea = max(maxArea, area)
    return maxArea


class TestMaxRectangle(unittest.TestCase):
    """Unit test for max_rectangle."""

    def test_1(self):
        test_1_input = [
              ["1", "0", "1", "0", "0"],
              ["1", "0", "1", "1", "1"],
              ["1", "1", "1", "1", "1"],
              ["1", "0", "0", "1", "0"]
            ]
        self.assertEqual(max_rectangle(test_1_input), 6)


if __name__ == '__main__':
    unittest.main()
