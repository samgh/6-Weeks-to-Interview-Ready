"""
Title: Word break problem.

Problem:
        Given a non-empty string s and a dictionary wordDict containing a list
        of non-empty words, determine if s can be segmented into a
        space-separated sequence of one or more dictionary words.

        Note: The same word in the dictionary may be reused multiple times in
        the segmentation.  You may assume the dictionary does not contain
        duplicate words.

Execution: python word_break.py
"""
import unittest
from typing import List


def word_break(s: str, word_dict: List[str]) -> bool:
    """Word break problem."""
    n = len(s)
    dp = [False for i in range(n+1)]
    dp[0] = True
    for i in range(1, n+1):
        for w in word_dict:
            if dp[i - len(w)] and s[i - len(w):i] == w:
                dp[i] = True
    return dp[-1]


class TestWordBreak(unittest.TestCase):
    """Unit test for word_break function."""

    def test_1(self):
        test_input_str = "leetcode"
        test_input_dict = ["leet", "code"]
        self.assertEqual(word_break(test_input_str, test_input_dict), True)
        print("Explanation: Return 'true' because 'leetcode' can be segmented"
              "as 'leet code'.")

    def test_2(self):
        test_input_str = "applepenapple"
        test_input_dict = ["apple", "pen"]
        self.assertEqual(word_break(test_input_str, test_input_dict), True)
        print("Explanation: Return true because 'applepenapple' can be"
                "segmented as 'apple pen apple'. Note that you are allowed to"
                "reuse a dictionary word.")

    def test_3(self):
        test_input_str = "catsandog"
        test_input_dict = ["cats", "dog", "sand", "and", "cat"]
        self.assertEqual(word_break(test_input_str, test_input_dict), False)


if __name__ == '__main__':
    unittest.main()
