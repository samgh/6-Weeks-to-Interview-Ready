"""
Title: In-order traversal

Problem:
    Given a binary tree, return the inorder traversal of its nodes' values.

Execution: python inorder_traversal.py
"""
from typing import List
import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


def inorder_traversal(root: TreeNode) -> List[int]:
    """Perform in-order traversal."""

    def traverse(root, out, visited):
        if root:
            out = traverse(root.left, out, visited)
            if root not in visited:
                visited.append(root)
                out.append(root.val)
            out = traverse(root.right, out, visited)
        return out

    return traverse(root, [], [])


class TestInorderTraversal(unittest.TestCase):
    """Unit tests for inorder_traversal."""

    def test_1(self):
        tn = TreeNode(1)
        tn.right = TreeNode(2)
        tn.right.left = TreeNode(3)
        self.assertEqual(inorder_traversal(tn), [1, 3, 2])


if __name__ == "__main__":
    unittest.main()
