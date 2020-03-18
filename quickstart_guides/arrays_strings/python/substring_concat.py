"""
Title: Substring with Concatenation of All Words

You are given a string, s, and a list of words, words, that are all of the same
length. Find all starting indices of substring(s) in s that is a concatenation
of each word in words exactly once and without any intervening characters.

Execution: python substring_concat.py
"""
from typing import List
import collections
import unittest


def substring_concat(s: str, words: List[str]) -> List[int]:
    if not s or not words:
        return None
    wordLen = len(words[0])
    windowLen = len(words)*wordLen
    strLen = len(s)
    wordDict, ret = collections.Counter(words), []
    for i in range(strLen - windowLen + 1):
        newDict = collections.defaultdict(int)
        for j in range(i, i + windowLen, wordLen):
            subWord = s[j: j + wordLen]
            if subWord in wordDict:
                newDict[subWord] += 1
                if newDict[subWord] > wordDict[subWord]:
                    break
            else:
                break
        if newDict == wordDict:
            ret.append(i)
    return ret


class TestSubstringConcat(unittest.TestCase):
    """Unit tests for substring_concat."""

    def test_1(self):
        s = "barfoothefoobarman"
        words = ["foo","bar"]
        expected_res = [0, 9]
        self.assertEqual(substring_concat(s, words), expected_res)

    def test_2(self):
        s = "wordgoodgoodgoodbestword"
        words = ["word", "good", "best", "word"]
        expected_res = []
        self.assertEqual(substring_concat(s, words), expected_res)


if __name__ == '__main__':
    unittest.main()
