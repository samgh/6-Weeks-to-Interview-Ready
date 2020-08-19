"""
Title: Linked list remove unsorted duplicates

Problem:
    Removes duplicates in an unsorted linked list.

Execution: python remove_unsorted_duplicates.py
"""
from typing import List
import unittest


class Node:
    """Linked list Node class."""

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """Generic linked list class."""

    def __init__(self):
        self.head = None

    def print_list(self):
        """Print linked list."""
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def append(self, data):
        """Append node to end of linked list."""
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def remove_duplicates(self):
        """Remove duplicates from an (unsorted) linked list."""
        cur = self.head
        prev = None

        dup_values = dict()

        while cur:
            if cur.data in dup_values:
                # Remove node:
                prev.next = cur.next
            else:
                # Have not encountered element before.
                dup_values[cur.data] = 1
                prev = cur
            cur = prev.next


class TestRemoveDuplicates(unittest.TestCase):
    """Unit test for remove_unsorted_duplicates."""

    def test_1(self):
        llist = LinkedList()
        llist.append(1)
        llist.append(6)
        llist.append(1)
        llist.append(4)
        llist.append(2)
        llist.append(2)
        llist.append(4)

        llist.remove_duplicates()

        cur_node = llist.head
        nodes: List[str] = []
        while cur_node:
            nodes.append(cur_node.data)
            cur_node = cur_node.next
        self.assertEqual(nodes, [1, 6, 4, 2])

    def test_2(self):
        llist = LinkedList()
        llist.append(1)
        llist.append(2)
        llist.append(2)
        llist.append(1)
        llist.append(2)
        llist.append(2)
        llist.append(1)

        llist.remove_duplicates()

        cur_node = llist.head
        nodes: List[str] = []
        while cur_node:
            nodes.append(cur_node.data)
            cur_node = cur_node.next
        self.assertEqual(nodes, [1, 2])

    def test_3(self):
        llist = LinkedList()
        llist.append(3)
        llist.append(2)
        llist.append(1)

        llist.remove_duplicates()

        cur_node = llist.head
        nodes: List[str] = []
        while cur_node:
            nodes.append(cur_node.data)
            cur_node = cur_node.next
        self.assertEqual(nodes, [3, 2, 1])


if __name__ == "__main__":
    unittest.main()
