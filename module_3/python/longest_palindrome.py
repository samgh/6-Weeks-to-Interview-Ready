"""
Title: Longest palindrome

Problem:
    Given a string s, find the longest palindromic substring in s. You may
    assume that the maximum length of s is 1000.

Execution: python longest_palindrome.py
"""
import unittest


def longest_palindrome(s: str):
    """Function for calculating longest palindrome."""
    res = ""
    curr_length = 0
    for i in range(len(s)):
        if is_palindrome(s, i-curr_length-1, i):
            res = s[i-curr_length-1:i+1]
            curr_length = curr_length + 2
        elif is_palindrome(s, i-curr_length, i):
            res = s[i-curr_length:i+1]
            curr_length = curr_length + 1
    return res


def is_palindrome(s: str, begin: int, end: int):
    """Helper function to check if string is palindrome."""
    if begin < 0:
        return False
    while begin < end:
        if s[begin] != s[end]:
            return False
        begin += 1
        end -= 1
    return True


class TestLongestPalindrome(unittest.TestCase):
    """Unit test for longest palindrome."""

    def test_1(self):
        """Test for longest palindrome."""
        test_palindrome = "babad"
        self.assertEqual(longest_palindrome(test_palindrome), "bab")
        print("Explanation: 'aba' is also a valid answer.")

    def test_2(self):
        """Test for longest palindrome."""
        test_palindrome = "cbbd"
        self.assertEqual(longest_palindrome(test_palindrome), "bb")


if __name__ == '__main__':
    unittest.main()
