"""
Title: Copy list random pointer

Problem:
    A linked list is given such that each node contains an additional random
    pointer which could point to any node in the list or null.

    Return a deep copy of the list.

    The Linked List is represented in the input/output as a list of n nodes.
    Each node is represented as a pair of [val, random_index] where:

    val: an integer representing Node.val
    random_index: the index of the node (range from 0 to n-1) where random
    pointer points to, or null if it does not point to any node.

    Execution: python copy_list_random_pointer.py
"""
import unittest
from typing import List


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


def copy_random_list(head: 'Node') -> 'Node':
    memo = dict()

    def fn(n):
        """Return (deep) copy of node"""
        if n and n not in memo:
            cln = memo[n] = Node(n.val)
            cln.next, cln.random = fn(n.next), fn(n.random)
        return memo.get(n)

    return fn(head)


class TestCopyListRandomPointer(unittest.TestCase):
    """Unit test for merge_k_lists."""

    def test_1(self):
        pass


if __name__ == '__main__':
    head = [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]

    list_1 = Node(1)
    list_1.random = 1
    list_1.next = Node(4)
    # list_1.random = 1
    copy_random_list(list_1)
#    list_1.next.next = ListNode(5)    #copy_random_list(head)
#    unittest.main()
