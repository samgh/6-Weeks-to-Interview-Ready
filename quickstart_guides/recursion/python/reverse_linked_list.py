"""
Title: Reverse linked list

Problem:
    Given a linked list, write a function that prints the nodes of the list in
    reverse order.

Execution: python reverse_linked_list.py
"""
import unittest


class Node:
    """Node class for linked list."""

    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class LinkedList:
    """Linked list class."""

    def __init__(self):
        self.head = None

    def append(self, data) -> None:
        """Append to end of linked list."""
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def reverse_recursive(self):
        def _reverse_recursive(cur, prev) -> Node:
            if not cur:
                return prev

            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            return _reverse_recursive(cur, prev)

        self.head = _reverse_recursive(cur=self.head, prev=None)


class TestReverseLinkedList(unittest.TestCase):
    """Unit tests for reverse_linked_list."""

    def test_1(self):
        llist = LinkedList()
        llist.append("A")
        llist.append("B")
        llist.append("C")
        llist.append("D")

        llist.reverse_recursive()

        res = []
        expected_res = ["D", "C", "B", "A"]
        cur_node = llist.head
        while cur_node:
            res.append(cur_node.data)
            cur_node = cur_node.next
        self.assertEqual(expected_res, res)

    def test_2(self):
        llist = LinkedList()
        llist.append(1)
        llist.append(2)
        llist.append(3)
        llist.append(4)

        llist.reverse_recursive()

        res = []
        expected_res = [4, 3, 2, 1]
        cur_node = llist.head
        while cur_node:
            res.append(cur_node.data)
            cur_node = cur_node.next
        self.assertEqual(expected_res, res)


if __name__ == "__main__":
    unittest.main()
