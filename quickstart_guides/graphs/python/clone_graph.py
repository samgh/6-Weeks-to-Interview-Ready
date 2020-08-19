"""
Title: Clone graph

Problem:
    Given the root node of a directed graph, clone this graph by creating its
    deep copy so that the cloned graph has the same vertices and edges as the
    original graph.

    Let’s look at the below graphs as an example. If the input graph is
    G = (V, E) where V is set of vertices and E is set of edges, then the output
    graph (cloned graph) G’ = (V’, E’) such that V = V’ and E = E’.

Execution: python clone_graph.py
"""
import unittest


class Node:
    """Node class for graph."""

    def __init__(self, d: int) -> None:
        self.data = d
        self.neighbors = []


def clone_rec(root, nodes_completed):
    if root is None:
        return None

    p_new = Node(root.data)
    nodes_completed[root] = p_new

    for p in root.neighbors:
        x = nodes_completed.get(p)
        if x is None:
            p_new.neighbors += [clone_rec(p, nodes_completed)]
        else:
            p_new.neighbors += [x]
    return p_new


def clone(root):
    nodes_completed = {}
    return clone_rec(root, nodes_completed)


# This is un-directed graph i.e. if there is an edge from x to y that means
# there must be an edge from y to x and there is no edge from a node to itself
# hence there can maximum of (nodes * nodes - nodes) / 2 edges in this graph.
def create_test_graph_undirected(nodes_count, edges_count):
    vertices = []
    for i in range(0, nodes_count):
        vertices += [Node(i)]

    all_edges = []
    for i in range(0, nodes_count):
        for j in range(i + 1, nodes_count):
            all_edges.append([i, j])

    for i in range(0, min(edges_count, len(all_edges))):
        edge = all_edges[i]
        vertices[edge[0]].neighbors += [vertices[edge[1]]]
        vertices[edge[1]].neighbors += [vertices[edge[0]]]

    return vertices


def print_graph(vertices):
    for n in vertices:
        print(str(n.data), end=": {")
        for t in n.neighbors:
            print(str(t.data), end=" ")
        print()


def print_graph_rec(root, visited_nodes):
    if root is None or root in visited_nodes:
        return

    x = []
    visited_nodes.add(root)

    x.append(root.data)
    for n in root.neighbors:
        x.append(n.data)

    return x


class TestCloneGraph(unittest.TestCase):
    """Unit tests for clone_graph."""

    def test_1(self):
        vertices = create_test_graph_undirected(7, 18)

        visited_nodes = set()
        x = print_graph_rec(vertices[0], visited_nodes)

        visited_nodes = set()
        y = print_graph_rec(clone(vertices[0]), visited_nodes)

        self.assertEqual(x, y)


if __name__ == "__main__":
    unittest.main()
