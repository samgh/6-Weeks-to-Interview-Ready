"""
Title: Lowest common ancestor (LCA)

Problem:
    Given a binary tree, find the lowest common ancestor (LCA) of two given
    nodes in the tree.

    According to the definition of LCA on Wikipedia: “The lowest common ancestor is
    defined between two nodes p and q as the lowest node in T that has both p and q
    as descendants (where we allow a node to be a descendant of itself).”

    Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]

Execution: python lca.py
"""
import unittest


class TreeNode:
    """Definition for a binary tree node."""

    def __init__(self, x: int):
        self.val = x
        self.left = None
        self.right = None


def lca(root, p, q):
    """Lowest common ancestor."""
    if root is None:
        return None
    if root.val == p or root.val == q:
        return root
    left_lca = lca(root.left, p, q)
    right_lca = lca(root.right, p, q)

    if left_lca and right_lca:
        return root

    return left_lca if left_lca else right_lca

class TestLCA(unittest.TestCase):
    """Unit test for lca."""

    def test_1(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)

        p = 4
        q = 5

        self.assertEqual(lca(root, p, q).val, 2)

    def test_2(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)

        p = 4
        q = 6

        self.assertEqual(lca(root, p, q).val, 1)


if __name__ == '__main__':
    unittest.main()
