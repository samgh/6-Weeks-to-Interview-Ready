"""
Title: Basic calculator

Problem:
    Implement a basic calculator to evaluate a simple expression string.

    The expression string may contain open ( and closing parentheses ), the 
    plus + or minus sign -, non-negative integers and empty spaces .

Execution: python calculate.py
"""
import unittest


def evaluate_expr(stack):
    """Evaluate expression as stack."""
    res = stack.pop() if stack else 0
    # Evaluate the expression till we get corresponding ')'
    while stack and stack[-1] != ')':
        sign = stack.pop()
        if sign == '+':
            res += stack.pop()
        else:
            res -= stack.pop()
    return res


def calculate(s: str) -> int:
    """Interpret string and calculate."""
    stack = []
    n, operand = 0, 0

    for i in range(len(s) - 1, -1, -1):
        ch = s[i]

        if ch.isdigit():

            # Forming the operand - in reverse order.
            operand = (10**n * int(ch)) + operand
            n += 1

        elif ch != " ":
            if n:
                # Save the operand on the stack
                # As we encounter some non-digit.
                stack.append(operand)
                n, operand = 0, 0

            if ch == '(':
                res = evaluate_expr(stack)
                stack.pop()

                # Append the evaluated result to the stack.  This result could
                # be of a sub-expression within the parenthesis.
                stack.append(res)

            # For other non-digits just push onto the stack.
            else:
                stack.append(ch)

    # Push the last operand to stack, if any.
    if n:
        stack.append(operand)

    # Evaluate any left overs in the stack.
    return evaluate_expr(stack)


class TestCalculate(unittest.TestCase):
    """Unit test for calculate."""

    def test_1(self):
        """Test for 1+1 = 2."""
        self.assertEqual(calculate("1 + 1"), 2)

    def test_2(self):
        """Test for 2-1+2 = 3."""
        self.assertEqual(calculate(" 2-1 + 2 "), 3)

    def test_3(self):
        """Test for (1+(4+5+2)-3)+(6+8) = 23"""
        self.assertEqual(calculate("(1+(4+5+2)-3)+(6+8)"), 23)


if __name__ == '__main__':
    unittest.main()
