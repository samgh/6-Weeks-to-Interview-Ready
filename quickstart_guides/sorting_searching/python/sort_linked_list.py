"""
Title: Sort linked list

Problem:
	Sort a linked list in O(n log n) time using constant space complexity.

Execution: python sort_linked_list.py
"""
from typing import List
import unittest


class Node:
    def __init__(self, data=None, nxt=None) -> None:
        self.data = data
        self.nxt = nxt


def print_list(node: Node) -> List[int]:
    ptr = node
    res = []
    while ptr:
        res.append(ptr.data)
        ptr = ptr.nxt
    return res


# Takes two lists sorted in increasing order, and merge their nodes
# together to make one big sorted list which is returned
def sorted_merge(a, b):

    # Base cases
    if a is None:
        return b
    elif b is None:
        return a

    # Pick either a or b, and recur
    if a.data <= b.data:
        result = a
        result.nxt = sorted_merge(a.nxt, b)
    else:
        result = b
        result.nxt = sorted_merge(a, b.nxt)

    return result


"""
Split the nodes of the given list into front and back halves,
If the length is odd, the extra node should go in the front list.
It uses the fast/slow pointer strategy
"""


def front_back_split(source):

    # if length is less than 2, handle separately
    if source is None or source.nxt is None:
        return source, None

    (slow, fast) = (source, source.nxt)

    # Advance 'fast' two nodes, and advance 'slow' one node
    while fast:

        fast = fast.nxt
        if fast:
            slow = slow.nxt
            fast = fast.nxt

    # 'slow' is before the midpoint the list, so split it in two
    # at that point.
    ret = (source, slow.nxt)
    slow.nxt = None

    return ret


# Sort given linked list using Merge sort algorithm
def merge_sort(head: Node):
    # Base case -- length 0 or 1
    if head is None or head.nxt is None:
        return head

    # Split head into 'a' and 'b' sublists
    front, back = front_back_split(head)

    # Recursively sort the sublists
    front = merge_sort(front)
    back = merge_sort(back)

    # answer = merge the two sorted lists together
    return sorted_merge(front, back)


class TestMergeSort(unittest.TestCase):
    """Unit test for MergeSort."""

    def test_1(self):
        # input keys
        keys = [8, 6, 4, 9, 3, 1]

        head = None
        for key in keys:
            head = Node(key, head)

        # sort the list
        head = merge_sort(head)

        # print the sorted list
        self.assertEqual(print_list(head), [1, 3, 4, 6, 8, 9])


if __name__ == "__main__":
    unittest.main()
