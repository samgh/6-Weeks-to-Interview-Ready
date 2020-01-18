"""
Title: Linked list nth to last

Problem:
    Obtain the nth-to-last node.

Execution: python nth_to_last.py
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

    def len_iterative(self):

        count = 0
        cur_node = self.head

        while cur_node:
            count += 1
            cur_node = cur_node.next
        return count

    def print_nth_from_last(self, n):

        # Method 1:
        total_len = self.len_iterative()

        cur = self.head
        while cur:
            if total_len == n:
                return cur.data
            total_len -= 1
            cur = cur.next
        if cur is None:
            return


class TestNthToLast(unittest.TestCase):
    """Unit test for nth_to_last."""

    def test_1(self):
        llist = LinkedList()
        llist.append("A")
        llist.append("B")
        llist.append("C")
        llist.append("D")
        
        self.assertEqual(llist.print_nth_from_last(2), "C")


if __name__ == '__main__':
    unittest.main()

