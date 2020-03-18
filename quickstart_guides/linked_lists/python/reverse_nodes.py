"""
Title: Linked list reverse nodes.

Problem:
    Reverse nodes in linked list.

Execution: python reverse_nodes.py
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

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def reverse_iterative(self):

        prev = None
        cur = self.head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        self.head = prev

    def reverse_recursive(self):

        def _reverse_recursive(cur, prev):
            if not cur:
                return prev
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            return _reverse_recursive(cur, prev)

        self.head = _reverse_recursive(cur=self.head, prev=None)


class TestReverseNodes(unittest.TestCase):
    """Unit test for reverse_nodes."""

    def test_recursive(self):
        llist = LinkedList()
        llist.append("A")
        llist.append("B")
        llist.append("C")
        llist.append("D")

        llist.reverse_recursive()
        cur_node = llist.head
        nodes: List[str] = []
        while cur_node:
            nodes.append(cur_node.data)
            cur_node = cur_node.next
        self.assertEqual(nodes, ["D", "C", "B", "A"])

    def test_iterative(self):
        llist = LinkedList()
        llist.append("A")
        llist.append("B")
        llist.append("C")
        llist.append("D")

        llist.reverse_iterative()
        cur_node = llist.head
        nodes: List[str] = []
        while cur_node:
            nodes.append(cur_node.data)
            cur_node = cur_node.next
        self.assertEqual(nodes, ["D", "C", "B", "A"])


if __name__ == '__main__':
    unittest.main()

