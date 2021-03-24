/*
 *   Title: Basic calculator
 *
 *   Problem:
 *      Implement a basic calculator to evaluate a simple expression
 *      string.
 *
 *      The expression string may contain open ( and closing parentheses ), the plus +
 *      or minus sign -, non-negative integers and empty spaces .
 *
 *   Execution: javac Calculate.java && java Calculate
 */
import java.util.*;


public class Calculate {
    public static int evaluateExpr(Stack<Object> stack) {

        int res = 0;

        if (!stack.empty()) {
            res = (int) stack.pop();
        }

        // Evaluate the expression till we get corresponding ')'
        while (!stack.empty() && !((char) stack.peek() == ')')) {

            char sign = (char) stack.pop();

            if (sign == '+') {
                res += (int) stack.pop();
            } else {
                res -= (int) stack.pop();
            }
        }
        return res;
    }

    public static int calculate(String s) {

        int operand = 0;
        int n = 0;
        Stack<Object> stack = new Stack<Object>();

        for (int i = s.length() - 1; i >= 0; i--) {

            char ch = s.charAt(i);

            if (Character.isDigit(ch)) {

                // Forming the operand - in reverse order.
                operand = (int) Math.pow(10, n) * (int) (ch - '0') + operand;
                n += 1;

            } else if (ch != ' ') {
                if (n != 0) {

                    // Save the operand on the stack
                    // As we encounter some non-digit.
                    stack.push(operand);
                    n = 0;
                    operand = 0;

                }
                if (ch == '(') {

                    int res = evaluateExpr(stack);
                    stack.pop();

                    // Append the evaluated result to the stack.
                    // This result could be of a sub-expression within the parenthesis.
                    stack.push(res);

                } else {
                    // For other non-digits just push onto the stack.
                    stack.push(ch);
                }
            }
        }

        //Push the last operand to stack, if any.
        if (n != 0) {
            stack.push(operand);
        }

        // Evaluate any left overs in the stack.
        return evaluateExpr(stack);
    }

    // Using recursion rather than stacks to solve this problem
    public static int calculateRecursive(String s) {
        return calculateRecursive(s, 0, s.length());
    }

    private static int calculateRecursive(String s, int start, int end) {
        int sum = 0;
        char currentSign = '+';

        for (int i = start; i < end; i++) {
            char currentChar = s.charAt(i);

            if (currentChar == ' ') continue;

            if (currentChar == '+' || currentChar == '-') {
                currentSign = currentChar;
                continue;
            }

            int nextValue = 0;

            if (Character.isDigit(currentChar)) nextValue = Integer.parseInt(String.valueOf(currentChar));
            if (currentChar == '(') {
                int endParen = getMatchingParen(s, i);
                nextValue = calculateRecursive(s, i+1, endParen);
                i = endParen;
            }

            if (currentSign == '+') sum += nextValue;
            else sum -= nextValue;
        }

        return sum;
    }

    private static int getMatchingParen(String s, int start) {
        int countOpen = 1;
        for (int i = start+1; i < s.length(); i++) {
            if (s.charAt(i) == '(') countOpen++;
            if (s.charAt(i) == ')') countOpen--;
            if (countOpen == 0) return i;
        }
        return -1;
    }


    public static void main(String[] args) {
        assert calculate("1 + 1") == 2;
        assert calculate(" 2-1 + 2 ") == 3;
        assert calculate("(1+(4+5+2)-3)+(6+8)") == 23;

        System.out.println("Passed all test cases");
    }

}
