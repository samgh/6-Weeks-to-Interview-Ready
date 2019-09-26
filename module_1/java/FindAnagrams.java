/*
 *   Title: Find Anagrams.
 *
 *   Problem: Given a string s and a non-empty string p, 
 *   find all the start indices of p's anagrams in s. 
 *
 *   Strings consists of lowercase English letters only and 
 *   the length of both strings s and p will not be larger than 20,100. 
 *
 *   The order of output does not matter.
 *
 *   Execution: javac FindAnagrams.java && java FindAnagrams
 */

import java.util.ArrayList;
import java.util.List;

public class FindAnagrams {
    public static List<Integer> findAnagrams(String s, String p) {
        List<Integer> list = new ArrayList<>();

        if (s == null || s.length() == 0 || p == null || p.length() == 0) {
            return list;
        }

        // Character hash.
        int[] hash = new int[256];

        // Record each character in "p" to a hash.
        for (char c : p.toCharArray()) {
            hash[c]++;
        }

        // Initialize count to "p"'s length.
        int left = 0, right = 0, count = p.length();
        while (right < s.length()) {
            // Move right each time if the character exists in p's hash
            // Decrease the count current hash value greater than 1
            // means the character exists in p.
            if (hash[s.charAt(right++)]-- >= 1) {
                count--;
            }

            // When the count is zero, this means we found the 
            // right anagram. Add window's left to result list.
            if (count == 0) {
                list.add(left);
            }

            if (right - left == p.length() && hash[s.charAt(left++)]++ >= 0) {
                count++;
            }
        }
        return list;
    }

    public static void main(String[] args) {
        List<Integer> expected_result_1 = new ArrayList<Integer>();
        expected_result_1.add(0);
        expected_result_1.add(6);
        List<Integer> result_1 = findAnagrams("cbaebabacd", "abc");

        if (result_1.equals(expected_result_1)) {
            System.out.println("Passed for string 'cbaebabcd'.");
        } else {
            System.out.println("Failed for string 'cbaebabcd'.");
        } 

        List<Integer> expected_result_2 = new ArrayList<Integer>();
        expected_result_2.add(0);
        expected_result_2.add(1);
        expected_result_2.add(2);
        List<Integer> result_2 = findAnagrams("abab", "ab");

        if (result_2.equals(expected_result_2)) {
            System.out.println("Passed for string 'abab'.");
        } else {
            System.out.println("Failed for string 'abab'.");
        } 

        System.out.println("Passed all test cases");
    }
    
}
