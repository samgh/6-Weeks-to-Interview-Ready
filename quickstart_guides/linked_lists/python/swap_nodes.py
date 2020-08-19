"""
Title: Linked list swap nodes.

Problem:
    Swap nodes in a linked list.

Execution: python swap_nodes.py
"""
import unittest


class LinkedList(object):
    """Linked list class."""

    def __init__(self) -> None:
        self.head = None

    class Node(object):
        """Basic node class for linked list."""

        def __init__(self, d) -> None:
            self.data = d
            self.next = None

    def swap_nodes(self, x: int, y: int) -> None:
        """Swap two nodes in linked list."""
        # Nothing to do if x and y are same
        if x == y:
            return

        prev_x = None
        cur_x = self.head
        while cur_x and cur_x.data != x:
            prev_x = cur_x
            cur_x = cur_x.next

        prev_y = None
        cur_y = self.head
        while cur_y and cur_y.data != y:
            prev_y = cur_y
            cur_y = cur_y.next

        if cur_x is None or cur_y is None:
            return
        if prev_x:
            prev_x.next = cur_y
        else:
            self.head = cur_y

        if prev_y:
            prev_y.next = cur_x
        else:
            self.head = cur_x

        temp = cur_x.next
        cur_x.next = cur_y.next
        cur_y.next = temp

    def push(self, data):
        node = self.Node(data)
        node.next = self.head
        self.head = node


class TestSwapNodes(unittest.TestCase):
    """Unit test for swap_nodes."""

    def test_1(self):
        llist = LinkedList()

        llist.push(3)
        llist.push(2)
        llist.push(1)

        self.assertEqual(llist.head.data, 1)

        llist.swap_nodes(1, 2)

        self.assertEqual(llist.head.data, 2)

    def test_2(self):
        llist = LinkedList()

        llist.push(1)
        llist.push(2)
        llist.push(3)

        self.assertEqual(llist.head.data, 3)

        llist.swap_nodes(1, 3)

        self.assertEqual(llist.head.data, 1)


if __name__ == "__main__":
    unittest.main()
