/*
 *   Title: Reverse string
 *
 *   Problem:
 *        Write a function that reverses a string. The input string is given as an
 *        array of characters char[].
 *
 *       Do not allocate extra space for another array, you must do this by
 *       modifying the input array in-place with O(1) extra memory.
 *
 *       You may assume all the characters consist of printable ascii characters.
 *
 *   Execution: javac ReverseString.java && java ReverseString
 */
import java.util.*;


public class ReverseString {
    public static char[] reverseString(char[] s) {
        int left = 0, right = s.length - 1;
        while (left < right) {
            char tmp = s[left];
            s[left++] = s[right];
            s[right--] = tmp;
        }
        return s;
    }

    public static void main(String[] args) {
        char[] test_input_1 = {'h','e','l','l','o'};
        char[] expected_output_1 = {'o','l','l','e','h'};
        assert reverseString(test_input_1) == expected_output_1;

        char[] test_input_2 = { 'H','a','n','n','a','h' };
        char[] expected_output_2 = { 'h','a','n','n','a','H' };
        assert reverseString(test_input_2) == expected_output_2;

        System.out.println("Passed all test cases");
    }
    
}
