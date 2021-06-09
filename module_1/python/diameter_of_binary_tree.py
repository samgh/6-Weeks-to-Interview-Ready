"""
Title: Diameter of Binary Tree
Leetcode Link: https://leetcode.com/problems/diameter-of-binary-tree/

Problem: Given a binary tree, you need to compute the length of the diameter of
the tree. The diameter of a binary tree is the length of the longest path
between any two nodes in a tree. This path may or may not pass through the root.

Input:
    root: TreeNode      => the root of the tree
Output:
    int                 => the diameter of the tree whose root is root

Execution: python diameter_of_binary_tree.py
"""
import unittest
from typing import List


# Definition for a binary tree node.
class TreeNode:
    """Definition for a binary tree node."""

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

"""
The diameter of the tree is either:
   a) The diameter of the left subtree
   b) The diameter of the right subtree
   c) height(left subtree) + height(right subtree) + 1
We will solve this by recursively computing the diameters of the left
and right subtree while simultaneously computing the heights

Time Complexity: O(n)
Space Complexity: O(n)
"""
def diameter_of_binary_tree(root: TreeNode) -> int:
    # Our approach counts the number of nodes in the path, but Leetcode
    # requires the number of edges, which is # nodes - 1
    return diameter_of_binary_tree_inner(root)[0]-1

"""
Inner function that computes height in addition to diameter.

Returns [diameter, height]
"""
def diameter_of_binary_tree_inner(root: TreeNode) -> List[int]:
    # Base Case. If root is null, diameter of empty tree is 0 and height is 0
    if not root:
        return [0,0]

    # Find the diameter and height of the two subtrees
    left = diameter_of_binary_tree_inner(root.left)
    right = diameter_of_binary_tree_inner(root.right)

    # Find the maximum of the diameters and the combined heights
    diam = max(left[0], right[0])
    diam = max(diam, left[1]+right[1]+1)

    # Find the height of the current subtree
    height = max(left[1], right[1])+1

    return [diam, height]

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

        self.assertEqual(diameter_of_binary_tree(tree), 3)
        print("Explanation: Return 3, which is the length of the path [4, 2, 1, 3] or [5, 2, 1, 3].")

    # ADD YOUR OWN TESTS HERE

if __name__ == '__main__':
    unittest.main()
