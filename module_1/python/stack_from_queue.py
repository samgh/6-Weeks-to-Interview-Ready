"""
Title: Stack from Queues
Leetcode Link: https://leetcode.com/problems/implement-stack-using-queues/

Problem: Implement a LIFO stack with basic operations using 2 FIFO queues.

Execution: python stack_from_queue.py
"""

import collections
import unittest

class Stack:

    """
    Constructor
    """
    def __init__(self):
        self._queue = []

    """
    Push an item onto the stack
    """
    def push(self, x:int)->None:
        # We are going to just create a new queue here so we're using 2 queues
        # _at a time_. If we want to be more precise, we could allocate two
        # queues at the beginning and just alternate between which we're using
        # as the primary and secondary queues
        new_queue = []
        new_queue.append(x)
        for i in self._queue:
            new_queue.append(i)

        self._queue = new_queue

    """
    Remove the most recently added element from the stack
    """
    def pop(self)->int:
        # We've handled all the logic while pushing so this is easy
        return self._queue.pop(0)

    """
    Return the top element of stack without removing it
    """
    def top(self):
        return self._queue[0]

    """
    Return true if stack is empty
    """
    def empty(self):
        return len(self._queue) == 0

class TestStackFromQueue(unittest.TestCase):
    """Unit test for Stack from Queue."""

    def test_1(self):
        """Test for stack from queue."""
        s = Stack()

        self.assertEqual(s.empty(), True)
        print("Explanation: Stack is initially empty.")

        s.push(1)
        s.push(2)
        s.push(3)

        self.assertEqual(s.top(), 3)
        print("Explanation: Check the top of stack.")

        self.assertEqual(s.empty(), False)
        print("Explanation: Stack has elements and is not empty.")

    # ADD YOUR TEST CASES HERE

if __name__ == '__main__':
    unittest.main()
