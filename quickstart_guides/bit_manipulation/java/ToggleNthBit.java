/*
    Title: Toggle n^th bit

    Problem:
        Write a program  that takes an integer and
        toggles the n-th bit in the binary representation of
        that integer
        For instance, the binary representation of 6 is:
            110
        The least significant bit is the bit on the far right
        of the binary representation and the most significant
        bit is the bit on the far left. We order the bits as
        b2, b1, b0
        1   1   0
        For our function, if we toggle the 0th bit, we should obtain
        the binary representation:
            1 1 1
        If we again toggle the 0th bit from the above representation 
        we obtain
            1 1 0
    Execution: javac ToggleNthBit.java && java ToggleNthBit
 */
import java.util.*;


public class ToggleNthBit {
    public static int toggleNthBit(int x, int n) {
        return x ^ (1 << n);
    }

    public static void main(String[] args) {
        assert toggleNthBit(6, 0) == 7;
        System.out.println("Passed all test cases");
    }
}
