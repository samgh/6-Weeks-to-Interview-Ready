"""
Title: Find substring

Problem:
    You are given a string, s, and a list of words, words, that are all of the
    same length. Find all starting indices of substring(s) in s that is a
    concatenation of each word in words exactly once and without any
    intervening characters.

Execution: python find_substring.py
"""
from collections import Counter
from typing import List
import unittest


def find_substring(s: str, words: List[str]) -> List[int]:
    if not words or not s:
        return []

    wordlen, nwords = len(words[0]), len(words)
    indices = []

    # iterative over `wordlen` times
    for i in range(wordlen):
        counter = Counter(words)
                    # start index of sliding window left and right pointer
        l = r = i
        while r + wordlen <= len(s):
            # remove the substring from the counter
            counter[s[r:r+wordlen]] -= 1
            r += wordlen
            # move left pointer one word offset to the right once the window size exceeds
            if r - l > wordlen * nwords:
                counter[s[l:l+wordlen]] += 1
                l += wordlen
            # if the window size is what we want and we found that all values in counter are 0
            # we can make sure that the substring in this window is one of the answer
            # we are looking for
            if r - l == wordlen * nwords and all(count == 0 for count in counter.values()):
                indices.append(l)

    return indices

class TestFindSubstring(unittest.TestCase):
    """Unit tests for find_substring."""

    def test_1(self):
        self.assertEqual(find_substring("barfoothefoobarman", ["foo", "bar"]), [0, 9])

    def test_2(self):
        self.assertEqual(find_substring("wordgoodgoodgoodbestword", ["word", "good", "best", "word"]), [])


if __name__ == '__main__':
    unittest.main()
