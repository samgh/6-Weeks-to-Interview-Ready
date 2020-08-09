"""
Title: Lowest common ancestor

Problem:
    Given a binary tree, find the lowest common ancestor (LCA) of two given
    nodes in the tree.

    According to the definition of LCA on Wikipedia: “The lowest common ancestor
    is defined between two nodes p and q as the lowest node in T that has both p
    and q as descendants (where we allow a node to be a descendant of itself).”

    Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]

Execution: python lowest_common_ancestor.py
"""
import unittest


class Node:
    def __init__(self, data=None) -> None:
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self) -> None:
        self.root = None

    def insert(self, data: int) -> None:
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data: int, cur_node: Node) -> None:
        if data < cur_node.data:
            if cur_node.left is None:
                cur_node.left = Node(data)
                cur_node.left.parent = cur_node
            else:
                self._insert(data, cur_node.left)

        elif data > cur_node.data:
            if cur_node.right is None:
                cur_node.right = Node(data)
                cur_node.right.parent = cur_node
            else:
                self._insert(data, cur_node.right)
        else:
            print("Value already in tree!")

    def lca(self, data_1: int, data_2: int) -> int:
        x = max(data_1, data_2)
        y = min(data_1, data_2)

        cur_node = self.root
        while x < cur_node.data or y > cur_node.data:
            while cur_node.data < x:
                cur_node = cur_node.right
            while cur_node.data > y:
                cur_node = cur_node.left

        return cur_node.data


class TestMaxDepthBinaryTree(unittest.TestCase):
    """Unit tests for max_depth_binary_tree."""

    def test_1(self):
        bst = BST()
        bst.insert(8)
        bst.insert(3)
        bst.insert(10)
        bst.insert(1)
        bst.insert(6)
        bst.insert(4)
        bst.insert(7)
        bst.insert(13)

        self.assertEqual((bst.lca(1, 6)), 1)


if __name__ == "__main__":
    unittest.main()
