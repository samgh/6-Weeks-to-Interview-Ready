"""
Title: Balanced binary tree

Problem:
    Given a binary tree, determine if it is height-balanced.

    For this problem, a height-balanced binary tree is defined as:

    a binary tree in which the left and right subtrees of every node differ in
    height by no more than 1.

Execution: python is_balanced_binary_tree.py
"""
import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


def is_balanced_binary_tree(root: TreeNode) -> bool:
    """
    :type root: TreeNode
    :rtype: bool
    """

    def height(node: TreeNode) -> int:
        if not node:
            return 0
        return 1 + max(height(node.left), height(node.right))

    def dfs(node: TreeNode) -> bool:
        if not node:
            return True
        left = height(node.left)
        right = height(node.right)
        if abs(left - right) > 1:
            return False
        return dfs(node.left) and dfs(node.right)

    def dfs2(node: TreeNode) -> int:
        if not node:
            return 0
        left = dfs2(node.left)
        if left == -1:
            return -1
        right = dfs2(node.right)
        if right == -1:
            return -1
        if abs(left - right) > 1:
            return -1
        return max(left, right) + 1

    return dfs2(root) != -1


class TestIsBalancedBinaryTree(unittest.TestCase):
    """Unit tests for is_balanced_binary_tree."""

    def test_1(self):
        tn = TreeNode(3)
        tn.right = TreeNode(20)
        tn.left = TreeNode(9)
        tn.right.left = TreeNode(15)
        tn.right.right = TreeNode(7)
        self.assertEqual(is_balanced_binary_tree(tn), True)

    def test_3(self):
        tn = TreeNode(1)
        tn.right = TreeNode(2)
        tn.left = TreeNode(2)
        tn.left.left = TreeNode(3)
        tn.left.right = TreeNode(3)
        tn.left.left.left = TreeNode(4)
        tn.left.left.right = TreeNode(4)
        self.assertEqual(is_balanced_binary_tree(tn), False)


if __name__ == "__main__":
    unittest.main()
