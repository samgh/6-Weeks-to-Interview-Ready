/*
*    Title: Sum two integers.
*
*    Problem:
*        Calculate the sum of two integers a and b, but you are not allowed to
*        use the operator + and -.
*
*    Execution: javac SumTwoIntegers.java && java SumTwoIntegers
*/
import java.util.*;


public class SumTwoInts {
    public static int sumTwoInts(int A, int B) {
        int carry = 0; 
		int r = 0;

		for(int i = 0; i < 32; ++i) {
			int a = (A & 1 << i);
			int b = (B & 1 << i);
			int t = a ^ b ^ carry;

			r |= t;

			// Case when both bits 1.
			if((a & b) != 0) {
				carry = 1 << ( i + 1);
			 // Case when a's or b's bit 1 and carry 1.
			} else if(carry != 0 && t == 0) {
				carry = 1 << ( i + 1);
			} else {
				carry = 0;
			}
		}

		return r;
    }

    public static void main(String[] args) {
        int a_1 = 3; 
        int b_1 = 2;

        int a_2 = -2;
        int b_2 = 3;

        assert sumTwoInts(a_1, b_1) == 3;
        assert sumTwoInts(a_2, b_2) == 1;

        System.out.println("Passed all test cases");
    }
}
