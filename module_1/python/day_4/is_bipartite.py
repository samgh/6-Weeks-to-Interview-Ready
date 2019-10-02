"""
Title: Determine if a given graph is bipartite.

Problem:
    Given an undirected graph, return true if and only if it is bipartite.

    Recall that a graph is bipartite if we can split it's set of nodes into two
    independent subsets A and B such that every edge in the graph has one node in A
    and another node in B.

    The graph is given in the following form: graph[i] is a list of indexes j for
    which the edge between nodes i and j exists.  Each node is an integer between 0
    and graph.length - 1.  There are no self edges or parallel edges: graph[i] does
    not contain i, and it doesn't contain any element twice.

Execution: python is_bipartite.py
"""
import unittest


def is_bipartite(graph: list):
    """Function for checking if graph is bipartite."""
    color = dict()
    def depth_first_search(position: int):
        """Use depth first search to determine if graph is bipartite."""
        for i in graph[position]:
            if i in color:
                if color[i] == color[position]:
                    return False
            else:
                color[i] = 1 - color[position]
                if not depth_first_search(i):
                    return False
        return True
    for i in range(len(graph)):
        if i not in color:
            color[i] = 0
            if not depth_first_search(i):
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


if __name__ == '__main__':
    unittest.main()
