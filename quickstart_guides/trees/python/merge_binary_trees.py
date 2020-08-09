"""
Title: Merge binary trees.

Problem:
    Given two binary trees and imagine that when you put one of them to cover
    the other, some nodes of the two trees are overlapped while the others are
    not.

    You need to merge them into a new binary tree. The merge rule is that if two
    nodes overlap, then sum node values up as the new value of the merged node.
    Otherwise, the NOT null node will be used as the node of new tree.

    Execution: python merge_binary_trees.py
"""
import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


def merge_binary_trees(t1: TreeNode, t2: TreeNode) -> TreeNode:
    if t1 is None:
        return t2
    if t2 is None:
        return t1

    t1.val += t2.val
    t1.left = merge_binary_trees(t1.left, t2.left)
    t1.right = merge_binary_trees(t1.right, t2.right)

    return t1


class TestMergeBinaryTrees(unittest.TestCase):
    """Unit tests for merge_binary_trees."""

    def test_1(self):
        t1 = TreeNode(1)
        t1.left = TreeNode(3)
        t1.right = TreeNode(2)
        t1.left.left = TreeNode(5)

        t2 = TreeNode(2)
        t2.left = TreeNode(1)
        t2.right = TreeNode(3)
        t2.left.right = TreeNode(4)
        t2.right.right = TreeNode(7)

        tr = TreeNode(3)
        tr.left = TreeNode(4)
        tr.right = TreeNode(5)

        tr = merge_binary_trees(t1, t2)
        self.assertEqual(tr.val, 3)
        self.assertEqual(tr.left.val, 4)
        self.assertEqual(tr.right.val, 5)
        self.assertEqual(tr.left.left.val, 5)
        self.assertEqual(tr.left.right.val, 4)
        self.assertEqual(tr.right.right.val, 7)


if __name__ == "__main__":
    unittest.main()
