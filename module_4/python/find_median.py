"""
Title: Find median

Problem:
    Median is the middle value in an ordered integer list. If the size of the
    list is even, there is no middle value. So the median is the mean of the
    two middle value.

    For example, [2,3,4], the median is 3

    [2,3], the median is (2 + 3) / 2 = 2.5

    Design a data structure that supports the following two operations:

    void addNum(int num) - Add a integer number from the data stream to the
    data structure.  double findMedian() - Return the median of all elements so
    far.

Execution: python find_median.py
"""
import unittest


class FindMedian:
    def __init__(self) -> None:
        """Initialize median data structure."""
        self._store = []

    def add_num(self, num: int) -> None:
        """ Add number to median data structure."""
        self._store.append(num)

    def find_median(self) -> float:
        """Find median."""
        self._store.sort()
        n = len(self._store)
        if n & 1:
            return self._store[n//2]
        else:
            return (self._store[n//2 - 1] + self._store[n//2]) * 0.5
        

class TestFindMedian(unittest.TestCase):
    """Unit test for find_median."""

    def test_1(self):
        x = FindMedian()
        x.add_num(1)
        x.add_num(2)
        self.assertEqual(x.find_median(), 1.5)
        x.add_num(3)
        self.assertEqual(x.find_median(), 2)


if __name__ == '__main__':
    unittest.main()
