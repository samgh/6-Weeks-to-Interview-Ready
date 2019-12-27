/*
    Title: Is n^th bit set

    Problem:
        Write a program that takes an integer and tests whether
        the n-th bit in the binary representation of that integer
        is set of not.

        For instance, the binary representation of 6 is:
            110
        The least significant bit is the bit on the far right
        of the binary representation and the most significant
        bit is the bit on the far left. We order the bits as

        b2, b1, b0
        1   1   0

        For our function, if we check the 0th bit, we should obtain
        "False" as the binary value at b0 is 0.
        Alternatively, if we check the 1st bit, we should obtain
        "True" as the binary value at b1 is 1.

    Execution: javac IsNthBitSet.java && java IsNthBitSet
 */
import java.util.*;


public class IsNthBitSet {
    public static boolean isNthBitSet(int x, int n) {
        if ((x & (1 << (n - 1))) == 1) {
            return true;
        }        
        return false;
    }

    public static void main(String[] args) {
        assert isNthBitSet(6, 2) == true;
        assert isNthBitSet(6, 0) == false;
        System.out.println("Passed all test cases");
    }
}
