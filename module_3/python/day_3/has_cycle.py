"""
Title: Does linked list have cycle.

Problem:
        Given a linked list, determine if it has a cycle in it.

        To represent a cycle in the given linked list, we use an integer pos which
        represents the position (0-indexed) in the linked list where tail connects to.
        If pos is -1, then there is no cycle in the linked list.

Execution: python has_cycle.py
"""
import unittest


class Node:
    """Node class for LinkedList."""

    def __init__(self, data):
        """Set the data for node."""
        self.data = data
        self.next = None


class LinkedList:
    """Linked list class."""

    def __init__(self): 
        """Initialize head of list."""
        self.head = None

    def append(self, new_data): 
        """Insert a new node at the beginning."""
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        """Print the linked LinkedList."""
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

    def detect_loop(self):
        """Check if LinkedList has loop."""
        s = set()
        temp = self.head
        while (temp):
            # If we have already has this node in hashmap it
            # means their is a cycle (Because you we encountering
            # the node second time).
            if (temp in s):
                return True

            # If we are seeing the node for
            # the first time, insert it in hash
            s.add(temp)
            temp = temp.next

        return False


class TestHasCycle(unittest.TestCase):
    """Unit test for has cycle function."""

    def test_1(self):
        ll = LinkedList()
        ll.append(20)
        ll.append(4)
        ll.append(15)
        ll.append(10)
        ll.head.next.next.next.next = ll.head
        self.assertEqual(ll.detect_loop(), True)


if __name__ == '__main__':
    unittest.main()
