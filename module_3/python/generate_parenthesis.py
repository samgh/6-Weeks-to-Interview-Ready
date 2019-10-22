"""
Title: Generate parenthesis

Problem:
    Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
    For example, given n = 3, a solution set is:
        [
          "((()))",
          "(()())",
          "(())()",
          "()(())",
          "()()()"
        ]

Execution: python generate_parenthesis.py
"""
import unittest
from typing import List


def generate_parenthesis_brute_force(n: int) -> List[str]:
    """Brute-force generate parenthesis."""
    def generate(A=[]):
        if len(A) == 2*n:
            if valid(A):
                ans.append("".join(A))
        else:
            A.append('(')
            generate(A)
            A.pop()
            A.append(')')
            generate(A)
            A.pop()

    def valid(A):
        bal = 0
        for c in A:
            if c == '(': bal += 1
            else: bal -= 1
            if bal < 0: return False
        return bal == 0

    ans = []
    generate()

    return ans


def generate_parenthesis_backtracking(n: int) -> List[str]:
    """Backtracking generate parenthesis."""
    ans = []

    def backtrack(S: str = "", left: int = 0, right: int = 0):
        if len(S) == 2 * n:
            ans.append(S)
            return
        if left < n:
            backtrack(S+'(', left+1, right)
        if right < left:
            backtrack(S+')', left, right+1)

    backtrack()
    return ans


class TestGenerateParenthesis(unittest.TestCase):
    """Unit test for generate_parenthesis."""

    def test_1(self):
        """Test for input shown below."""
        test_output = [
            "((()))",
            "(()())",
            "(())()",
            "()(())",
            "()()()"]
        self.assertEqual(generate_parenthesis_brute_force(3), test_output)
        self.assertEqual(generate_parenthesis_backtracking(3), test_output)


if __name__ == '__main__':
    unittest.main()
