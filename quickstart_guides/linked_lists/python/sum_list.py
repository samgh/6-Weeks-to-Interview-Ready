"""
Title: Linked list sum list

Problem:
    Sum two linked lists

Execution: python sum_list.py
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

    def sum_two_lists(self, llist):
        p = self.head
        q = llist.head

        sum_llist = LinkedList()

        carry = 0
        while p or q:
            if not p:
                i = 0
            else:
                i = p.data
            if not q:
                j = 0 
            else:
                j = q.data
            s = i + j + carry
            if s >= 10:
                carry = 1
                remainder = s % 10
                sum_llist.append(remainder)
            else:
                carry = 0
                sum_llist.append(s)
            if p:
                p = p.next
            if q:
                q = q.next
        return sum_llist


class TestSumList(unittest.TestCase):
    """Unit test for sum_list."""

    def test_1(self):
        llist1 = LinkedList()
        llist1.append(5)
        llist1.append(6)
        llist1.append(3)

        llist2 = LinkedList()
        llist2.append(8)
        llist2.append(4)
        llist2.append(2)

        llist1.sum_two_lists(llist2)
        cur_node = llist1.head
        nodes: List[str] = []
        while cur_node:
            nodes.append(cur_node.data)
            cur_node = cur_node.next
        self.assertEqual(nodes, [5, 6, 3])


if __name__ == '__main__':
    unittest.main()

