/*
 *   Title: Find anagrams
 *   Problem:
 *        Given a string s and a non-empty string p, find all the start indices
 *        of p's anagrams in s.
 *
 *       Strings consists of lowercase English letters only and the length of
 *       both strings s and p will not be larger than 20,100.
 *
 *       The order of output does not matter.
 *
 *   Execution: javac FindAnagrams.java && java FindAnagrams
 */
import java.util.*;


public class FindAnagrams {
    static List<Integer> findAnagrams(String s, String p) {
        List<Integer> res = new ArrayList<>();
        int len = p.length();

        if (len>s.length()) {
            return res;
        }

        int[] table = new int[26];
        Arrays.fill(table, 0);
        char[] pch = p.toCharArray();

        for (char ch: pch){
            table[ch-'a']++;
        }

        char[] sch = s.toCharArray();
        int[] comp = new int[26];

        for (int i=0; i<len-1; i++){
            comp[sch[i]-'a']++;
        }

        boolean flag=true;
        for (int i=0; i<=s.length()-len; i++){
            comp[sch[i+len-1]-'a']++;
            for (int j=0; j<=25; j++){
                if(table[j]!=comp[j]){
                    flag=false;
                    break;
                }
            }
            if (flag) {
                res.add(i);
            }
            flag=true;
            comp[sch[i]-'a']--;
        }
        return res;
    }

    public static boolean check_array_equality(List<Integer> arr_1, List<Integer> arr_2) {

        if (arr_1.size() != arr_2.size()) {
            return false;
        }

        for (int i = 0; i < arr_1.size(); i++) {
            if (arr_1.get(i) != arr_2.get(i)) {
                return false;
            }
        }
        return true;
    }

    // Sample test cases
    public static void main(String[] args) {

        // Test 1:
        List<Integer> expected_output_1 = new ArrayList<Integer>();
        expected_output_1.add(0);
        expected_output_1.add(6);

        System.out.println(check_array_equality(findAnagrams("cbaebabacd", "abc"), expected_output_1));

        // Test 2:
        List<Integer> expected_output_2 = new ArrayList<Integer>();
        expected_output_2.add(0);
        expected_output_2.add(1);
        expected_output_2.add(2);

        System.out.println(check_array_equality(findAnagrams("abab", "ab"), expected_output_2));

        System.out.println("Passed all test cases");
    }
    
}
