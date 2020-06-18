"""
Title: Find fixed point

Problem:
    A fixed point in an array "A" is an index "i" such that A[i] is equal to
    "i".  Given an array of n distinct integers sorted in ascending order,
    write a function that returns a "fixed point" in the array. If there is not
    a fixed point return "None".

Execution: python find_fixed_point.py
"""
import unittest


# Time Complexity: O(log n)
# Space Complexity: O(1)
def find_fixed_point(A):
    low = 0
    high = len(A) - 1

    while low <= high:
        mid = (low + high)//2

        if A[mid] < mid:
            low = mid + 1
        elif A[mid] > mid:
            high = mid - 1
        else:
            return A[mid]
    return None

class TestFindFixedPoint(unittest.TestCase):
    """Unit tests for find_fixed_point."""

    def test_1(self):
        A = [-10, -5, 0, 3, 7]
        self.assertEqual(find_fixed_point(A), 3)

    def test_2(self):
        A = [0, 2, 5, 8, 17]
        self.assertEqual(find_fixed_point(A), 0)

    def test_3(self):
        A = [-10, -5, 3, 4, 7, 9]
        self.assertEqual(find_fixed_point(A), None)


if __name__ == '__main__':
    unittest.main()
