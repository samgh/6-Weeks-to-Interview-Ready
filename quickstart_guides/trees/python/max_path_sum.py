"""
Title: Max sum path

Problem:
    Given a non-empty binary tree, find the maximum path sum.

    For this problem, a path is defined as any sequence of nodes from some
    starting node to any node in the tree along the parent-child connections.
    The path must contain at least one node and does not need to go through the
    root.

    Execution: python max_sum_path.py
"""
import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


class MaxSumPath:
    def __init__(self) -> None:
        self.max_value = 0

    def max_sum_path(self, root: TreeNode) -> int:
        if root:
            # Initialize maxval default with root.val.
            self.max_value = root.val
        self.traverse(root)
        return self.max_value  # return value

    def traverse(self, root: TreeNode) -> int:
        """
        Find maximum from each root nodes to left&right tree and store the
        highest one.
        """
        if root is None:
            return 0
        # Recurse left and store val if > 0.
        left = max(0, self.traverse(root.left))
        # Recurse right and store val if > 0.
        right = max(0, self.traverse(root.right))
        # Compare result with existing node val maximum.
        self.max_value = max(left + right + root.val, self.max_value)
        # Return maximum of left traversal from current node and vice versa.
        return root.val + max(left, right)


class TestMaxPathSum(unittest.TestCase):
    """Unit tests for max_path_sum."""

    def test_1(self):
        tn = TreeNode(1)
        tn.left = TreeNode(2)
        tn.right = TreeNode(3)
        msp = MaxSumPath()
        self.assertEqual(msp.max_sum_path(tn), 6)


if __name__ == "__main__":
    unittest.main()
