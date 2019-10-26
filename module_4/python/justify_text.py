"""
Title: Text justification

Problem:
    Given an array of words and a width maxWidth, format the text such that
    each line has exactly maxWidth characters and is fully (left and right)
    justified.

    You should pack your words in a greedy approach; that is, pack as many
    words as you can in each line. Pad extra spaces ' ' when necessary so that
    each line has exactly maxWidth characters.

    Extra spaces between words should be distributed as evenly as possible. If
    the number of spaces on a line do not divide evenly between words, the
    empty slots on the left will be assigned more spaces than the slots on the
    right.

    For the last line of text, it should be left justified and no extra space
    is inserted between words.

Execution: python justify_text.py
"""
import unittest
from typing import List


def justify_text(words: List[str], max_width: int) -> List[str]:
    res, cur, num_of_letters = [], [], 0
    for w in words:
        if num_of_letters + len(w) + len(cur) > max_width:
            for i in range(max_width - num_of_letters):
                cur[i % (len(cur)-1 or 1)] += ' '
            res.append(''.join(cur))
            cur, num_of_letters = [], 0
        cur += [w]
        num_of_letters += len(w)
    return res + [' '.join(cur).ljust(max_width)]


class TestJustifyText(unittest.TestCase):
    """Unit test for justify_text."""

    def test_1(self):
        words = ["This", "is", "an", "example", "of", "text", "justification."]
        max_width = 16
        expected_out = [
                "This    is    an",
                "example  of text",
                "justification.  "]
        self.assertEqual(justify_text(words, max_width), expected_out)

    def test_2(self):
        words = ["What","must","be","acknowledgment","shall","be"]
        max_width = 16
        expected_out = [
                  "What   must   be",
                  "acknowledgment  ",
                  "shall be        "]
        self.assertEqual(justify_text(words, max_width), expected_out)

    def test_3(self):
        words = ["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"]
        max_width = 20
        expected_out = [
                  "Science  is  what we",
                  "understand      well",
                  "enough to explain to",
                  "a  computer.  Art is",
                  "everything  else  we",
                  "do                  "]
        self.assertEqual(justify_text(words, max_width), expected_out)


if __name__ == '__main__':
    unittest.main()
