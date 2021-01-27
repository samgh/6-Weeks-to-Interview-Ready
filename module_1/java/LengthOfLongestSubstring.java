/*
 *   Title: Longest substring without repeating characters.
 *
 *   Given a string, find the length of the longest substring without repeating characters.
 *
 *   Execution: javac LengthOfLongestSubstring && java LengthOfLongestSubstring
 */

import java.util.HashSet;
import java.util.Set;

public class LengthOfLongestSubstring {
    public static int lengthOfLongestSubstring(String s) {
        int n = s.length(), ans = 0;

        // Current index of character.
        int[] index = new int[128];

        // Attempt to extend the range.
        int i = 0;
        for (int j = 0; j < n; j++) {
            i = Math.max(index[s.charAt(j)], i);
            ans = Math.max(ans, j - i + 1);
            index[s.charAt(j)] = j + 1;
        }
        return ans;
    }

    // Code that directly mirrors the video solution
    public static int lengthOfLongestSubstringAlt(String s) {
      Set<Character> inSubstring = new HashSet<Character>();

      int maxLength = 0;

      int i = 0;
      for (int j = 0; j < s.length(); j++) {
        char c = s.charAt(j);
        while (inSubstring.contains(c)) {
          inSubstring.remove(s.charAt(i));
          i++;
        }
        inSubstring.add(c);
        maxLength = Math.max(maxLength, j-i+1);
      }

      return maxLength;
    }

    // Sample test cases
    public static void main(String[] args) {
      System.out.println(lengthOfLongestSubstring("abcabcbb"));
        assert lengthOfLongestSubstring("abcabcbb") == 3;
        System.out.println("Explanation: The answer is 'abc', with the length of 3.");

        assert lengthOfLongestSubstring("bbbbb") == 1;
        System.out.println("Explanation: The answer is 'b', with the length of 1.");

        assert lengthOfLongestSubstring("pwwkew") == 3;
        System.out.println("Explanation: The answer is 'wke', with the length 3. Note that the answer must be a substring, 'pwke' is a subsequence and not a substring.");

        System.out.println("Passed all test cases");
    }

}
