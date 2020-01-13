"""
Title: Merge two lists.

Problem:
    Merge two sorted linked lists.

Execution: python merge_two_lists.py
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

    def merge_sorted(self, llist):
    
        p = self.head 
        q = llist.head
        s = None
    
        if not p:
            return q
        if not q:
            return p

        if p and q:
            if p.data <= q.data:
                s = p 
                p = s.next
            else:
                s = q
                q = s.next
            new_head = s 
        while p and q:
            if p.data <= q.data:
                s.next = p 
                s = p 
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next
        if not p:
            s.next = q 
        if not q:
            s.next = p 
        return new_head


class TestMergeTwoLists(unittest.TestCase):
    """Unit test for merge_two_lists."""

    def test_1(self):
        llist_1 = LinkedList()
        llist_2 = LinkedList()

        llist_1.append(1)
        llist_1.append(5)
        llist_1.append(7)
        llist_1.append(9)
        llist_1.append(10)

        llist_2.append(2)
        llist_2.append(3)
        llist_2.append(4)
        llist_2.append(6)
        llist_2.append(8)

        llist_1.merge_sorted(llist_2)

        cur_node = llist_1.head
        nodes: List[str] = []
        while cur_node:
            nodes.append(cur_node.data)
            cur_node = cur_node.next
        self.assertEqual(nodes, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


if __name__ == '__main__':
    unittest.main()

