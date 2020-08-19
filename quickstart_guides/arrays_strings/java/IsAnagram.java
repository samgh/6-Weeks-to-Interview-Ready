/*
 *   Title: Is Anagram
 *
 *   Problem:
 *      Given two strings s and t , write a function to determine if t is an
 *      anagram of s.
 *
 *   Execution: javac IsAnagram.java && java IsAnagram
 */

import java.util.Arrays;
import java.util.List;

public class IsAnagram {
    public static boolean isAnagramSort(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }
        char[] str1 = s.toCharArray();
        char[] str2 = t.toCharArray();
        Arrays.sort(str1);
        Arrays.sort(str2);
        return Arrays.equals(str1, str2);
    }

    public static boolean isAnagramHashTable(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }
        int[] counter = new int[26];
        for (int i = 0; i < s.length(); i++) {
            counter[s.charAt(i) - 'a']++;
            counter[t.charAt(i) - 'a']--;
        }
        for (int count : counter) {
            if (count != 0) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        assert isAnagramSort("anagram", "nagaram") == true;
        assert isAnagramSort("rat", "car") == false;

        assert isAnagramHashTable("anagram", "nagaram") == true;
        assert isAnagramHashTable("rat", "car") == false;
        System.out.println("Passed all test cases");
    }
}
