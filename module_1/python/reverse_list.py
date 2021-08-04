"""
Title: Reverse Linked List
Leetcode Link: https://leetcode.com/problems/reverse-linked-list/

Problem: Given a singly linked list, reverse the list.

Input:
    ListNode head   => The head of the linked list
Output:
    ListNode        => The head of the reversed list

Execution: python reverse_list.py
"""
import unittest

# Basic node class
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

"""
Solution #1: Brute Force

In this solution, we add all the nodes to an builtin list, allowing us to easily
maintain order while swapping pointers.

This is not recommended and for demonstrative purposes only.

Time Complexity: O(n)
Space Complexity: O(n)
"""
def reverse_list_bf(head: ListNode) -> ListNode:
    if not head:
        return head
    # Create an list that contains references to all the list nodes
    nodes = []
    curr = head
    while curr:
        nodes.append(curr)
        curr = curr.next

    # Reverse pointers
    nodes[0].next = None
    for i in range(1, len(nodes)):
        nodes[i].next = nodes[i-1]

    return nodes[-1]

"""
Solution #2: Iterative

Iterate over all the nodes and reverse pointers as we go

Time Complexity: O(n)
Space Complexity: O(1)
"""
def reverse_list_iter(head: ListNode) -> ListNode:
    prev = None
    curr = head

    # Iterate over the list and swap pointers as we go
    while curr:
        next_temp = curr.next
        curr.next = prev
        prev = curr
        curr = next_temp
    return prev

"""
Solution #3: Recursive

Recursively reverse the remainder of the list and point current node to the
previous

Time Complexity: O(n)
Space Complexity: O(n)
"""
def reverse_list_rec(head: ListNode) -> ListNode:
    # If we're at the end of the list, just return head
    if head is None or head.next is None:
        return head

    # Reverse the list from head.next to the end
    rem = reverse_list_rec(head.next)

    # Point the last node of that reversed list to the current node
    head.next.next = head
    head.next = None
    return rem

class TestReverseList(unittest.TestCase):
    """Unit test for reverse list."""

    def test_1(self):
        """Test for 1->2->3->4->5."""
        input_1 = ListNode(1)
        input_1.next = ListNode(2)
        input_1.next.next = ListNode(3)
        input_1.next.next.next = ListNode(4)
        input_1.next.next.next.next = ListNode(5)

        output_1 = reverse_list_rec(input_1)
        l = []
        while output_1:
            l.append(output_1.val)
            output_1 = output_1.next

        self.assertEqual(l, [5, 4, 3, 2, 1])

    # ADD YOUR TESTS HERE

if __name__ == '__main__':
    unittest.main()
