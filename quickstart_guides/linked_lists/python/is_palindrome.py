"""
Title: Linked list is palindrome

Problem:
    Check if linked list has nodes that consist of palindrome.

Execution: python is_palindrome.py
"""
import unittest


class ListNode:
    """Class for Linked List node."""

    def __init__(self, x: int) -> None:
        self.val = x
        self.next = None


def is_palindrome(head: ListNode) -> bool:
    """Check if linked list is palindrome."""
    vals = []
    curr = head
    while curr:
        vals.append(curr.val)
        curr = curr.next

    while head:
        if head.val != vals.pop():
            return False
        head = head.next
    return True


class TestIsPalindrome(unittest.TestCase):
    """Unit test for is_palindrome."""

    def test_1(self):
        list_1 = ListNode(1)
        list_1.next = ListNode(2)

        self.assertEqual(is_palindrome(list_1), False)

    def test_2(self):
        list_2 = ListNode(1)
        list_2.next = ListNode(2)
        list_2.next.next = ListNode(2)
        list_2.next.next.next = ListNode(1)

        self.assertEqual(is_palindrome(list_2), True)


if __name__ == "__main__":
    unittest.main()
