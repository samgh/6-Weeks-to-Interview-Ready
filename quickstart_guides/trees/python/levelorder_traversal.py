"""
Title: Levelorder traversal

Problem:
    Given a binary tree, return the level-order traversal of its nodes' values.

Execution: python levelorder_traversal.py
"""
from typing import List
import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


def helper_util(lst, rst, result, level):
    # To add layer to the stack
    if len(result) < level:
        result.append([])

    # Keep tracking the left sub tree
    if lst is not None:
        result[level - 1].extend([lst.val])
        helper_util(lst.left, lst.right, result, level + 1)

    # Keep tracking the right sub tree
    if rst is not None:
        result[level - 1].extend([rst.val])
        helper_util(rst.left, rst.right, result, level + 1)

    return result


def levelorder_traversal(root: TreeNode) -> List[List[int]]:

    if root is None:
        return []

    result = [[root.val]]
    lst = root.left
    rst = root.right

    result = helper_util(lst, rst, result, 2)

    result = [x for x in result if len(x) != 0]

    return result


class TestLevelorderTraversal(unittest.TestCase):
    """Unit tests for levelorder_traversal."""

    def test_1(self):
        tn = TreeNode(3)
        tn.right = TreeNode(20)
        tn.left = TreeNode(9)
        tn.right.left = TreeNode(15)
        tn.right.right = TreeNode(7)
        self.assertEqual(levelorder_traversal(tn), [[3], [9, 20], [15, 7]])


if __name__ == "__main__":
    unittest.main()
