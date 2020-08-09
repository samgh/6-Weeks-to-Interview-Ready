/*
 *   Title: Convert string to binary sequence
 *
 *   Problem:
 *      Given a string of character the task is to convert each character of a
 *      string into the equivalent binary number.
 *
 *   Execution: javac StringToBinary.java && java StringToBinary
 */
import java.util.*;


public class StringToBinary {
    static String stringToBinary(String s) {
        int n = s.length();

        String bin = "";
        for (int i = 0; i < n; i++) {
            // Convert each char to ASCII value.
            int val = Integer.valueOf(s.charAt(i));

            // Convert ASCII value to binary.
            bin = "";
            while (val > 0) {
                if (val % 2 == 1) {
                    bin += '1';
                }
                else {
                    bin += '0';
                }
                val /= 2;
            }
            bin = reverse(bin);
            System.out.print(bin + " ");
        }
        return bin;
    }

    static String reverse(String input) {
        char[] a = input.toCharArray();
        int l, r = 0;
        r = a.length - 1;

        for (l = 0; l < r; l++, r--) {
            // Swap values of l and r
            char temp = a[l];
            a[l] = a[r];
            a[r] = temp;
        }
        return String.valueOf(a);
    } 
    public static void main(String[] args) {
        String s = "BbB";
        assert stringToBinary(s) == "1000010 1100010 1000010";

        System.out.println("Passed all test cases");
    }
}
