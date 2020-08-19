/*
 *   Title: Sort string
 *
 *   Problem:
 *   Given a string of lowercase characters from ‘a’ – ‘z’. We need to write a
 *   program to print the characters of this string in sorted order.
 *
 *   Execution: javac SortString.java && java SortString
 */

import java.util.Arrays;

public class SortString {
    public static String sortString(String s) {
        char[] arr = s.toCharArray();
        Arrays.sort(arr);
        return String.valueOf(arr);
    }

    public static void main(String[] args) {
        assert sortString("bbccdefbbaa") == "aabbbbccdef";
        assert sortString("cba") == "abc";
        System.out.println("Passed all test cases");
    }
}
