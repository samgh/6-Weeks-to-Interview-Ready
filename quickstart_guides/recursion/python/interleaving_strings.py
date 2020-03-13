"""
Title: Check interleaving strings.
    
    Check whether a string interleaves with two other strings.

Execution: python interleaving_strings.py
"""
from typing import List
import unittest


def is_interleaved(A: str, B: str, C: str):
    """
    Returns "True" if the string "C" is an interleaving string of "A" and "B"
    and returns "False" otherwise.
    """

    # Find lengths of the two strings.
    M, N = len(A), len(B)

    # Let us create a 2D table to store solutions of subproblems. C[i][j] will
    # be true if C[0..i+j-1]  is an interleaving of A[0..i-1] and B[0..j-1].
    # Initialize all values as false.
    IL = [[False] * (N + 1) for i in range(M + 1)]

    # C can be an interleaving of A and B only of sum of lengths of A & B is
    # equal to length of C.
    if M + N != len(C):
        return False

    # Process all characters of A and B
    for i in range(M + 1):
        for j in range(N + 1):

            # Two empty strings have an empty string as interleaving.
            if i == 0 and j == 0:
                IL[i][j] = True

            # A is empty.
            elif i == 0:
                if B[j - 1] == C[j - 1]:
                    IL[i][j] = IL[i][j - 1]

            # B is empty.
            elif j == 0:
                if (A[i - 1] == C[i - 1]):
                    IL[i][j] = IL[i - 1][j]

            # Current character of C matches with  current character of A, but
            # doesn't match  with current character of B.
            elif A[i - 1] == C[i + j - 1] and B[j - 1] != C[i + j - 1]:
                IL[i][j] = IL[i - 1][j]

            # Current character of C matches with  current character of B, but
            # doesn't match  with current character of A.
            elif A[i - 1] != C[i + j - 1] and B[j - 1] == C[i + j - 1]:
                IL[i][j] = IL[i][j - 1]

            # Current character of C matches with  that of both A and B.
            elif A[i - 1] == C[i + j - 1] and B[j - 1] == C[i + j - 1]:
                IL[i][j] = (IL[i - 1][j] or IL[i][j - 1])

    return IL[M][N]


class TestInterleavingStrings(unittest.TestCase):
    """Unit tests for interleaving_strings."""

    def test_1(self):
        self.assertEqual(is_interleaved("XXY", "XXZ", "XXZXXXY"), False)

    def test_2(self):
        self.assertEqual(is_interleaved("XY", "WZ", "WZXY"), True)

    def test_3(self):
        self.assertEqual(is_interleaved("YX", "X", "XXY"), False)

    def test_4(self):
        self.assertEqual(is_interleaved("XXY", "XXZ", "XXXXZY"), True)


if __name__ == '__main__':
    unittest.main()

