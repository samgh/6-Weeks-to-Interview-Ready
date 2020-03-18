"""
Title: Linked list rotate

Problem:
    Rotate nodes in linked list.

Execution: python rotate.py
"""
from typing import List
import unittest


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def rotate(self, k):
        p = self.head
        q = self.head
        prev = None
        
        count = 0
        
        while p and count < k:
            prev = p
            p = p.next
            q = q.next
            count += 1
        p = prev
        while q:
            prev = q
            q = q.next
        q = prev

        q.next = self.head
        self.head = p.next
        p.next = None


class TestRotate(unittest.TestCase):
    """Unit test for rotate."""

    def test_1(self):
        llist = LinkedList()
        llist.append(1)
        llist.append(2)
        llist.append(3)
        llist.append(4)
        llist.append(5)
        llist.append(6)

        llist.rotate(4)

        cur_node = llist.head
        nodes: List[str] = []
        while cur_node:
            nodes.append(cur_node.data)
            cur_node = cur_node.next
        self.assertEqual(nodes, [5, 6, 1, 2, 3, 4])


if __name__ == '__main__':
    unittest.main()

