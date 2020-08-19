"""
Title: Reorder list.

Problem:
    Given a singly linked list L: L0→L1→…→Ln-1→Ln, reorder it to:
    L0→Ln→L1→Ln-1→L2→Ln-2→….

    You may not modify the values in the list's nodes, only nodes itself may be
    changed.

Execution: python reorder_list.py
"""
import unittest


class ListNode:
    """Basic node class for linked list."""

    def __init__(self, x):
        self.val = x
        self.next = None


def reorder_list(head: ListNode) -> None:
    """Reorder linked list."""
    if head is None:
        return None

    fast = slow = head
    # Slow will be the middle of the list
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    # Reverse list elements starting from the middle.
    pr, cur = slow, slow.next
    while cur:
        tmp = cur.next
        cur.next, pr = pr, cur
        cur = tmp

    tail = pr
    # Walk from head and tail towards the middle of the list and merge
    # {0: n}, {1: (n-1)} ... { k: (n-k)}
    while tail != slow:
        tmp = tail.next
        tail.next = head.next
        head.next = tail
        head = tail.next
        tail = tmp

    slow.next = None


class TestReverseList(unittest.TestCase):
    """Unit test for reverse list."""

    def test_1(self):
        """Test for 1->2->3->4->5."""
        input_1 = ListNode(1)
        input_1.next = ListNode(2)
        input_1.next.next = ListNode(3)
        input_1.next.next.next = ListNode(4)
        input_1.next.next.next.next = ListNode(5)

        reorder_list(input_1)


if __name__ == "__main__":
    unittest.main()
