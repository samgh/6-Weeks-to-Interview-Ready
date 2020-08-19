"""
Title: Tree to list

Problem:
    Given a tree, write a function to convert it into a circular doubly linked
    list from left to right by only modifying the existing pointers.

Execution: python tree_to_list.py
"""
import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


def flatten(root: TreeNode) -> None:
    """
    :type root: TreeNode
    :rtype: None Do not return anything, modify root in-place instead.
    """
    if not root:
        return
    stack = []

    def flatten_helper(root: TreeNode) -> None:
        if not root:
            return
        stack.append(root)
        stack.append(root)
        if root.left:
            flatten_helper(root.left)
        if root.right:
            flatten_helper(root.right)

    flatten_helper(root)
    for i in range(len(stack) - 1):
        stack[i].left = None
        stack[i].right = stack[i + 1]
    stack[-1].left = None
    stack[-1].right = None


class TestTreeToList(unittest.TestCase):
    """Unit tests for tree_to_list."""

    def test_1(self):
        tn = TreeNode(1)
        tn.left = TreeNode(2)
        tn.right = TreeNode(3)
        tn.right.left = TreeNode(4)
        tn.right.right = TreeNode(5)

        flatten(tn)
        self.assertEqual(tn.val, 1)
        self.assertEqual(tn.right.val, 2)
        self.assertEqual(tn.right.right.val, 3)


if __name__ == "__main__":
    unittest.main()
