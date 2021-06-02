/*
 *   Title: Longest palindrome
 *
 *   Problem:
 *
 *   Given a string s, find the longest palindromic substring in s. You
 *   may assume that the maximum length of s is 1000.
 *
 *   Execution: javac LongestPalindrome.java && java LongestPalindrome
 */


public class LongestPalindrome {
    public static String longestPalindrome(String s) {
        String res = "";
        int currLength = 0;
        for(int i=0; i<s.length(); i++){
            if(isPalindrome(s, i-currLength-1, i)) {
                res = s.substring(i-currLength-1, i+1);
                currLength = currLength + 2;
            }
            else if(isPalindrome(s, i-currLength, i)) {
                res = s.substring(i-currLength, i+1);
                currLength = currLength + 1;
            }
        }
        return res;
    }

    public static boolean isPalindrome(String s, int begin, int end){
        if(begin < 0) {
            return false;
        }
        while(begin < end) {
        	if(s.charAt(begin++) != s.charAt(end--)) { 
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        assert longestPalindrome("babad") == "bab";
        System.out.println("Note: 'aba' is also a valid answer");

        assert longestPalindrome("cbbd") == "bb";

        System.out.println("Passed all test cases");
    }
    
}
