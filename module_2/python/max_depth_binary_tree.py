"""
Title: Maximum depth of binary tree.

Problem:
    Given a binary tree, find its maximum depth.

    The maximum depth is the number of nodes along the longest path from the root
    node down to the farthest leaf node.

    Note: A leaf is a node with no children.

Execution: python max_depth_binary_tree.py
"""
import unittest


class Node():
    """Tree node class."""
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BinaryTree():
    """Binary tree class."""
    def __init__(self, root):
        self.root = Node(root)

    def max_depth_binary_tree(self, root):
        depth = 0
        level = [root] if root else []
        while level:
            depth += 1
            queue = []
            for el in level:
                if el.left:
                    queue.append(el.left)
                if el.right:
                    queue.append(el.right)
            level = queue
        return depth


class TestMaxDepthBinaryTree(unittest.TestCase):
    """Unit test for max depth binary tree."""

    def test_1(self):
        """
        Given binary tree [3,9,20,null,null,15,7],
            3
           / \
          9  20
            /  \
           15   7
        """
        tree = BinaryTree(3)
        tree.root.left = Node(9)
        tree.root.right = Node(20)
        tree.root.right.left = Node(15)
        tree.root.right.right = Node(7)
        self.assertEqual(tree.max_depth_binary_tree(tree.root), 3)


if __name__ == '__main__':
    unittest.main()
