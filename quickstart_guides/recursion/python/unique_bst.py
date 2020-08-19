"""
Title: Unique BST.

Problem:
    Construct all possible BSTs for keys 1 to N.

Execution: python unique_bst.py
"""
from typing import Any, List
import unittest


class Node:
    def __init__(self, item):
        self.key = item
        self.left = None
        self.right = None


def preorder(root, lst: List[int]) -> List[int]:
    if root:
        lst.append(root.key)
        preorder(root.left, lst)
        preorder(root.right, lst)
    return lst


def construct_trees(start: int, end: int) -> List[Any]:
    node_list = []

    # If start > end, then subtree will be empty, so return None in the list.
    if start > end:
        node_list.append(None)
        return node_list

    # Iterate through all values from start to end for constructing left and
    # right subtree.
    for i in range(start, end + 1):

        # Construct left subtree.
        left_subtree = construct_trees(start, i - 1)

        # Construct right subtree.
        right_subtree = construct_trees(i + 1, end)

        # Loop through all left and right subtrees.
        for j in range(len(left_subtree)):
            left = left_subtree[j]
            for k in range(len(right_subtree)):
                right = right_subtree[k]
                node = Node(i)
                node.left = left
                node.right = right
                node_list.append(node)
    return node_list


class TestUniqueBST(unittest.TestCase):
    """Unit tests for unique_bst."""

    def test_1(self):
        expected_out = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [3, 1, 2], [3, 2, 1]]

        total_trees = construct_trees(1, 3)

        for i in range(len(total_trees)):
            res = preorder(total_trees[i], [])
            self.assertEqual(res, expected_out[i])


if __name__ == "__main__":
    unittest.main()
