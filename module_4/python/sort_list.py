"""
Title: Sort list

Problem: Sort a linked list in O(n log n) time using constant space complexity.


Execution: python sort_list.py
"""
import unittest


class ListNode:
    """Definition for singly-linked list."""

    def __init__(self, x: int):
        """Set value and next for ListNode."""
        self.val = x
        self.next = None


def merge(h1: ListNode, h2: ListNode) -> ListNode:
    """Merge two ListNode objects."""
    dummy = tail = ListNode(None)
    while h1 and h2:
        if h1.val < h2.val:
            tail.next, tail, h1 = h1, h1, h1.next
        else:
            tail.next, tail, h2 = h2, h2, h2.next

    tail.next = h1 or h2
    return dummy.next


def sort_list(head: ListNode) -> ListNode:
    """Sort ListNode objects."""
    if not head or not head.next:
        return head

    pre, slow, fast = None, head, head
    while fast and fast.next:
        pre, slow, fast = slow, slow.next, fast.next.next
    pre.next = None

    return merge(*map(sort_list, (head, slow)))


def compare_lists(l1: ListNode, l2: ListNode) -> bool:
    """Compare equality between two ListNode objects."""
    while l1:
        if l1.val != l2.val:
            return False
        l1 = l1.next
        l2 = l2.next
    return True


class TestSortList(unittest.TestCase):
    """Unit test for sort_list."""

    def test_1(self):
        ll = ListNode(4)
        ll.next = ListNode(2)
        ll.next.next = ListNode(1)
        ll.next.next.next = ListNode(3)

        out_ll = ListNode(1)
        out_ll.next = ListNode(2)
        out_ll.next.next = ListNode(3)
        out_ll.next.next.next = ListNode(4)

        self.assertEqual(compare_lists(sort_list(ll), out_ll), True)


if __name__ == '__main__':
    unittest.main()
