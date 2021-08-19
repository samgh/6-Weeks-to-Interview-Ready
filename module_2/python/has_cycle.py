"""
Title: Has Cycle
Leetcode Link: https://leetcode.com/problems/linked-list-cycle/

Problem: Given a linked list, determine if it contains a cycle.

Input:
  Node n  => List head
Output:
  bool => True if the list contains a cycle

Execution: python has_cycle.py
"""
import unittest

"""
Simple Node class
"""
class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

"""
Solution #1: Using extra memory

We'll store all the nodes into a set. Then for each node we visit
we check whether we've already visited that node.

Time Complexity: O(n)
Space Complexity: O(n)
"""
def has_cycle_extra_space(n: Node) -> bool:
    # Set to store nodes we've already visited
    visited = set()

    # Keep looping until we get to the end of the list or see a node
    # we've already seen
    while n:
        if n in visited:
            return True
        visited.add(n)
        n = n.next

    # If we get here it means we reached the end of the list (no cycle)
    return False

"""
Solution #2: No extra memory

In this algorithm we use 2 pointers moving at different speeds. If there
is a cycle, the fast pointer should catch up to the slow pointer.
Otherwise, if the fast pointer reaches the end, there's no cycle

Time Complexity: O(n)
Space Complexity: O(1)
"""
def has_cycle(n: Node) -> bool:
    if not n:
        return False

    fast = n.next
    slow = n

    # Keep looping through and check if the fast and slow pointers overlap
    while fast and fast.next:
        if fast == slow:
            return True

        # Fast pointer moves 2x each loop, slow moves 1x
        fast = fast.next.next
        slow = slow.next

    return False



class TestHasCycle(unittest.TestCase):
    """Unit test for has cycle function."""

    def test_1(self):
        list = Node()
        list.next = Node()
        list.next.next = Node()

        self.assertEqual(has_cycle(list), False)

        list.next.next.next = list

        self.assertEqual(has_cycle(list), True)

    # ADD YOUR TESTS HERE

if __name__ == '__main__':
    unittest.main()
