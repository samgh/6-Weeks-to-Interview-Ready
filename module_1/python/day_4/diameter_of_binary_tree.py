"""
Title: Diameter of binary tree.

Problem: Given a binary tree, you need to compute the length of the diameter of
         the tree. The diameter of a binary tree is the length of the longest path
         between any two nodes in a tree. This path may or may not pass through the
         root.

Execution: python diameter_of_binary_tree.py
"""
import unittest


# Definition for a binary tree node.
class TreeNode:
    """Definition for a binary tree node."""

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class TreeFunctions:
    """Definition for the functions used for binary tree."""

    def diameter_of_binary_tree(self, root: TreeNode):
        """Function for calculating the diameter of a binary tree."""
        self.ans = 1
        def depth(node):
            if not node:
                return 0
            L = depth(node.left)
            R = depth(node.right)
            self.ans = max(self.ans, L + R + 1)
            return max(L, R) + 1
    
        depth(root)
        return self.ans - 1


class TestDiameterOfBinaryTree(unittest.TestCase):
    """Unit test for calculating the diameter of binary tree."""

    def test_1(self):
        """
        Test for calculating the diameter of the following binary tree:
                  1
                 / \
                2   3
               / \
              4   5
        """
        # Construct the above binary tree.
        tree = TreeNode(1)
        tree.left = TreeNode(2)
        tree.right = TreeNode(3)
        tree.left.left = TreeNode(4)
        tree.left.right = TreeNode(5)

        tree_functions = TreeFunctions()
        self.assertEqual(tree_functions.diameter_of_binary_tree(tree), 3)
        print("Explanation: Return 3, which is the length of the path [4, 2, 1, 3] or [5, 2, 1, 3].")


if __name__ == '__main__':
    unittest.main()
