"""
Title: Search In Rotated Array
Leetcode Link: https://leetcode.com/problems/search-in-rotated-sorted-array/

Problem: Given a a sorted array that is rotated around some unknown pivot point,
write a function to find the index of a target value.
(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2])

You can assume the array contains no duplicates.

   Input:
      List[int] nums    => The array to search in
      int target        => The value to search for
   Output:
      int               => The index of target. Return -1 if not found

Execution: python search_rotated_array.py
"""
import unittest
from typing import List

"""
Perform a modified binary search. In addition to considering whether the value
is to the left or the right of the midpoint, we also have to consider whether
the pivot point is to the left or righ.

Time Complexity: O(log n)
Space Complexity: O(1)
"""
def search_rotated_array(nums: List[int], target: int)->int:
    # The bounds of our current sublist
    low, high = 0, len(nums)-1

    # Keep dividing subarray in half until we either find the value we're
    # looking for or the subarray length is 0 (aka low >= high)
    while low <= high:
        # The midpoint of our sublist
        mid = (low + high) // 2

        # If we've found the value, return the index
        if target == nums[mid]:
            return mid

        # If the target < nums[mid], we have 3 possible options:
        # 1. Left sublist contains pivot. This means all values lower than
        # nums[mid] are in the left sublist
        # 2. target >= nums[low]. This means target is in left sublist
        # 3. target < nums[low]. This means there could be a pivot in the
        # right sublist so if our target is in the list it must be there
        if target < nums[mid]:
            # A sublist must contain pivot if nums[low] > nums[high]
            if nums[low] > nums[mid] or target >= nums[low]:
                high = mid-1
            else:
                low = mid+1
        else:
            # If target > nums[mid] we just do the opposite of above
            if nums[mid] > nums[high] or target <= nums[high]:
                low = mid+1
            else:
                high = mid-1

    return -1


class TestSearchRotatedArray(unittest.TestCase):
    """Unit test for SearchRotatedArray."""

    def test_1(self):
        """Test for: Input: nums = [4,5,6,7,0,1,2], target = 0 Output: 4."""
        self.assertEqual(
                search_rotated_array(
                    nums=[4, 5, 6, 7, 0, 1, 2],
                    target=0
                ), 4)

    def test_2(self):
        """Test for: Input: nums = [4,5,6,7,0,1,2], target = 3 Output: -1."""
        self.assertEqual(
                search_rotated_array(
                    nums=[4, 5, 6, 7, 0, 1, 2],
                    target=3
                ), -1)

    # ADD YOUR TESTS HERE

if __name__ == '__main__':
    unittest.main()
