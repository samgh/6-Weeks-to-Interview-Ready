"""
Title: Merge k lists.

Problem:
    Merge k sorted linked lists and return it as one sorted list. Analyze and
    describe its complexity.

Execution: python merge_k_lists.py
"""
import unittest
from typing import List


class ListNode:
    """Class for Linked List node."""

    def __init__(self, x):
        self.val = x
        self.next = None


def merge_k_lists(lists: List[ListNode]) -> ListNode:
    """Merge K-lists."""
    nodes = []
    head = point = ListNode(0)
    for l in lists:
        while l:
            nodes.append(l.val)
            l = l.next
    for x in sorted(nodes):
        point.next = ListNode(x)
        point = point.next
    return head.next


def check_list_equal(list_1: ListNode, list_2: ListNode) -> bool:
    """Check if two lists are equal."""
    while list_1.next:
        if list_1.val != list_2.val:
            return False
        list_1 = list_1.next
        list_2 = list_2.next
    return True


class TestMergeKLists(unittest.TestCase):
    """Unit test for merge_k_lists."""

    def test_1(self):
        list_1 = ListNode(1)
        list_1.next = ListNode(4)
        list_1.next.next = ListNode(5)

        list_2 = ListNode(1)
        list_2.next = ListNode(3)
        list_2.next.next = ListNode(4)

        list_3 = ListNode(2)
        list_3.next = ListNode(6)

        k_lists = [list_1, list_2, list_3]

        # Expected output for the above test.
        expected_out = ListNode(1)
        expected_out.next = ListNode(1)
        expected_out.next.next = ListNode(2)
        expected_out.next.next.next = ListNode(3)
        expected_out.next.next.next.next = ListNode(4)
        expected_out.next.next.next.next.next = ListNode(4)
        expected_out.next.next.next.next.next.next = ListNode(5)
        expected_out.next.next.next.next.next.next.next = ListNode(6)

        out_list = merge_k_lists(k_lists)
        self.assertEqual(check_list_equal(out_list, expected_out), True)


if __name__ == "__main__":
    unittest.main()
