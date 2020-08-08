"""
Title: Substring with Concatenation of All Words

Problem:
    You are given a string, s, and a list of words, words, that are all of the
    same length. Find all starting indices of substring(s) in s that is a
    concatenation of each word in words exactly once and without any intervening
    characters.

Execution: python substring_concat.py
"""
from typing import List, Optional
import collections
import unittest


def substring_concat(s: str, words: List[str]) -> Optional[List[int]]:
    """"Concatenate substring."""
    if not s or not words:
        return None
    word_len = len(words[0])
    window_len = len(words) * word_len
    str_len = len(s)
    word_dict, ret = collections.Counter(words), []
    for i in range(str_len - window_len + 1):
        new_dict = collections.defaultdict(int)

        for j in range(i, i + window_len, word_len):
            sub_word = s[j : j + word_len]

            if sub_word in word_dict:
                new_dict[sub_word] += 1
                if new_dict[sub_word] > word_dict[sub_word]:
                    break
            else:
                break
        if new_dict == word_dict:
            ret.append(i)
    return ret


class TestSubstringConcat(unittest.TestCase):
    """Unit tests for substring_concat."""

    def test_1(self):
        s = "barfoothefoobarman"
        words = ["foo", "bar"]
        expected_res = [0, 9]
        self.assertEqual(substring_concat(s, words), expected_res)

    def test_2(self):
        s = "wordgoodgoodgoodbestword"
        words = ["word", "good", "best", "word"]
        expected_res = []
        self.assertEqual(substring_concat(s, words), expected_res)


if __name__ == "__main__":
    unittest.main()
