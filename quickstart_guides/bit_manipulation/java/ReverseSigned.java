/*
*    Title: Reverse signed
*
*    Problem:
*        Reverse bits of a given 32 bits unsigned integer.
*
*    Execution: javac ReverseSigned.java && java ReverseSigned
*/
import java.util.*;


public class ReverseSigned {
    public static int reverseSigned(int n) {
        char[] chs = new char[Integer.SIZE];
		for (int i = 0; i < Integer.SIZE; i++)
		{
			chs[i] = (char) (((n >> i) & 1) + '0');
		}
		String resStr = new String(chs);

        // Avoid overflow.
		long total=0;
		char [] binCharArray = resStr.toCharArray();

		// Convert the binary string into an int number.
        for (int i = 0; i < binCharArray.length; i++) {
            total=total+binCharArray[i]-48;
            if(i!=binCharArray.length-1){
                total=total<<1;
            }
        }
    return (int) total;
    }

    public static void main(String[] args) {
        int input_1 = Integer.parseInt("00000010100101000001111010011100", 2);
        int output_1 = Integer.parseInt("00111001011110000010100101000000", 2);

        assert reverseSigned(input_1) == output_1;

        System.out.println("Passed all test cases");
    }
}
