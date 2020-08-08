"""
Title: Calculate the Hamming distance.

Problem: 
    The Hamming distance between two integers is the number of positions
    at which the corresponding bits are different.

    Now your job is to find the total Hamming distance between all pairs of the
    given numbers.

Execution: python hamming_distance.py
"""
from typing import List
import unittest


def hamming_distance(nums: List[int]) -> int:
    """Function for calculating the Hamming distance."""
    res = 0
    while nums != [0] * len(nums):
        c = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                c += 1
            nums[i] = (nums[i] - nums[i] % 2) // 2
        res += c * (len(nums) - c)
    return res


class TestHammingDistance(unittest.TestCase):
    """Unit test for hamming_distance."""

    def test_1(self):
        input_list = [4, 14, 2]
        self.assertEqual(hamming_distance(input_list), 6)
        output = """
        In binary representation, the 4 is 0100, 14 is 1110, and 2 is 0010
        (just showing the four bits relevant in this case). So the answer will
        be: HammingDistance(4, 14) + HammingDistance(4, 2) +
        HammingDistance(14, 2) = 2 + 2 + 2 = 6.
        """
        print(f"Explanation: {output}")


if __name__ == "__main__":
    unittest.main()
