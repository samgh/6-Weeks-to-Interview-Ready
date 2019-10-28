"""
Title: K-closest

Problem:
    We have a list of points on the plane.  Find the K closest points to the
    origin (0, 0).

    (Here, the distance between two points on a plane is the Euclidean distance.)

    You may return the answer in any order.  The answer is guaranteed to be unique
    (except for the order that it is in.)

Execution: python k_closest.py
"""
import random
import unittest
from typing import List


def k_closest_brute_force(points: List[List[int]], K: int) -> List[List[int]]:
    """Brute-force implementation of k-closest."""
    points.sort(key = lambda P: P[0]**2 + P[1]**2)
    return points[:K]


def k_closest_divide_conquer(points: List[List[int]], K: int) -> List[List[int]]:
    dist = lambda i: points[i][0]**2 + points[i][1]**2

    def sort(i: int, j: int, K: int) -> List[List[int]]:
        if i >= j:
            return

        k = random.randint(i, j)
        points[i], points[k] = points[k], points[i]

        mid = partition(i, j)
        if K < mid - i + 1:
            sort(i, mid - 1, K)
        elif K > mid - i + 1:
            sort(mid + 1, j, K - (mid - i + 1))

    def partition(i: int, j: int) -> int:
        oi = i
        pivot = dist(i)
        i += 1

        while True:
            while i < j and dist(i) < pivot:
                i += 1
            while i <= j and dist(j) >= pivot:
                j -= 1
            if i >= j:
                break
            points[i], points[j] = points[j], points[i]
        points[oi], points[j] = points[j], points[oi]
        return j

    sort(0, len(points) - 1, K)
    return points[:K]


class TestKClosest(unittest.TestCase):
    """Unit test for k_closest problem."""

    def test_1(self):
        """
        The distance between (1, 3) and the origin is sqrt(10).  The distance
        between (-2, 2) and the origin is sqrt(8).  Since sqrt(8) < sqrt(10),
        (-2, 2) is closer to the origin.  We only want the closest K = 1 points
        from the origin, so the answer is just [[-2,2]].
        """
        points = [[1, 3], [-2, 2]]
        K = 1
        expected_out = [[-2, 2]]
        self.assertEqual(k_closest_brute_force(points, K), expected_out)
        self.assertEqual(k_closest_divide_conquer(points, K), expected_out)

    def test_2(self):
        """The answer [[-2,4],[3,3]] would also be accepted."""
        points = [[3, 3], [5, -1], [-2, 4]]
        K = 2
        expected_out = [[3, 3], [-2, 4]]
        self.assertEqual(k_closest_brute_force(points, K), expected_out)
        self.assertEqual(k_closest_divide_conquer(points, K), expected_out)


if __name__ == '__main__':
    unittest.main()
