"""
Title: Linked list random node

Problem:
    Given a singly linked list, return a random node's value from the linked
    list. Each node must have the same probability of being chosen.

    Follow up: What if the linked list is extremely large and its length is
    unknown to you? Could you solve this efficiently without using extra space?

Execution: python random_node.py
"""
from random import random
import unittest


class ListNode:
    def __init__(self, x: int) -> None:
        self.val = x
        self.next = None


class LinkedList():
    def __init__(self, head: ListNode) -> None:
        self.head = head

    def get_random(self) -> int:
        cur_node = self.head
        counter = 1
        choice = -1

        while cur_node is not None:
            if random() < 1/counter:
                choice = cur_node.val
            cur_node = cur_node.next
            counter += 1
        return choice

    def check_random_node(self, node_val: int) -> bool:
        return node_val in [1, 2, 3]



class TestRandomNode(unittest.TestCase):
    """Unit test for get_random."""

    def test_1(self):
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)

        ll = LinkedList(head)
        self.assertEqual(ll.check_random_node(ll.get_random()), True)
        print("Explanation: .")


if __name__ == '__main__':
    unittest.main()
