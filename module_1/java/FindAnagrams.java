 /*
  *   Title: Find Anagrams
  *   Leetcode Link: https://leetcode.com/problems/find-all-anagrams-in-a-string/
  *
  *   Problem: Given a string s and a non-empty string p, find all the start
  *   indices of p's anagrams in s.
  *
  *   Input:
  *      String s       => string to seach
  *      String p       => string to find anagrams of
  *   Output:
  *      List<Integer>  => inidices of anagrams in s
  *
  *   Execution: javac FindAnagrams.java && java -ea FindAnagrams
  */

import java.util.*;

public class FindAnagrams {

    /*
     * Start by counting the number of occurrences of each character in p. Then
     * we use a sliding window to find every substring of s that contains the
     * same set of characters.
     *
     * Time Complexity: O(n)
     * Space Complexity: O(1)
     */
    public static List<Integer> findAnagrams(String s, String p) {
        List<Integer> results = new ArrayList<>();

        // If either string is empty or p is longer than s, we have no results
        if (s.length() == 0 || p.length() == 0 || s.length() < p.length()) {
            return results;
        }

        // Counts of characters. Could also use Map<Character, Integer> but we
        // are told that all chars are lowercase English characters
        int[] pChars = new int[26];
        for (char c : p.toCharArray()) {
            pChars[c-'a']++;
        }

        // Track the start and end of our window in s, along with the chars in
        // that window. This should always be the size of p
        int start = 0, end = p.length()-1;
        int[] sChars = new int[26];

        // Fill up initial sChars
        for (int i = 0; i < p.length(); i++) sChars[s.charAt(i)-'a']++;

        // Iterate through every substring of length p
        while (end < s.length()-1) {
            // This is a slow but constant time operation because the arrays
            // are always the same size ragardless of the input
            if (Arrays.equals(pChars, sChars)) results.add(start);

            // Move our window by 1
            sChars[s.charAt(start)-'a']--;
            start++; end++;
            sChars[s.charAt(end)-'a']++;
        }

        // Get the last substring if it's valid
        if (Arrays.equals(pChars, sChars)) results.add(start);

        return results;
    }

    // Test cases
    public static void main(String[] args) {

        assert findAnagrams("cbaebabacd", "abc").equals(Arrays.asList(0,6));
        assert findAnagrams("abab", "ab").equals(Arrays.asList(0,1,2));

        // ADD YOUR OWN TEST HERE

        System.out.println("Passed all test cases");
    }

}
