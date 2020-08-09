"""
Title: Linked list nth to last

Problem:
    Obtain the nth-to-last node.

Execution: python nth_to_last.py
"""
import unittest


class Node:
    def __init__(self, data: str) -> None:
        self.data = data
        self.next = None


class LinkedList:
    """Linked list class."""

    def __init__(self) -> None:
        self.head = None

    def append(self, data: str) -> None:
        """Append node to list."""
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def len_iterative(self) -> int:
        """Calculate the length iteratively."""
        count = 0
        cur_node = self.head

        while cur_node:
            count += 1
            cur_node = cur_node.next
        return count

    def print_nth_from_last(self, n: int) -> None:
        """Print nth from last node."""
        # Method 1:
        total_len = self.len_iterative()

        cur = self.head
        while cur:
            if total_len == n:
                return cur.data
            total_len -= 1
            cur = cur.next
        if cur is None:
            return


class TestNthToLast(unittest.TestCase):
    """Unit test for nth_to_last."""

    def test_1(self):
        llist = LinkedList()
        llist.append("A")
        llist.append("B")
        llist.append("C")
        llist.append("D")

        self.assertEqual(llist.print_nth_from_last(2), "C")


if __name__ == "__main__":
    unittest.main()
