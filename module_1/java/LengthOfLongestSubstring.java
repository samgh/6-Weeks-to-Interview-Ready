/*
 *   Title: Longest Substring Without Repeating Characters
 *   Leetcode Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
 *
 *   Problem: Given a string, find the length of the longest substring without
 *   repeating characters.
 *
 *   Input:
 *      String s    => String in which to find substring
 *   Output:
 *      int         => Length of longest substring
 *
 *   Execution: javac LengthOfLongestSubstring.java && java -ea LengthOfLongestSubstring
 *
 */

import java.util.HashSet;
import java.util.Set;

public class LengthOfLongestSubstring {

    /*
     * Solution #1: Using a sliding window with a set
     *
     * In this solution, we use a sliding window to keep track of the longest
     * substring. In a set, we store all the characters in the current substring
     * so that we can quickly see whether we can expand string or not.
     *
     * Time Complexity: O(n)
     * Space Complexity: O(1) - Our set has a max size of 26, so O(1)
     */
    public static int lengthOfLongestSubstring(String s) {
        // Set to store all chars in current substring
        Set<Character> inSubstring = new HashSet<Character>();

        int maxLength = 0;

        // i is the start of our substring and j is the end
        // We're using a sliding window here. Expand j out as far as possible
        // until there are duplicate characters, then increment i until there
        // are no longer any duplicates
        int i = 0;
        for (int j = 0; j < s.length(); j++) {
            char c = s.charAt(j);

            // If the character at j is already in string, increase i until it
            // is no longer in the string so that we can update j
            while (inSubstring.contains(c)) {
                inSubstring.remove(s.charAt(i));
                i++;
            }
            inSubstring.add(c);

            // Keep track of longest substring
            maxLength = Math.max(maxLength, j-i+1);
        }

        return maxLength;
    }

    /*
     * Solution #2: Using a sliding window tracking previous indices
     *
     * This is similar to the previous solution except that we track the index
     * of the previous occurence of each character. This allows us to quickly
     * update i to the right value rather than having to increment
     *
     * Time Complexity: O(n)
     * Space Complexity: O(1)
     */
    public static int lengthOfLongestSubstringImproved(String s) {
        // Index of the previous occurrence of character
        int[] index = new int[128];

        int maxLength = 0;

        // i is the start of our substring and j is the end
        // We're using a sliding window here. Expand j out as far as possible
        // until there are duplicate characters, then move i to 1 plus the
        // previous occurrence of that character
        int i = 0;
        for (int j = 0; j < s.length(); j++) {
            char c = s.charAt(j);

            // If the current character previously occurred after i's position
            // update i
            i = Math.max(index[c], i);
            maxLength = Math.max(maxLength, j-i+1);

            index[c] = j+1;
        }

        return maxLength;
    }

    // Sample test cases
    public static void main(String[] args) {
        assert lengthOfLongestSubstringImproved("abcabcbb") == 3;
        System.out.println("Explanation: The answer is 'abc', with the length of 3.");

        assert lengthOfLongestSubstringImproved("bbbbb") == 1;
        System.out.println("Explanation: The answer is 'b', with the length of 1.");

        assert lengthOfLongestSubstringImproved("pwwkew") == 3;
        System.out.println("Explanation: The answer is 'wke', with the length 3. Note that the answer must be a substring, 'pwke' is a subsequence and not a substring.");

        // ADD YOUR TESTS HERE
        
        System.out.println("Passed all test cases");
    }

}
