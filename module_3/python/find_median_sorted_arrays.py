"""
Title: Find median sorted arrays.

Problem: 
    There are two sorted arrays nums1 and nums2 of size m and n
    respectively.

    Find the median of the two sorted arrays. The overall run time complexity
    should be O(log (m+n)).

    You may assume nums1 and nums2 cannot be both empty.

Execution: python find_median_sorted_arrays.py
"""
import unittest
from typing import List


def find_median_sorted_arrays(nums1: List[int], nums2: List[int]) -> float:
    """Function for ."""
    m, n = len(nums1), len(nums2)
    if m > n:
        nums1, nums2, m, n = nums2, nums1, n, m
    if n == 0:
        raise ValueError

    imin, imax, half_len = 0, m, (m + n + 1) // 2
    while imin <= imax:
        i = (imin + imax) // 2
        j = half_len - i
        if i < m and nums2[j-1] > nums1[i]:
            # i is too small, must increase it
            imin = i + 1
        elif i > 0 and nums1[i-1] > nums2[j]:
            # i is too big, must decrease it
            imax = i - 1
        else:
            # i is perfect
            if i == 0:
                max_of_left = nums2[j-1]
            elif j == 0:
                max_of_left = nums1[i-1]
            else:
                max_of_left = max(nums1[i-1], nums2[j-1])

            if (m + n) % 2 == 1:
                return max_of_left

            if i == m:
                min_of_right = nums2[j]
            elif j == n:
                min_of_right = nums1[i]
            else:
                min_of_right = min(nums1[i], nums2[j])

            return (max_of_left + min_of_right) / 2.0


class TestFindMedianSortedArrays(unittest.TestCase):
    """Unit test for find_median_sorted_arrays"""

    def test_1(self):
        nums1 = [1, 3]
        nums2 = [2]
        self.assertEqual(find_median_sorted_arrays(nums1, nums2), 2.0)
        print("Explanation: The median is 2.0.")

    def test_2(self):
        nums1 = [1, 2]
        nums2 = [3, 4]
        self.assertEqual(find_median_sorted_arrays(nums1, nums2), 2.5)
        print("Explanation: The median is (2 + 3)/2 = 2.5")


if __name__ == '__main__':
    unittest.main()
