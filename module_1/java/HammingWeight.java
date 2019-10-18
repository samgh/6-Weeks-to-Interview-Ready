/*
 *   Title: Write a function that takes an unsigned integer and return the
 *   number of '1' bits it has (also known as the Hamming weight).
 *
 *   Problem: Calculate Hamming Weight
 *
 *   Execution: javac HammingWeight.java && java HammingWeight
 */


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

        int testInput1 = Integer.parseInt("00000000000000000000000000001011");  
        assert hammingWeight(testInput1) == 3;
        System.out.println("The input binary string 00000000000000000000000000001011 has a total of three '1' bits.");

        int testInput2 = Integer.parseInt("00000000000000000000000010000000");
        assert hammingWeight(testInput2) == 1;
        System.out.println("The input binary string 00000000000000000000000010000000 has a total of one '1' bit.");

        System.out.println("Passed all test cases");
    }
    
}
