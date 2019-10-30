"""
Title: Max path sum

Problem:
    Given a non-empty binary tree, find the maximum path sum.

    For this problem, a path is defined as any sequence of nodes from some
    starting node to any node in the tree along the parent-child connections.
    The path must contain at least one node and does not need to go through the
    root.

Execution: python max_path_sum.py
"""
import unittest


class TreeNode:
    """Definition of binary tree node."""

    def __init__(self, x: int) -> None:
        """Set value for node and left/right nodes."""
        self.val = x
        self.left = None
        self.right = None


def max_path_sum(root: TreeNode) -> int:
    def dfs(root):
        if root:
            l, tl = dfs(root.left)
            r, tr = dfs(root.right)
            t = l + r + root.val
            return max(root.val, l + root.val, r+root.val), max(t, tl, tr, l, r)
        else:
            return float('-inf'),float('-inf')

    m, n = dfs(root)
    return max(m,n)


class TestMaxSumPath(unittest.TestCase):
    """Unit test for max_path_sum."""

    def test_1(self):
        tree = TreeNode(1)
        tree.left = TreeNode(2)
        tree.right = TreeNode(3)

        self.assertEqual(max_path_sum(tree), 6)

    def test_2(self):
        tree = TreeNode(-10)
        tree.left = TreeNode(9)
        tree.right = TreeNode(20)
        tree.right.left = TreeNode(15)
        tree.right.right = TreeNode(7)

        self.assertEqual(max_path_sum(tree), 42)


if __name__ == '__main__':
    unittest.main()
