"""
Title: Breadth-first search

Problem:
    Breadth First Traversal (or Search) for a graph is similar to Breadth First
    Traversal of a tree. The only catch here is, unlike trees, graphs may
    contain cycles, so we may come to the same node again.

    To avoid processing a node more than once, we use a boolean visited array.
    For simplicity, it is assumed that all vertices are reachable from the
    starting vertex.

Execution: python bfs.py
"""
from typing import List
import unittest
from collections import defaultdict


class BFS:
    """
    This class represents a directed graph by making use of the adjacency
    list representation.
    """

    def __init__(self) -> None:
        self.graph = defaultdict(list)

    def add_edge(self, u: int, v: int) -> None:
        """Add edge in graph."""
        self.graph[u].append(v)

    def bfs(self, s: int) -> List[int]:
        """Perform breadth first search."""
        result = []

        # Mark all the vertices as not visited.
        visited = [False] * (len(self.graph))

        # Create a queue for BFS
        queue = list()

        # Mark the source node as visited and enqueue it.
        queue.append(s)
        visited[s] = True

        while queue:

            # Dequeue a vertex from queue and print it.
            s = queue.pop(0)
            result.append(s)

            # Get all adjacent vertices of the dequeued vertex s. If a adjacent
            # has not been visited, then mark it visited and enqueue it
            for i in self.graph[s]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True
        return result


class TestBFS(unittest.TestCase):
    """Unit tests for bfs."""

    def test_1(self):
        g = BFS()
        g.add_edge(0, 1)
        g.add_edge(0, 2)
        g.add_edge(1, 2)
        g.add_edge(2, 0)
        g.add_edge(2, 3)
        g.add_edge(3, 3)

        self.assertEqual(g.bfs(2), [2, 0, 3, 1])

        self.assertEqual(g.bfs(3), [3])

        self.assertEqual(g.bfs(1), [1, 2, 0, 3])


if __name__ == "__main__":
    unittest.main()
