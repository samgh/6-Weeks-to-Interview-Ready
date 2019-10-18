"""
Title: Stack from queue.

Problem: Implement the stack datastructure using a queue.

Execution: python stack_from_queue.py
"""

import collections
import unittest


class Stack:
    """Stack using queue class."""

    def __init__(self):
        self._queue = collections.deque()

    def push(self, x):
        q = self._queue
        q.append(x)
        for _ in range(len(q) - 1):
            q.append(q.popleft())
    
    def pop(self):
        return self._queue.popleft()

    def top(self):
        return self._queue[0]

    def empty(self):
        return not len(self._queue)


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


if __name__ == '__main__':
    unittest.main()
