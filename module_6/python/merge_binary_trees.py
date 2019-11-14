"""
Title: Merge two binary trees

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
    def __init__(self, x: int):
        self.val = x
        self.left = None
        self.right = None


def merge_binary_trees(t1: TreeNode, t2: TreeNode) -> TreeNode:
    if not t1:
        return t2
    elif not t2:
        return t1
    else:
        res = TreeNode(t1.val + t2.val)
        res.left = merge_binary_trees(t1.left, t2.left)
        res.right = merge_binary_trees(t1.right, t2.right)
    return res


class TestXXX(unittest.TestCase):
    """Unit test for merge_binary_trees."""

    def test_1(self):
        tree_1 = TreeNode(1)
        tree_1.left = TreeNode(3)
        tree_1.right = TreeNode(2)
        tree_1.left.left = TreeNode(5)

        tree_2 = TreeNode(2)
        tree_2.left = TreeNode(1)
        tree_2.right = TreeNode(3)
        tree_2.left.right = TreeNode(4)
        tree_2.right.right = TreeNode(7)

        res_tree = merge_binary_trees(tree_1, tree_2)

        self.assertEqual(res_tree.val, 3)
        self.assertEqual(res_tree.left.val, 4)
        self.assertEqual(res_tree.right.val, 5)
        self.assertEqual(res_tree.left.left.val, 5)
        self.assertEqual(res_tree.left.right.val, 4)
        self.assertEqual(res_tree.right.right.val, 7)


if __name__ == '__main__':
    unittest.main()
