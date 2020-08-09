/*
 *   Title: Is palindrome
 *
 * Problem:
 *   Given a string, determine if it is a palindrome, considering only
 *   alphanumeric characters and ignoring cases.
 *
 *   Note: For the purpose of this problem, we define empty string as valid
 *   palindrome.
 *
 *   Execution: javac IsPalindrome.java && java IsPalindrome
 */
import java.util.Arrays;


public class IsPalindrome {
    public static boolean isPalindrome(String s) {
        if((s == null) || (s.length() == 0)) {
            return true;
        }

        s = String.join("",Arrays.asList(s.split("\\W+")));
        s = s.toLowerCase();

        String snew = new StringBuilder(s).reverse().toString();
        return s.equals(snew);
    }

    public static void main(String[] args) {
        assert isPalindrome("A man, a plan, a canal: Panama") == true;
        assert isPalindrome("race a car") == false;

        System.out.println("Passed all test cases");
    }
    
}
