"""
Title: Sliding puzzle

Problem:
    On a 2x3 board, there are 5 tiles represented by the integers 1 through 5,
    and an empty square represented by 0.

    A move consists of choosing 0 and a 4-directionally adjacent number and
    swapping it.

    The state of the board is solved if and only if the board is [[1,2,3],[4,5,0]].

    Given a puzzle board, return the least number of moves required so that the
    state of the board is solved. If it is impossible for the state of the board to
    be solved, return -1.

Execution: python sliding_puzzle.py
"""
import unittest
from typing import List


def swap(t, zero, target) -> tuple:
    """Simple swap function."""
    t = list(t)
    t[zero], t[target] = t[target], t[zero]
    return tuple(t)


def sliding_puzzle(board: List[List[int]]) -> int:
    """Sliding puzzle function."""
    board = tuple(board[0] + board[1])

    seen = set()
    q = [(board, 0)]

    while q:
        board, level = q.pop(0)
        if board == (1, 2, 3, 4, 5, 0):
            return level

        i = board.index(0)
        if i == 0:
            nexts = [swap(board, i, 1), swap(board, i, 3)]
        elif i == 2:
            nexts = [swap(board, i, 1), swap(board, i, 5)]
        elif i == 3:
            nexts = [swap(board, i, 0), swap(board, i, 4)]
        elif i == 5:
            nexts = [swap(board, i, 2), swap(board, i, 4)]
        elif i == 1:
            nexts = [swap(board, i, 0), swap(board, i, 2), swap(board, i, 4)]
        elif i == 4:
            nexts = [swap(board, i, 1), swap(board, i, 3), swap(board, i, 5)]
            
        for b in nexts:
            if b not in seen:
                seen.add(b)
                q.append((b, level+1))
    return -1


class TestSlidingPuzzle(unittest.TestCase):
    """Unit test for sliding_puzzle."""

    def test_1(self):
        board = [[1, 2, 3], [4, 0, 5]]
        self.assertEqual(sliding_puzzle(board), 1)
        print("Explanation: Swap the 0 and the 5 in one move.")

    def test_2(self):
        board = [[1, 2, 3], [5, 4, 0]]
        self.assertEqual(sliding_puzzle(board), -1)
        print("Explanation: No number of moves will make the board solved.")
        
    def test_3(self):
        board = [[4, 1, 2], [5, 0, 3]]
        self.assertEqual(sliding_puzzle(board), 5)
        print("Explanation: 5 is the smallest number of moves that solves the board.")

    def test_4(self):
        board = [[3, 2, 4], [1, 5, 0]]
        self.assertEqual(sliding_puzzle(board), 14)


if __name__ == '__main__':
    unittest.main()
