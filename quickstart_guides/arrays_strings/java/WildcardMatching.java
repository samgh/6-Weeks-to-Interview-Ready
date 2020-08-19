/*
 *   Title: Wildcard Matching
 *
 *   Problem:
 *       Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.
 *
 *       '?' Matches any single character.
 *       '*' Matches any sequence of characters (including the empty sequence).
 *       The matching should cover the entire input string (not partial).
 *
 *       Note:
 *
 *       s could be empty and contains only lowercase letters a-z.
 *       p could be empty and contains only lowercase letters a-z, and characters like ? or *.
 *
 *   Execution: javac WildcardMatching.java && java WildcardMatching
 */

import java.util.*;

public class WildcardMatching {
    public static boolean wildcardMatching(String s, String p) {
        boolean[][] dp = new boolean[s.length() + 1][p.length() + 1];
        dp[0][0] = true;
        for (int i = 0; i < p.length(); i++) {
            if(p.charAt(i) == '*' && dp[0][i]){
                dp[0][i+1] = true;
            }
        }
        for (int i = 0; i < s.length(); i++) {
            for (int j = 0; j < p.length(); j++) {
                if(s.charAt(i) == p.charAt(j) || p.charAt(j) == '?'){
                    dp[i+1][j+1] = dp[i][j];
                }
                if(p.charAt(j) == '*'){
                    dp[i + 1][j + 1] = dp[i][j + 1] || dp[i + 1][j];
                }
            }
        }
        return dp[s.length()][p.length()];
    }
    
    public static void main(String[] args) {
        assert wildcardMatching("aa", "a") == false;
        assert wildcardMatching("aa", "*") == true;
        assert wildcardMatching("cb", "?a") == false;
        assert wildcardMatching("adceb", "*a*b") == true;
        assert wildcardMatching("acdcb", "a*c?b") == false;

        System.out.println("Passed all test cases");
    }
}
