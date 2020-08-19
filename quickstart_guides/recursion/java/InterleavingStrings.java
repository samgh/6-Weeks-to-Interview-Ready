/*
 *   Title: Interleaving strings
 *
 * Problem:
 *   Check whether a string interleaves with two other strings.
 *
 *   Execution: javac InterleavingStrings.java && java InterleavingStrings
 */
import java.util.Arrays;


public class InterleavingStrings {

    // Returns true if C is an interleaving of A and B, otherwise returns false.
    static boolean isInterleaved (String A, String B, String C)
    {
        int i = 0, j = 0, k = 0;

        // Iterate through all characters of C.
        while (k != C.length())
        {
            // Match first character of C with first character
            // of A. If matches them move A to next
            if (i<A.length()&&A.charAt(i) == C.charAt(k))
                i++;

            // Else Match first character of C with first
            // character of B. If matches them move B to next
            else if (j<B.length()&&B.charAt(j) == C.charAt(k))
                j++;

            // If doesn't match with either A or B, then return
            // false
            else
                return false;

            // Move C to next for next iteration
            k++;
        }

        // If A or B still have some characters, then length of C is smaller
        // than sum of lengths of A and B, so return false.
        if (i < A.length() || j < B.length())
            return false;

        return true;
    }

    public static void main(String []args){

        String A = "AB";
        String B = "CD";
        String C = "ACBG";
        if (isInterleaved(A, B, C) == true)
            System.out.printf("%s is interleaved of %s and %s", C, A, B);
        else
            System.out.printf("%s is not interleaved of %s and %s", C, A, B);
    }
}
