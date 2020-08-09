/*
*    Title: Set n^th bit
*
*    Problem:
*        Write a program  that takes an integer and sets the n-th bit in the
*        binary representation of that integer.
*
*        For instance, the binary representation of 6 is:
*            110
*        The least significant bit is the bit on the far right of the binary
*        representation and the most significant bit is the bit on the far left.
*        We order the bits as
*
*        b2, b1, b0
*        1   1   0
*
*        For our function, if we set the 0th bit, we should obtain the binary
*        representation:
*            1 1 1
*
*    Execution: javac SetNthBit.java && java SetNthBit
*/
import java.util.*;


public class SetNthBit {
    public static int setNthBit(int x, int n) {
        return x | (1 << n);
    }

    public static void main(String[] args) {
        assert setNthBit(6, 0) == 7;
        System.out.println("Passed all test cases");
    }
}
