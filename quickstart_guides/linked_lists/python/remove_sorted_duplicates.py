"""
Title: Linked list remove duplicates (sorted)

Problem:
    Removes duplicates in sorted linked list.

Execution: python remove_sorted_duplicates.py
"""
from typing import List
import unittest


class Node:
    """Node for linked list."""

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """General linked list class."""

    def __init__(self):
        self.head = None

    def print_list(self) -> None:
        """Print elements of linked list."""
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def append(self, data):
        """Append item to end of linked list."""
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def remove_sorted_duplicates(self):
        """Remove duplicates from sorted linked list."""
        cur = self.head
        while cur is not None and cur.next is not None:
            if cur.next.data == cur.data:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return self.head


class TestRemoveDuplicates(unittest.TestCase):
    """Unit test for remove_sorted_duplicates."""

    def test_1(self):
        llist = LinkedList()
        llist.append(1)
        llist.append(2)
        llist.append(3)
        llist.append(3)

        llist.remove_sorted_duplicates()

        cur_node = llist.head
        nodes: List[str] = []
        while cur_node:
            nodes.append(cur_node.data)
            cur_node = cur_node.next
        self.assertEqual(nodes, [1, 2, 3])

    def test_2(self):
        llist = LinkedList()
        llist.append(8)
        llist.append(8)
        llist.append(9)
        llist.append(12)

        llist.remove_sorted_duplicates()

        cur_node = llist.head
        nodes: List[str] = []
        while cur_node:
            nodes.append(cur_node.data)
            cur_node = cur_node.next
        self.assertEqual(nodes, [8, 9, 12])


if __name__ == "__main__":
    unittest.main()
