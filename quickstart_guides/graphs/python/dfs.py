"""
Title: Depth-first search

Problem:
    Depth First Traversal (or Search) for a graph is similar to Depth First
    Traversal of a tree. The only catch here is, unlike trees, graphs may
    contain cycles, a node may be visited twice. To avoid processing a node more
    than once, use a boolean visited array.

Execution: python dfs.py
"""
from typing import List
import unittest
from collections import defaultdict


class DFS:
    """Depth-first search class."""

    def __init__(self):
        self.graph = defaultdict(list)
        self.result = []

    def add_edge(self, u: int, v: int) -> None:
        """Add edge to graph."""
        self.graph[u].append(v)

    def dfs_helper(self, v: int, visited: List[int]) -> None:
        """Recursive helper for depth-first search method."""
        # Mark the current node as visited and print it.
        visited[v] = True
        self.result.append(v)

        # Recur for all the vertices adjacent to this vertex.
        for i in self.graph[v]:
            if not visited[i]:
                self.dfs_helper(i, visited)

    def dfs(self, v: int) -> List[int]:
        # Mark all the vertices as not visited.
        visited = [False] * (max(self.graph) + 1)

        self.dfs_helper(v, visited)
        return self.result


class TestDFS(unittest.TestCase):
    """Unit tests for dfs."""

    def test_1(self):
        g = DFS()
        g.add_edge(0, 1)
        g.add_edge(0, 2)
        g.add_edge(1, 2)
        g.add_edge(2, 0)
        g.add_edge(2, 3)
        g.add_edge(3, 3)
        self.assertEqual(g.dfs(2), [2, 0, 1, 3])

        g = DFS()
        g.add_edge(0, 1)
        g.add_edge(0, 2)
        g.add_edge(1, 2)
        g.add_edge(2, 0)
        g.add_edge(2, 3)
        g.add_edge(3, 3)
        self.assertEqual(g.dfs(3), [3])

        g = DFS()
        g.add_edge(0, 1)
        g.add_edge(0, 2)
        g.add_edge(1, 2)
        g.add_edge(2, 0)
        g.add_edge(2, 3)
        g.add_edge(3, 3)
        self.assertEqual(g.dfs(1), [1, 2, 0, 3])


if __name__ == "__main__":
    unittest.main()
