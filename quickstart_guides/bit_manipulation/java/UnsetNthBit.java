/*
    Title: Unset n^th bit

    Problem:
        Write a program  that takes an integer and
        unsets the n-th bit in the binary representation of
        that integer
        For instance, the binary representation of 6 is:
            110
        The least significant bit is the bit on the far right
        of the binary representation and the most significant
        bit is the bit on the far left. We order the bits as
        b2, b1, b0
        1   1   0
        For our function, if we unset the 1st bit, we should obtain
        the binary representation:
            1 0 0

    Execution: javac UnsetNthBit.java && java UnsetNthBit
 */
import java.util.*;


public class UnsetNthBit {
    public static int unsetNthBit(int x, int n) {
        return x | ~(1 << n);
    }

    public static void main(String[] args) {
        assert unsetNthBit(6, 1) == 4;
        assert unsetNthBit(6, 2) == 2;
        System.out.println("Passed all test cases");
    }
}
