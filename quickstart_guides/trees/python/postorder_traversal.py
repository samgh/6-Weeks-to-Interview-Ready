"""
Title: Post-order traversal

Problem:
    Given a binary tree, return the post-order traversal of its nodes' values.

Execution: python postorder_traversal.py
"""
from typing import List
import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


def postorder_traversal(root: TreeNode) -> List[int]:
    res, stack = [], [(root, False)]
    while stack:
        node, visited = stack.pop()
        if node:
            if visited:
                # Add to result if visited.
                res.append(node.val)
            else:
                # Post-order traverse.
                stack.append((node, True))
                stack.append((node.right, False))
                stack.append((node.left, False))
    return res


class TestPostorderTraversal(unittest.TestCase):
    """Unit tests for postorder_traversal."""

    def test_1(self):
        tn = TreeNode(1)
        tn.right = TreeNode(2)
        tn.right.left = TreeNode(3)
        self.assertEqual(postorder_traversal(tn), [3, 2, 1])


if __name__ == "__main__":
    unittest.main()
