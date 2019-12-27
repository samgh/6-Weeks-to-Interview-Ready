/*
 *   Title: Find substring
 *
 *   Problem:
        You are given a string, s, and a list of words, words, that are all of the
        same length. Find all starting indices of substring(s) in s that is a
        concatenation of each word in words exactly once and without any
        intervening characters.
 *
 *   Execution: javac FindSubstring.java && java FindSubstring
 */

import java.util.*;

public class FindSubstring {
    public static List<Integer> findSubstring(String s, String[] words) {
        List<Integer> result = new ArrayList<Integer>();

        if(s.length() == 0 || words.length == 0) return result;
        int length = words[0].length();
        int sLength = s.length();

        HashMap<String,Integer> concat = new HashMap<String,Integer>();

        for(String word : words){
            concat.put(word,concat.getOrDefault(word,0)+1);
        }
        HashMap<String,Integer> local = new HashMap<String,Integer>();

        int start = 0;
        int end = length-1;

        while(end < sLength){
            //System.out.println(end);
            String sub = s.substring(end-length+1,end+1);
            if(concat.containsKey(sub)){
                local.put(sub,local.getOrDefault(sub,0)+1);
                if(concat.get(sub) == 1) concat.remove(sub);
                else concat.put(sub,concat.get(sub) - 1);
                end += length;
            }else {

                if(!local.isEmpty()){
                    for(Map.Entry<String,Integer> entry : local.entrySet()){
                        String word = entry.getKey();
                        int value = entry.getValue();
                        concat.put(word,concat.getOrDefault(word,0)+value);
                    }
                    local = new HashMap<>();
                }
                start++;
                end = start + length - 1;
            }
            if(concat.isEmpty()){
                result.add(start);
                concat = local;
                local = new HashMap<String,Integer>();
                start++;
                end = start + length -1;
            }
        }

        return result;
    }

    public static void main(String[] args) {

        List<Integer> expected_output_1 = new ArrayList<Integer>();
        expected_output_1.add(0);
        expected_output_1.add(9);

        String[] words_test_1 = {"foo", "bar"};

        assert findSubstring("barfoothefoobarman", words_test_1) == expected_output_1;
        System.out.println("Passed all test cases");
    }
}
