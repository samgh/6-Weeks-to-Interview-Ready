"""
Title: Maximum depth of binary tree

Problem:
    Given a binary tree, find its maximum depth.

    The maximum depth is the number of nodes along the longest path from the
    root node down to the farthest leaf node.

    Note: A leaf is a node with no children.

Execution: python max_depth_binary_tree.py
"""
import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


def max_depth_binary_tree(root: TreeNode) -> int:
    if root is None:
        return 0
    left = max_depth_binary_tree(root.left) + 1
    right = max_depth_binary_tree(root.right) + 1
    if left > right:
        return left
    return right


class TestMaxDepthBinaryTree(unittest.TestCase):
    """Unit tests for max_depth_binary_tree."""

    def test_1(self):
        tn = TreeNode(3)
        tn.left = TreeNode(9)
        tn.right = TreeNode(20)
        tn.right.left = TreeNode(15)
        tn.right.right = TreeNode(7)
        self.assertEqual(max_depth_binary_tree(tn), 3)


if __name__ == "__main__":
    unittest.main()
