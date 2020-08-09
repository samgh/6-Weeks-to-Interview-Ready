/*
 *   Title: Longest substring without repeating characters.
 *
 *   Problem
 *      Given a string, find the length of the longest substring without
 *      repeating characters.
 *
 *   Execution: javac LengthOfLongestSubstring.java && java LengthOfLongestSubstring
 */

import java.util.HashMap;

public class LengthOfLongestSubstring {
    public static long lengthOfLongestSubstring(String s) {
        int n = s.length(), ans = 0;

        // Current index of character.
        int[] index = new int[128];

        // Attempt to extend the range.
        int i = 0;
        for (int j = 0; j < n; j++) {
            i = Math.max(index[s.charAt(j)], i);
            ans = Math.max(ans, j - 1 + 1);
            index[s.charAt(j)] = j + 1;
        }
        return ans;
    }

    public static void main(String[] args) {
        assert lengthOfLongestSubstring("abcabcbb") == 3;
        System.out.println("Explanation: The answer is 'abc', with the length of 3.");

        assert lengthOfLongestSubstring("bbbbb") == 1;
        System.out.println("Explanation: The answer is 'b', with the length of 1.");

        assert lengthOfLongestSubstring("pwwkew") == 3;
        System.out.println("Explanation: The answer is 'wke', with the length 3. Note that the answer must be a substring, 'pwke' is a subsequence and not a substring.");

        System.out.println("Passed all test cases");
    }
    
}
