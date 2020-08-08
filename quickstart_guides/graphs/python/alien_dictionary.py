"""
Title: Alien dictionary

Problem:
    Given a sorted dictionary (array of words) of an alien language, find
    order of characters in the language.

Execution: python alien_dictionary.py
"""
from typing import List
import unittest
from collections import defaultdict


def alien_order(words: List[str]):
    """Find order of characters in alien language."""
    pre = defaultdict(set)
    suc = defaultdict(set)

    for pair in zip(words, words[1:]):
        for a, b in zip(*pair):
            if a != b:
                suc[a].add(b)
                pre[b].add(a)
                break
    chars = set("".join(words))
    char_to_process = chars - set(pre)
    order = ""
    while char_to_process:
        # Receiving first node in "char_to_process" and add to string.
        ch = char_to_process.pop()
        order += ch
        # For each character for whom our node is successor.
        for b in suc[ch]:
            pre[b].discard(ch)
            # In case node does not have successors, add to queue.
            if not pre[b]:
                char_to_process.add(b)
    # Check if all characters from alphabet have been covered.
    return order * (set(order) == chars)


class TestAlienDictionary(unittest.TestCase):
    """Unit tests for alien_dictionary."""

    def test_1(self):
        self.assertEqual(alien_order(["wrt", "ert"]), "rwte")

    def test_2(self):
        self.assertEqual(alien_order(["wrt", "wrf", "ert"]), "wrtef")


if __name__ == "__main__":
    unittest.main()
