/*
*    Title: Is even or odd.
*
*    Problem:
*        Write a program to determine if a given number is even or odd.
*        Do not make use of the modulus operator.
*
*    Execution: javac IsEvenOdd.java && java IsEvenOdd
*/
import java.util.*;


public class IsEvenOdd {
    public static String isEvenOdd(int x) {
        if ((x & 1) == 0) {
            return "Even";
        } else {
            return "Odd";
        }
    }

    public static void main(String[] args) {
        assert isEvenOdd(26) == "Even";
        assert isEvenOdd(25) == "Odd";

        System.out.println("Passed all test cases");
    }
}
