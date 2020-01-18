"""
Title: Linked list insertion

Problem:
    Insert an element into a linked list.

Execution: python insertion.py
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


class TestInsertion(unittest.TestCase):
    """Unit test for insertion."""

    def test_1(self):
        llist = LinkedList()
        llist.append("A")
        llist.append("B")
        llist.append("C")
        llist.append("D")

        cur_node = llist.head
        nodes: List[str] = []
        while cur_node:
            nodes.append(cur_node.data)
            cur_node = cur_node.next
        self.assertEqual(nodes, ["A", "B", "C", "D"])


if __name__ == '__main__':
    unittest.main()

