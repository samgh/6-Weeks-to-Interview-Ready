/*
*    Title: Power of four.
*
*    Problem:
*        Given an integer, write a function to determine if it is a power of
*        four.
*
*    Execution: javac PowerOfFour.java && java PowerOfFour
*/
import java.util.*;


public class PowerOfFour {
    public static boolean powerOfFour(int num) {
        if(num==1) return true;
        if(num==0) return false;
        while(num>4 && num%4==0){
            num=num/4;
            }
        if(num==4) return true;
        return false;
    }

    public static void main(String[] args) {
        assert powerOfFour(16) == true;
        assert powerOfFour(5) == false;

        System.out.println("Passed all test cases");
    }
}
