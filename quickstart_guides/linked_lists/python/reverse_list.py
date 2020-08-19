"""
Title: Reverse linked list.

Problem:
    Reverse a singly linked list.

Execution: python reverse_list.py
"""
import unittest


class ListNode:
    """Basic node class for linked list."""
    def __init__(self, x):
        self.val = x
        self.next = None


def reverse_list_iterative(head: ListNode) -> ListNode:
    """Function for iteratively reversing singly linked list."""
    prev = None
    curr = head

    while curr:
        next_temp = curr.next
        curr.next = prev
        prev = curr
        curr = next_temp
    return prev


def reverse_list_recursive(head: ListNode) -> ListNode:
    """Function for recursively reversing singly linked list."""
    if head is None or head.next is None:
        return head
    p = reverse_list_recursive(head.next)
    head.next.next = head
    head.next = None
    return p


def print_list(head: ListNode) -> list:
    """Print linked list elements."""
    output_list = []
    while head:
        output_list.append(head.val)
        head = head.next
    return output_list


class TestReverseList(unittest.TestCase):
    """Unit test for reverse list."""

    def test_1(self):
        """Test for 1->2->3->4->5."""
        input_1 = ListNode(1)
        input_1.next = ListNode(2)
        input_1.next.next = ListNode(3)
        input_1.next.next.next = ListNode(4)
        input_1.next.next.next.next = ListNode(5)

        list_output_iterative_1 = print_list(reverse_list_iterative(input_1))
        self.assertEqual(list_output_iterative_1, [5, 4, 3, 2, 1])


if __name__ == "__main__":
    unittest.main()
