"""
Title: Is Graph Bipartite
Leetcode Link: https://leetcode.com/problems/is-graph-bipartite/

Problem: Given an undirected graph, return true if and only if it is bipartite.

Recall that a graph is bipartite if we can split it's set of nodes into two
independent subsets U and V such that every edge in the graph has one node
in U and another node in B.

The graph is given in the following form:
  graph[i] is a list of indexes j for which the edge between nodes i and j
  exists.  Each node is an integer between 0 and graph.length - 1.  There
  are no self edges or parallel edges: graph[i] doesnot contain i, and it
  doesn't contain any element twice.

Input:
  List[int] graph       => Edge list representing graph
Output:
  bool             => True if and only if graph is bipartite

Execution: python is_bipartite.py
"""
import unittest
from typing import List

"""
We select a random starting node and then  greedily assign each node to either
U or V. We do this using BFS. As we do this, we look for contradictions. If we
can successfully assign all the nodes, then the graph is bipartite.

Time Complexity: O(V+E)
Space Complexity: O(V)
"""
def is_bipartite(graph: List)->bool:

    """
    Traverse graph using depth first search to determine if graph is bipartite.
    """
    def dfs(curr: int):
        # Go through each of the neighbors
        for next in graph[curr]:
            # If the neighbor already has a color, make sure it matches
            if next in color:
                if color[next] == color[curr]:
                    return False
            # If the neighbor doesn't have a color, give it the right color and
            # continue dfs
            else:
                color[next] = -color[curr]
                if not dfs(next):
                    return False
        return True

    # Track the coloring of each node that we visit. For simplicity, nodes in U
    # will be set to 1 and nodes in V will be -1
    color = dict()

    # Our nodes aren't all necessarily connected, so we need to be sure to
    # iterate over every connected component of the graph
    for i in range(len(graph)):
        # If we've already visited a node, skip it
        if i not in color:
            # Initialize color
            color[i] = 1
            if not dfs(i):
                return False

    return True


class TestIsBipartite(unittest.TestCase):
    """Unit test for is_bipartite."""

    def test_1(self):
        """
        Test for graph:
            0----1
            |    |
            |    |
            3----2
        """
        graph = [[1, 3], [0, 2], [1, 3], [0, 2]]
        self.assertEqual(is_bipartite(graph), True)

        output = """
        The graph looks like this:
            0----1
            |    |
            |    |
            3----2
        We can divide the vertices into two groups: {0, 2} and {1, 3}.
        """
        print(f"Explanation: {output}")

    def test_2(self):
        """
        Test for graph:
            0----1
            | \  |
            |  \ |
            3----2
        """
        graph = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]
        self.assertEqual(is_bipartite(graph), False)
        output = """
        The graph looks like this:
            0----1
            | \  |
            |  \ |
            3----2
        We cannot find a way to divide the set of nodes into two
        independent subsets.
        """
        print(f"Explanation: {output}")

    # ADD YOUR TESTS HERE

if __name__ == '__main__':
    unittest.main()
