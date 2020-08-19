"""
Title: Set n^th bit

Problem: 
    Write a program  that takes an integer and sets the n-th bit in the binary
    representation of that integer

    For instance, the binary representation of 6 is:

    ```
    110
    ```

    The least significant bit is the bit on the far right of the binary
    representation and the most significant bit is the bit on the far left. We
    order the bits as

    ```
    b2, b1, b0
    1   1   0
    ```

    For our function, if we set the 0th bit, we should obtain the binary
    representation:

    ```
    1 1 1
    ```

Execution: python set_nth_bit.py
"""
import unittest


def set_nth_bit(x: int, n: int) -> int:
    """Set the nth bit of an integer."""
    return x | 1 << n


class TestSetNthBit(unittest.TestCase):
    """Unit test for set_nth_bit."""

    def test_1(self):
        self.assertEqual(set_nth_bit(6, 0), 7)


if __name__ == "__main__":
    unittest.main()
