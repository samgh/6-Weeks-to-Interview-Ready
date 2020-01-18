"""
Title: Linked list length

Problem:
    Calculate length of linked list.

Execution: python length.py
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

    def length(self):

        count = 0
        cur_node = self.head

        while cur_node:
            count += 1
            cur_node = cur_node.next
        return count


class TestLength(unittest.TestCase):
    """Unit test for length."""

    def test_iterative(self):
        llist = LinkedList()
        llist.append("A")
        llist.append("B")
        llist.append("C")
        llist.append("D")
        self.assertEqual(llist.length(), 4)


if __name__ == '__main__':
    unittest.main()

