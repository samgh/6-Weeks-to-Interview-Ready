/*
 *   Title: Find square root
 *
 *   Problem:
 *      Implement int sqrt(int x).
 *
 *      Compute and return the square root of x, where x is guaranteed to be a
 *      non-negative integer.
 *
 *      Since the return type is an integer, the decimal digits are truncated and
 *      only the integer part of the result is returned.
 *
 *   Execution: javac FindSqrt.java && java FindSqrt
 */
class FindSqrt {
    public static int findSqrt(int x)
    {
        if(x == 0){
            return 0;
        }
        long l = 1;
        long r = (long)x;
        long middle = 0;
        while(l <= r){
            middle = (l + r) / 2;

            if(middle * middle == x)
                return (int)middle;
            else if(middle * middle < x)
            {
                l = middle + 1;
            }
            else
            {
                r = middle - 1;
            }
        }
        if(middle * middle > x)
            return (int)(middle - 1);
        return (int)middle;
    }

	public static void main(String args[])
	{
	    assert findSqrt(4) == 2;
	    assert findSqrt(16) == 4;

        System.out.println("Passed all test cases");
	}
}

