"""
Title: Serialize and deserialize binary tree

Problem:
    Serialization is the process of converting a data structure or object into
    a sequence of bits so that it can be stored in a file or memory buffer, or
    transmitted across a network connection link to be reconstructed later in
    the same or another computer environment.

    Design an algorithm to serialize and deserialize a binary tree. There is no
    restriction on how your serialization/deserialization algorithm should
    work.  You just need to ensure that a binary tree can be serialized to a
    string and this string can be deserialized to the original tree structure.

Execution: python serialize_binary_tree.py
"""
import collections
import unittest

class TreeNode(object):
    def __init__(self, x: int):
        self.val = x
        self.left = None
        self.right = None


class Codec(object):

    def serialize(self, root: TreeNode) -> str:
        if not root:
            return ""
        res = [str(root.val)]
        q = collections.deque([root])
        while q:
            node = q.popleft()
            if node.left:
                res.append(str(node.left.val))
                q.append(node.left)
            else:
                res.append("null")
            if node.right:
                res.append(str(node.right.val))
                q.append(node.right)
            else:
                res.append("null")
        return f"[{','.join(res)}]"

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data: return
        s = data[1:len(data)-1]
        l = s.split(',')
        for i in range(len(l)):
            if l[i] == "null":
                l[i] = None
            else:
                l[i] = int(l[i])
        vals = collections.deque(l)
        root = TreeNode(vals.popleft())
        q = collections.deque([root])
        while vals:
            node = q.popleft()
            x = vals.popleft()
            if x is not None:
                node.left = TreeNode(x)
                q.append(node.left)
            x = vals.popleft()
            if x is not None:
                node.right = TreeNode(x)
                q.append(node.right)
        return root


class TestCodec(unittest.TestCase):
    """Unit test for serialize and deserialize."""

    def test_1(self):
        """
        You may serialize the following tree:
                1
               / \
              2   3
                 / \
                4   5

            as "[1,2,3,null,null,4,5]
        """
        codec = Codec()

        tree = TreeNode(1)
        tree.left = TreeNode(2)
        tree.right = TreeNode(3)
        tree.right.left = TreeNode(4)
        tree.right.right = TreeNode(5)

        expected_out = "[1,2,3,null,null,4,5,null,null,null,null]"

        self.assertEqual(codec.serialize(tree), expected_out)


if __name__ == '__main__':
    unittest.main()
