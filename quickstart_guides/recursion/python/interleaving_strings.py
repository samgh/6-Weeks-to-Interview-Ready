"""
Title: Check interleaving strings.

Problem:
    Check whether a string interleaves with two other strings.

Execution: python interleaving_strings.py
"""
import unittest


def is_interleaved(str_a: str, str_b: str, str_c: str):
    """
    Returns "True" if the string "C" is an interleaving string of "A" and "B"
    and returns "False" otherwise.
    """

    # Find lengths of the two strings.
    m, n = len(str_a), len(str_b)

    # Let us create a 2D table to store solutions of subproblems. C[i][j] will
    # be true if C[0..i+j-1]  is an interleaving of A[0..i-1] and B[0..j-1].
    # Initialize all values as false.
    IL = [[False] * (n + 1) for i in range(m + 1)]

    # C can be an interleaving of A and B only of sum of lengths of A & B is
    # equal to length of C.
    if m + n != len(str_c):
        return False

    # Process all characters of A and B
    for i in range(m + 1):
        for j in range(n + 1):

            # Two empty strings have an empty string as interleaving.
            if i == 0 and j == 0:
                IL[i][j] = True

            # A is empty.
            elif i == 0:
                if str_b[j - 1] == str_c[j - 1]:
                    IL[i][j] = IL[i][j - 1]

            # B is empty.
            elif j == 0:
                if str_a[i - 1] == str_c[i - 1]:
                    IL[i][j] = IL[i - 1][j]

            # Current character of C matches with  current character of A, but
            # doesn't match  with current character of B.
            elif str_a[i - 1] == str_c[i + j - 1] and str_b[j - 1] != str_c[i + j - 1]:
                IL[i][j] = IL[i - 1][j]

            # Current character of C matches with  current character of B, but
            # doesn't match  with current character of A.
            elif str_a[i - 1] != str_c[i + j - 1] and str_b[j - 1] == str_c[i + j - 1]:
                IL[i][j] = IL[i][j - 1]

            # Current character of C matches with  that of both A and B.
            elif str_a[i - 1] == str_c[i + j - 1] and str_b[j - 1] == str_c[i + j - 1]:
                IL[i][j] = IL[i - 1][j] or IL[i][j - 1]

    return IL[m][n]


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


if __name__ == "__main__":
    unittest.main()
