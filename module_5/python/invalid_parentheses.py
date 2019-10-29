"""
Title: Remove invalid parentheses

Problem:
    Remove the minimum number of invalid parentheses in order to make the input
    string valid. Return all possible results.

    Note: The input string may contain letters other than the parentheses ( and ).

Execution: python invalid_parentheses.py
"""
import unittest
from typing import List


class InvalidParens(object):

    def __init__(self):
        self.valid_expressions = None
        self.min_removed = None

    def reset(self):
        self.valid_expressions = set()
        self.min_removed = float("inf")

    """
        string: The original string we are recursing on.
        index: current index in the original string.
        left: number of left parentheses till now.
        right: number of right parentheses till now.
        ans: the resulting expression in this particular recursion.
        ignored: number of parentheses ignored in this particular recursion.
    """
    def remaining(self, 
                  string: str, 
                  index: int, 
                  left_count:int, 
                  right_count: int, 
                  expr: str, 
                  rem_count: int) -> str:
        # If we have reached the end of string.
        if index == len(string):

            # If the current expression is valid. The only scenario where it can be
            # invalid here is if left > right. The other way around we handled early on in the recursion.
            if left_count == right_count:

                if rem_count <= self.min_removed:
                    # This is the resulting expression.
                    # Strings are immutable in Python so we move around a list in the recursion
                    # and eventually join to get the final string.
                    possible_ans = "".join(expr)

                    # If the current count of brackets removed < current minimum, ignore
                    # previous answers and update the current minimum count.
                    if rem_count < self.min_removed:
                        self.valid_expressions = set()
                        self.min_removed = rem_count

                    self.valid_expressions.add(possible_ans)
        else:

            current_char = string[index]

            # If the current character is not a parenthesis, just recurse one step ahead.
            if current_char != '(' and  current_char != ')':
                expr.append(current_char)
                self.remaining(string, index + 1, left_count, right_count, expr, rem_count)
                expr.pop()
            else:
                # Else, one recursion is with ignoring the current character.
                # So, we increment the ignored counter and leave the left and right untouched.
                self.remaining(string, index + 1, left_count, right_count, expr, rem_count + 1)

                expr.append(current_char)

                # If the current parenthesis is an opening bracket, we consider it
                # and increment left and  move forward
                if string[index] == '(':
                    self.remaining(string, index + 1, left_count + 1, right_count, expr, rem_count)
                elif right_count < left_count:
                    # If the current parenthesis is a closing bracket, we consider it only if we
                    # have more number of opening brackets and increment right and move forward.
                    self.remaining(string, index + 1, left_count, right_count + 1, expr, rem_count)

                expr.pop()

    def remove_invalid_parentheses(self, s: str) -> List[str]:
        """
        :type s: str
        :rtype: List[str]
        """

        # Reset the class level variables that we use for every test case.
        self.reset()

        # Recursive call
        self.remaining(s, 0, 0, 0, [], 0)
        return list(self.valid_expressions)


class TestInvalidParentheses(unittest.TestCase):
    """Unit test for remove_invalid_parentheses."""

    def test_1(self):
        obj = InvalidParens()
        paren_input = "()())()"
        paren_output = ["(())()", "()()()"]
        self.assertEqual(obj.remove_invalid_parentheses(paren_input), paren_output)

    def test_2(self):
        obj = InvalidParens()
        paren_input = ")("
        paren_output = [""]
        self.assertEqual(obj.remove_invalid_parentheses(paren_input), paren_output)

if __name__ == '__main__':
    unittest.main()
