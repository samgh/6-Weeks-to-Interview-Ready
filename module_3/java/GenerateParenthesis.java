/*
 *   Title: Generate parentheses
 *
 *   Problem:
 *      Given n pairs of parentheses, write a function to generate all
 *      combinations of well-formed parentheses.  For example, given n = 3, a
 *      solution set is:
 *      [
 *        "((()))",
 *         "(()())",
 *         "(())()",
 *         "()(())",
 *         "()()()"
 *      ]
 *
 *   Execution: javac GenerateParenthesis.java && java GenerateParenthesis
 */
import java.util.*;


public class GenerateParenthesis {
    public static List<String> generateParenthesisBruteForce(int n) {
        List<String> combinations = new ArrayList();
        generateAll(new char[2 * n], 0, combinations);
        return combinations;
    }

    public static void generateAll(char[] current, int pos, List<String> result) {
        if (pos == current.length) {
            if (valid(current))
                result.add(new String(current));
        } else {
            current[pos] = '(';
            generateAll(current, pos+1, result);
            current[pos] = ')';
            generateAll(current, pos+1, result);
        }
    }

    public static boolean valid(char[] current) {
        int balance = 0;
        for (char c: current) {
            if (c == '(') balance++;
            else balance--;
            if (balance < 0) return false;
        }
        return (balance == 0);
    }

    public static List<String> generateParenthesisBacktracking(int n) {
        List<String> ans = new ArrayList();
        backtrack(ans, "", 0, 0, n);
        return ans;
    }

    public static void backtrack(List<String> ans, String cur, int open, int close, int max){
        if (cur.length() == max * 2) {
            ans.add(cur);
            return;
        }

        if (open < max)
            backtrack(ans, cur+"(", open+1, close, max);
        if (close < open)
            backtrack(ans, cur+")", open, close+1, max);
    }
    public static void main(String[] args) {
        
        List<String> list = new ArrayList<String>();
        list.add("((()))");
        list.add("(()())");
        list.add("(())()");
        list.add("()(())");
        list.add("()()()");

        // Brute-force approach:
        assert generateParenthesisBruteForce(3) == list;

        // Backtracking approach:
        assert generateParenthesisBacktracking(3) == list;

        System.out.println("Passed all test cases");
    }
    
}
