"""
Title: Is Bipartite

Problem:
    A Bipartite Graph is a graph whose vertices can be divided into two
    independent sets, U and V such that every edge (u, v) either connects a
    vertex from U to V or a vertex from V to U. In other words, for every edge
    (u, v), either u belongs to U and v to V, or u belongs to V and v to U.

    We can also say that there is no edge that connects vertices of same set.

Execution: python is_bipartite.py
"""
import unittest


class Graph:
    """Generic graph class."""

    def __init__(self, vertices) -> None:
        self.vertices = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def is_bipartite(self, src: int) -> bool:

        # Create a color array to store colors assigned to all vertices. Vertex
        # number is used as index in this array. The value '-1' of  colorArr[i]
        # is used to indicate that no color is assigned to vertex 'i'. The value
        # 1 is used to indicate first color is assigned and value 0 indicates
        # second color is assigned.
        color_arr = [-1] * self.vertices

        # Assign first color to source.
        color_arr[src] = 1

        # Create a queue (FIFO) of vertex numbers and enqueue source vertex for
        # BFS traversal.
        queue = list()
        queue.append(src)

        # Run while there are vertices in queue (Similar to BFS).
        while queue:
            u = queue.pop()

            # Return "False" if there is a self-loop.
            if self.graph[u][u] == 1:
                return False

            for v in range(self.vertices):

                # An edge from u to v exists and destination v is not colored.
                if self.graph[u][v] == 1 and color_arr[v] == -1:

                    # Assign alternate color to this adjacent v of u.
                    color_arr[v] = 1 - color_arr[u]
                    queue.append(v)

                # An edge from u to v exists and destination v is colored with
                # same color as u.
                elif self.graph[u][v] == 1 and color_arr[v] == color_arr[u]:
                    return False

        # If we reach here, then all adjacent vertices can be colored with
        # alternate color.
        return True


class TestIsBipartite(unittest.TestCase):
    """Unit tests for is_bipartite."""

    def test_1(self):
        g = Graph(4)
        g.graph = [[0, 1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1, 0]]
        self.assertEqual(g.is_bipartite(0), True)


if __name__ == "__main__":
    unittest.main()
