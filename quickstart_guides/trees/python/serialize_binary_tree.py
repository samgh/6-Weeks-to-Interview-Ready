"""
Title: Serialize binary tree

Problem:
    Serialization is the process of converting a data structure or object into a
    sequence of bits so that it can be stored in a file or memory buffer, or
    transmitted across a network connection link to be reconstructed later in
    the same or another computer environment.

    Design an algorithm to serialize and deserialize a binary tree. There is no
    restriction on how your serialization/deserialization algorithm should work.
    You just need to ensure that a binary tree can be serialized to a string and
    this string can be deserialized to the original tree structure.

Execution: python serialize_binary_tree.py
"""
from collections import deque
import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


def serialize(root: TreeNode) -> str:
    """Encodes a tree to a single string.

    :type root: TreeNode
    :rtype: str
    """
    res = []
    q = [root]
    while q:
        res.extend([str(node.val) if node else "#" for node in q])
        q = [child for node in q if node for child in (node.left, node.right)]

    return ",".join(res)


def deserialize(data):
    """Decodes your encoded data to tree.

    :type data: str
    :rtype: TreeNode
    """

    def next_node(data):
        next_val = next(data, None)
        next_node = TreeNode(next_val) if next_val.lstrip("-").isnumeric() else None

        return next_node

    data = iter(data.split(","))
    root = next_node(data)
    if not root:
        return None

    q = deque([root])

    while q:
        cur = q.popleft()
        left = next_node(data)
        if left:
            cur.left = left
            q.append(left)
        right = next_node(data)
        if right:
            cur.right = right
            q.append(right)

    return root


class TestSerializeBinaryTree(unittest.TestCase):
    """Unit tests for serialize_binary_tree."""

    def test_1(self):
        tn = TreeNode(1)
        tn.left = TreeNode(2)
        tn.right = TreeNode(3)
        tn.right.left = TreeNode(4)
        tn.right.right = TreeNode(5)

        self.assertEqual(serialize(tn), "1,2,3,#,#,4,5,#,#,#,#")


if __name__ == "__main__":
    unittest.main()
