"""
Title: Add two numbers

Problem:
    You are given two non-empty linked lists representing two non-negative
    integers. The most significant digit comes first and each of their nodes
    contain a single digit. Add the two numbers and return it as a linked list.

    You may assume the two numbers do not contain any leading zero, except the
    number 0 itself.

    Follow up: What if you cannot modify the input lists? In other words,
    reversing the lists is not allowed.

Execution: python add_two_numbers.py
"""
import unittest
from typing import List, Tuple


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x: int):
        self.val = x
        self.next = None


def add_two_numbers(l1: ListNode, l2: ListNode) -> int:
    len1, len2 = get_length(l1), get_length(l2)
    l1 = add_leading_zeros(len2-len1, l1)
    l2 = add_leading_zeros(len1-len2, l2)
    c, ans = combine_list(l1, l2)
    if c > 0:
        l3 = ListNode(c)
        l3.next = ans
        ans = l3
    return ans


def get_length(node: ListNode) -> int:
    ll = 0
    while node:
        ll += 1
        node = node.next
    return ll


def add_leading_zeros(n: int, node: ListNode) -> ListNode:
    for i in range(n):
        new = ListNode(0)
        new.next = node
        node = new
    return node


def combine_list(l1: ListNode, l2: ListNode) -> Tuple[int, ListNode]:
    if (not l1 and not l2):
        return (0, None)
    c, new = combine_list(l1.next, l2.next)
    s = l1.val + l2.val + c
    ans = ListNode(s % 10)
    ans.next = new
    return (s//10, ans)


def compare_lists(l1: ListNode, l2: ListNode) -> bool:
    while l1:
        if l1.val != l2.val:
            return False
        l1 = l1.next
        l2 = l2.next
    return True


class TestAddTwoNumbers(unittest.TestCase):
    """Unit test for add_two_numbers."""

    def test_1(self):
        l1 = ListNode(7)
        l1.next = ListNode(2)
        l1.next.next = ListNode(4)
        l1.next.next.next = ListNode(3)

        l2 = ListNode(5)
        l2.next = ListNode(6)
        l2.next.next = ListNode(4)

        l_out = ListNode(7)
        l_out.next = ListNode(8)
        l_out.next.next = ListNode(0)
        l_out.next.next.next = ListNode(7)

        result = add_two_numbers(l1, l2)
        self.assertEqual(compare_lists(result, l_out), True)



if __name__ == '__main__':
    unittest.main()
