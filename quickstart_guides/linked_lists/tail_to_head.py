"""
Title: Linked list tail-to-head

Problem:
    Moves node from tail to head of linked list.

Execution: python tail_to_head.py
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

    def move_tail_to_head(self):
        
        last = self.head
        second_to_last = None
        while last.next:
            second_to_last = last
            last = last.next
        last.next = self.head
        second_to_last.next = None
        self.head = last


class TestTailToHead(unittest.TestCase):
    """Unit test for tail_to_head."""

    def test_1(self):

        # A -> B -> C -> D -> Null
        # D -> A -> B -> C -> Null
        llist = LinkedList()
        llist.append("A")
        llist.append("B")
        llist.append("C")
        llist.append("D")

        llist.move_tail_to_head()

        cur_node = llist.head
        nodes: List[str] = []
        while cur_node:
            nodes.append(cur_node.data)
            cur_node = cur_node.next
        self.assertEqual(nodes, ["D", "A", "B", "C"])


if __name__ == '__main__':
    unittest.main()
