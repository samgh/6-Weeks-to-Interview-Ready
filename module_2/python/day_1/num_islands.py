"""
Title: Number of islands.

Problem: Given a 2d grid map of '1's (land) and '0's (water), count the number
of islands. An island is surrounded by water and is formed by connecting
adjacent lands horizontally or vertically. You may assume all four edges of the
grid are all surrounded by water.

Execution: python num_islands.py
"""
import unittest
from typing import List


class Grid:
    def __init__(self, grid):
        self.grid = grid
        self.num_rows = len(grid)
        self.num_cols = len(grid[0])

    def is_valid(self, i, j, visited):
        return (i >= 0 and i < self.num_rows and
                j >= 0 and j < self.num_cols and
                not visited[i][j] and self.grid[i][j])

    def dfs(self, i, j, visited):

        # These lists are used to get row and
        # column numbers of 8 neighbors of a given cell.
        row_dir = [-1, -1, -1, 0, 0, 1, 1, 1]
        col_dir = [-1, 0, 1, -1, 1, -1, 0, 1]

        visited[i][j] = True

        for k in range(8):
            if self.is_valid(i + row_dir[k], j + col_dir[k], visited):
                self.dfs(i + row_dir[k], j + col_dir[k], visited)

    def num_islands(self):
        visited = [[False for j in range(self.num_cols)] for i in range(self.num_rows)]

        count = 0
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                if visited[i][j] is False and self.grid[i][j] == 1:
                    self.dfs(i, j, visited)
                    count += 1
        return count




class TestNumIslands(unittest.TestCase):
    """Unit test for Number of Islands."""

    def test_1(self):
        test_1_input = [
            [1, 1, 1, 1, 0],
            [1, 1, 0, 1, 0],
            [1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]
        g = Grid(test_1_input)
        self.assertEqual(g.num_islands(), 1)

    def test_2(self):
        test_2_input = [
            ["1", "1", "0", "0", "0"],
            ["0", "1", "0", "0", "1"],
            ["1", "0", "0", "1", "1"],
            ["0", "0", "0", "0", "0"],
            ["1", "0", "1", "0", "1"]
        ]
        g = Grid(test_2_input)
        self.assertEqual(g.num_islands(), 1)


if __name__ == '__main__':
    unittest.main()
