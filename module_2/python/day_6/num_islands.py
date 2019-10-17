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


class Graph:
    def __init__(self, row: int, col: int, graph: List[List[int]]):
        self._row = row
        self._col = col
        self._graph = graph

    # A function to check if a given cell
    # (row, col) can be included in DFS
    def isSafe(self, i: int, j: int, visited: List[List[int]]):
        # row number is in range, column number
        # is in range and value is
        # and not yet visited
        return (i >= 0 and i < self._row and
                j >= 0 and j < self._col and
                not visited[i][j] and self._graph[i][j])

    # A utility function to do DFS for a 2D
    # boolean matrix. It only considers
    # the 8 neighbours as adjacent vertices
    def DFS(self, i, j, visited: List[List[int]]):
        """Depth first search implementation"""
        # These arrays are used to get row and
        # column numbers of 8 neighbours
        # of a given cell
        rowNbr = [-1, -1, -1,  0, 0,  1, 1, 1]
        colNbr = [-1,  0,  1, -1, 1, -1, 0, 1]
          
        # Mark this cell as visited
        visited[i][j] = True
  
        # Recur for all connected neighbours
        for k in range(8):
            if self.isSafe(i + rowNbr[k], j + colNbr[k], visited):
                self.DFS(i + rowNbr[k], j + colNbr[k], visited)

    # The main function that returns
    # count of islands in a given boolean
    # 2D matrix 
    def countIslands(self):
        # Make a bool array to mark visited cells. 
        # Initially all cells are unvisited 
        visited = [[False for j in range(self._col)]for i in range(self._row)]

        # Initialize count as 0 and travese
        # through the all cells of
        # given matrix
        count = 0
        for i in range(self._row):
            for j in range(self._col):
                # If a cell with value 1 is not visited yet,
                # then new island found
                if visited[i][j] is False and self._graph[i][j] == 1:
                    # Visit all cells in this island
                    # and increment island count
                    self.DFS(i, j, visited)
                    count += 1
        return count


class TestNumIslands(unittest.TestCase):
    """Unit test for Number of Islands."""

    def test_1(self):
        graph = [[1, 1, 0, 0, 0],
                 [0, 1, 0, 0, 1],
                 [1, 0, 0, 1, 1],
                 [0, 0, 0, 0, 0],
                 [1, 0, 1, 0, 1]]

        row = len(graph)
        col = len(graph[0])
        g = Graph(row, col, graph)
        self.assertEqual(g.countIslands(), 5)


if __name__ == '__main__':
    unittest.main()
