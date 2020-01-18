"""
Title: Linked list count occurrences

Problem:
    Count occurrences of nodes in linked list.

Execution: python count_occurrences.py
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

    def count_occurences_iterative(self, data):
        count = 0
        cur = self.head
        while cur:
            if cur.data == data:
                count += 1
            cur = cur.next
        return count

    def count_occurences_recursive(self, node, data):
        if not node:
            return 0
        if node.data == data:
            return 1 + self.count_occurences_recursive(node.next, data)
        else:
            return self.count_occurences_recursive(node.next, data)


class TestCountOccurrences(unittest.TestCase):
    """Unit test for count_occurrences."""

    def test_iterative(self):
        llist = LinkedList()
        llist.append(1)
        llist.append(2)
        llist.append(3)
        llist.append(4)
        llist.append(5)
        llist.append(6)

        llist_2 = LinkedList()
        llist_2.append(1)
        llist_2.append(2)
        llist_2.append(1)
        llist_2.append(3)
        llist_2.append(1)
        llist_2.append(4)
        llist_2.append(1)
        self.assertEqual(llist_2.count_occurences_iterative(1), 4)

    def test_recursive(self):
        llist = LinkedList()
        llist.append(1)
        llist.append(2)
        llist.append(3)
        llist.append(4)
        llist.append(5)
        llist.append(6)

        llist_2 = LinkedList()
        llist_2.append(1)
        llist_2.append(2)
        llist_2.append(1)
        llist_2.append(3)
        llist_2.append(1)
        llist_2.append(4)
        llist_2.append(1)
        self.assertEqual(llist_2.count_occurences_recursive(llist_2.head, 1), 4)


if __name__ == '__main__':
    unittest.main()

