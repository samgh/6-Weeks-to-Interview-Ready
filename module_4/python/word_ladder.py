"""
Title: Word ladder II

Problem:
    Given two words (beginWord and endWord), and a dictionary's word list,
    find all shortest transformation sequence(s) from beginWord to endWord, such
    that:

    Only one letter can be changed at a time Each transformed word must exist in
    the word list. Note that beginWord is not a transformed word.  Note:

    Return an empty list if there is no such transformation sequence.  All words
    have the same length.  All words contain only lowercase alphabetic characters.
    You may assume no duplicates in the word list.  You may assume beginWord and
    endWord are non-empty and are not the same.

Execution: python word_ladder.py
"""
import collections
import unittest
from typing import List

def word_ladder(beginWord, endWord, wordList):
    """
    :type beginWord: str
    :type endWord: str
    :type wordList: List[str]
    :rtype: List[List[str]]
    """
    def dfs(word):
        if word == endWord:
            res.append(list(tmp))
            return
        if word in graph:
            for nei in graph[word]:
                if dist[nei] == dist[word]-1:
                    tmp.append(nei)
                    dfs(nei)
                    tmp.pop()

    wordSet = set(wordList)
    if endWord not in wordSet:
        return []
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    q = collections.deque([(endWord, 0)])
    min_dist = float('inf')
    seen = set([endWord])
    graph = collections.defaultdict(set)
    dist = {}
    while q:
        u, d = q.popleft()
        dist[u] = d
        for i in range(len(u)):
            for alph in alphabets:
                new = u[:i]+alph+u[i+1:]
                if new == beginWord:
                    if min_dist > d+1:
                        min_dist = d+1
                    graph[beginWord].add(u)
                else:
                    if new in wordSet:
                        graph[u].add(new)
                        graph[new].add(u)
                        if new not in seen:
                            seen.add(new)
                            q.append((new, d+1))

    if min_dist == float('inf'):
        return []
    res = []
    tmp = [beginWord]
    for nei in graph[beginWord]:
        if dist[nei] == min_dist-1:
            tmp.append(nei)
            dfs(nei)
            tmp.pop()
    return res


class TestWordLadder(unittest.TestCase):
    """Unit test for word_ladder."""

    def test_1(self):
        begin_word = "hit"
        end_word = "cog"
        word_list = ["hot", "dot", "dog" "lot", "log"]

        expected_out = []
        self.assertEqual(word_ladder(begin_word, end_word, word_list), expected_out)


if __name__ == '__main__':
    unittest.main()
