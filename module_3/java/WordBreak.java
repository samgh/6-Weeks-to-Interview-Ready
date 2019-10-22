/*
 *   Title: Word break
 *
 *   Problem:
 *   Given a non-empty string s and a dictionary wordDict containing a list
 *   of non-empty words, determine if s can be segmented into a space-separated
 *   sequence of one or more dictionary words.
 *
 *   Note:
 *      The same word in the dictionary may be reused multiple times in the
 *      segmentation.  You may assume the dictionary does not contain duplicate
 *      words.
 *
 *   Execution: javac WordBreak.java && java WordBreak
 */
import java.util.*;


public class WordBreak {
    public static boolean wordBreak(String s, Set<String> dict) {
        boolean[] f = new boolean[s.length() + 1];
        
        f[0] = true;
        
        for(int i = 1; i <= s.length(); i++){
            for(String str: dict){
                if(str.length() <= i){
                    if(f[i - str.length()]){
                        if(s.substring(i-str.length(), i).equals(str)){
                            f[i] = true;
                            break;
                        }
                    }
                }
            }
        }
        
        return f[s.length()];
    }

    public static void main(String[] args) {
        String testStr1 = "leetcode";
        Set<String> testDict1 = new HashSet<String>();

        testDict1.add("leet");
        testDict1.add("code");

        assert wordBreak(testStr1, testDict1) == true;
        System.out.println("Explanation: Return true because 'leetcode' can be segmented as 'leet code'.");

        String testStr2 = "applepenapple";
        Set<String> testDict2 = new HashSet<String>();

        testDict2.add("apple");
        testDict2.add("pen");

        assert wordBreak(testStr2, testDict2) == true;
        System.out.println("Explanation: Return true because 'applepenapple' can be segmented as 'apple pen apple'.");

        String testStr3 = "catsandog";
        Set<String> testDict3 = new HashSet<String>();

        testDict3.add("cats");
        testDict3.add("dog");
        testDict3.add("sand");
        testDict3.add("and");
        testDict3.add("cat");

        assert wordBreak(testStr3, testDict3) == false;

        System.out.println("Passed all test cases");
    }
    
}
