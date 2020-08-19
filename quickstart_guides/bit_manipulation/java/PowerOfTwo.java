/*
*    Title: Power of two.
*
*    Problem:
*        Given an integer, write a function to determine if it is a power of
*        two.
*
*    Execution: javac PowerOfTwo.java && java PowerOfTwo
*/
import java.util.*;


public class PowerOfTwo {
    public static boolean powerOfTwo(int n) {
        int powerOfTwo = 2;
        if(n==1 || n==2)
            return true;

        // Checking for odd numbers.
        if(n % 2 == 1)
            return false;
        while(powerOfTwo<=n/2) {
            powerOfTwo=powerOfTwo*2;
        if(n==powerOfTwo)
            return true;
        }
        return false;
    }

    public static void main(String[] args) {
        assert powerOfTwo(1) == true;
        assert powerOfTwo(16) == true;
        assert powerOfTwo(218) == false;

        System.out.println("Passed all test cases");
    }
}
