/*
 *   Title: Regex matching
 *
 *   Problem:
 *       Given an input string (s) and a pattern (p), implement regular
 *       expression matching with support for '.' and '*'.
 *
 *       '.' Matches any single character.
 *       '*' Matches zero or more of the preceding element.
 *       The matching should cover the entire input string (not partial).
 *
 *       Note:
 *
 *       s could be empty and contains only lowercase letters a-z.
 *       p could be empty and contains only lowercase letters a-z, and characters like . or *.
 *
 *   Execution: javac RegexMatching.java && java RegexMatching
 */
import java.util.*;


public class RegexMatching {
    enum Result {
    TRUE, FALSE
    }

    static Result[][] memo;

    public static boolean regexMatchingTopDown(String text, String pattern) {
        memo = new Result[text.length() + 1][pattern.length() + 1];
        return dp(0, 0, text, pattern);
    }

    public static boolean dp(int i, int j, String text, String pattern) {
        if (memo[i][j] != null) {
            return memo[i][j] == Result.TRUE;
        }
        boolean ans;
        if (j == pattern.length()){
            ans = i == text.length();
        } else{
            boolean first_match = (i < text.length() &&
                                   (pattern.charAt(j) == text.charAt(i) ||
                                    pattern.charAt(j) == '.'));

            if (j + 1 < pattern.length() && pattern.charAt(j+1) == '*'){
                ans = (dp(i, j+2, text, pattern) ||
                       first_match && dp(i+1, j, text, pattern));
            } else {
                ans = first_match && dp(i+1, j+1, text, pattern);
            }
        }
        memo[i][j] = ans ? Result.TRUE : Result.FALSE;
        return ans;
    }
    public static boolean regexMatchingBottomUp(String text, String pattern) {
        boolean[][] dp = new boolean[text.length() + 1][pattern.length() + 1];
        dp[text.length()][pattern.length()] = true;

        for (int i = text.length(); i >= 0; i--){
            for (int j = pattern.length() - 1; j >= 0; j--){
                boolean first_match = (i < text.length() &&
                                       (pattern.charAt(j) == text.charAt(i) ||
                                        pattern.charAt(j) == '.'));
                if (j + 1 < pattern.length() && pattern.charAt(j+1) == '*'){
                    dp[i][j] = dp[i][j+2] || first_match && dp[i+1][j];
                } else {
                    dp[i][j] = first_match && dp[i+1][j+1];
                }
            }
        }
        return dp[0][0];
    }
    public static void main(String[] args) {
        assert regexMatchingTopDown("aa", "a") == false;
        assert regexMatchingBottomUp("aa", "a") == false;

        assert regexMatchingTopDown("aa", "a*") == true;
        assert regexMatchingBottomUp("aa", "a*") == true;

        assert regexMatchingTopDown("ab", ".*") == true;
        assert regexMatchingBottomUp("ab", ".*") == true;

        assert regexMatchingTopDown("aab", "c*a*b") == true;
        assert regexMatchingBottomUp("aab", "c*a*b") == true;

        assert regexMatchingTopDown("mississippi", "mis*is*p*.") == false;
        assert regexMatchingBottomUp("mississippi", "mis*is*p*.") == false;

        System.out.println("Passed all test cases");
    }
}
