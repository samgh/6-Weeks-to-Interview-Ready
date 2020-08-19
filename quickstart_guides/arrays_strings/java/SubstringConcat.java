/*
 *   Title: Substring with Concatenation of All Words
 *
 *   Problem:
 *
 *       You are given a string, s, and a list of words, words, that are all of the same
 *       length. Find all starting indices of substring(s) in s that is a concatenation
 *       of each word in words exactly once and without any intervening characters.
 *
 *   Execution: javac SubstringConcat.java && java SubstringConcat
 */
import java.util.*;


public class SubstringConcat {
    static List<Integer> substringConcat(String s, String[] words) {
        ArrayList<Integer> res = new ArrayList<Integer>();
        if (s == null || s.length() == 0 || words == null || words.length == 0)
            return res;
        int wordLength = words[0].length();
        HashMap<String, Integer> needs = new HashMap<String, Integer>();
        for (String word : words) {
            needs.put(word, needs.getOrDefault(word, 0) + 1);
        }

        for (int i = 0; i < wordLength; i++) {
            int left = i, right = i, match = 0;
            HashMap<String, Integer> window = new HashMap<>();

            while (right < s.length() - wordLength + 1) {
                String s1 = s.substring(right, right + wordLength);
                if (needs.containsKey(s1)) {
                    window.put(s1, window.getOrDefault(s1, 0) + 1);
                    if (window.get(s1) == needs.get(s1)) {
                        match++;
                    }
                }
                right += wordLength;
                while (needs.size() == match) {
                    if (right - left == wordLength * words.length) {
                        res.add(left);
                    }
                    String s2 = s.substring(left, left + wordLength);
                    if (needs.containsKey(s2)) {
                        window.put(s2, window.get(s2) - 1);
                        if (window.get(s2) < needs.get(s2)) {
                            match--;
                        }
                    }
                    left += wordLength;
                }
            }
        }
        return res;
    }

    public static void main(String[] args) {

        String s1 = "barfoothefoobarman";
        String[] words1 = {"foo", "bar"};

        List<Integer> expected_res1 = new ArrayList<Integer>(){{
                        add(0);
                        add(9);
                          }};
        assert substringConcat(s1, words1).equals(expected_res1);

        String s2 = "wordgoodgoodgoodbestword";
        String[] words2 = {"word","good","best","word"};
        List<Integer> expected_res2 = new ArrayList<Integer>(){{
                          }};
        assert substringConcat(s2, words2).equals(expected_res1);

        System.out.println("Passed all test cases");
    }
    
}
