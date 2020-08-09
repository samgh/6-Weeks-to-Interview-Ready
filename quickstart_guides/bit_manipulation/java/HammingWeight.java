/*
*    Title: Hamming weight.
*
*    Problem:
*        Write a function that takes an unsigned integer and return the number
*        of '1' bits it has (also known as the Hamming weight).
*
*    Execution: javac HammingWeight.java && java HammingWeight
*/
import java.util.*;


public class HammingWeight {
    public static int hammingWeight(int n) {
        int sum = 0;
        while (n != 0) {
            sum++;
            n &= (n - 1);
        }
        return sum;
    }

    public static void main(String[] args) {
        int input_1 = Integer.parseInt("00000000000000000000000000001011", 2);
        int input_2 = Integer.parseInt("00000000000000000000000010000000", 2);

        assert hammingWeight(input_1) == 3;
        assert hammingWeight(input_2) == 1;

        System.out.println("Passed all test cases");
    }
}
