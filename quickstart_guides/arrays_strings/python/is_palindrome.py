"""
Title: Is palindrome

Problem:
    Given a string, determine if it is a palindrome, considering only
    alphanumeric characters and ignoring cases.

    Note: For the purpose of this problem, we define empty string as valid
    palindrome.

Execution: python is_palindrome.py
"""
import string
import unittest


def is_palindrome(s: str) -> bool:
    s = s.lower().replace(" ", "").translate(str.maketrans("",
                                                           "",
                                                           string.punctuation))
    return True if s[::-1] == s else False


class TestIsPalindrome(unittest.TestCase):
    """Unit tests for is_palindrome."""

    def test_1(self):
        self.assertEqual(is_palindrome("A man, a plan, a canal: Panama"), True)

    def test_2(self):
        self.assertEqual(is_palindrome("race a car"), False)


if __name__ == "__main__":
    unittest.main()
