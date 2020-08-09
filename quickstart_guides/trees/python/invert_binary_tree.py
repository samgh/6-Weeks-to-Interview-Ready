"""
Title: Invert binary tree

Problem:
    Invert a binary tree.

    Execution: python invert_binary_tree.py
"""
from typing import Optional
import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


def invert_binary_tree(t: TreeNode) -> Optional[TreeNode]:
    if t is None:
        return None
    right = invert_binary_tree(t.right)
    left = invert_binary_tree(t.left)

    t.left = right
    t.right = left

    return t


class TestInvertBinaryTree(unittest.TestCase):
    """Unit tests for invert_binary_tree."""

    def test_1(self):
        t1 = TreeNode(4)
        t1.left = TreeNode(2)
        t1.right = TreeNode(7)
        t1.left.left = TreeNode(1)
        t1.left.right = TreeNode(3)
        t1.right.left = TreeNode(6)
        t1.right.right = TreeNode(9)

        t2 = invert_binary_tree(t1)

        self.assertEqual(t2.val, 4)
        self.assertEqual(t2.left.val, 7)
        self.assertEqual(t2.right.val, 2)
        self.assertEqual(t2.left.left.val, 9)
        self.assertEqual(t2.left.right.val, 6)
        self.assertEqual(t2.right.left.val, 3)
        self.assertEqual(t2.right.right.val, 1)


if __name__ == "__main__":
    unittest.main()
