"""
Title: Diameter of binary tree

Problem:
    Given a binary tree, you need to compute the length of the diameter of the
    tree. The diameter of a binary tree is the length of the longest path
    between any two nodes in a tree. This path may or may not pass through the
    root.

    Execution: python diameter_of_binary_tree.py
"""
import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def _diam(node: TreeNode, depth: int) -> [int, int]:
    if node is None:
        return depth, 0
    depth += 1
    left_depth, left_sum = _diam(node.left, depth)
    right_depth, right_sum = _diam(node.right, depth)
    new_size = (left_depth - depth) + (right_depth - depth)
    return max(left_depth, right_depth), max(new_size, left_sum, right_sum)


def diameter_of_binary_tree(root: TreeNode) -> int:
    return _diam(root, 0)[1]


class TestDiameterOfBinaryTree(unittest.TestCase):
    """Unit tests for diameter_of_binary_tree."""

    def test_1(self):
        tn = TreeNode(1)
        tn.left = TreeNode(2)
        tn.right = TreeNode(3)
        tn.left.left = TreeNode(4)
        tn.left.right = TreeNode(5)
        self.assertEqual(diameter_of_binary_tree(tn), 3)


if __name__ == "__main__":
    unittest.main()
