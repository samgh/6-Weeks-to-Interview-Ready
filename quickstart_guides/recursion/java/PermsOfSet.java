/*
 *   Title: Perms of set
 *
 * Problem:
 *
 *   A permutation, also called an “arrangement number” or “order,” is a
 *   rearrangement of the elements of an ordered list S into a one-to-one
 *   correspondence with S itself. A string of length n has n! permutation.
 *
 *   Execution: javac PermsOfSet.java && java PermsOfSet
 */
import java.util.Arrays;


public class PermsOfSet {

    /**
     * permutation function
     * @param str string to calculate permutation for
     * @param l starting index
     * @param r end index
     */
    private void permute(String str, int l, int r) {
        if (l == r)
            System.out.println(str);
        else {
            for (int i = l; i <= r; i++) {
                str = swap(str,l,i);
                permute(str, l+1, r);
                str = swap(str,l,i);
            }
        }
    }

    /**
     * Swap Characters at position
     * @param a string value
     * @param i position 1
     * @param j position 2
     * @return swapped string
     */
    public String swap(String a, int i, int j) {
        char temp;
        char[] charArray = a.toCharArray();
        temp = charArray[i] ;
        charArray[i] = charArray[j];
        charArray[j] = temp;
        return String.valueOf(charArray);
    }

    public static void main(String[] args) {
        String str = "ABC";
        int n = str.length();
        PermsOfSet permutation = new PermsOfSet();
        permutation.permute(str, 0, n-1);
    }
}
