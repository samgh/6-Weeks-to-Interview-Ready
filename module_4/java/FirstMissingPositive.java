/*
 *   Title: First missing positive.
 *
 *   Problem: Given an unsorted integer array, find the smallest missing
 *   positive integer.
 *
 *   Execution: javac FirstMissingPositive.java && java FirstMissingPositive
 */
import java.util.*;


public class FirstMissingPositive {

    public static int firstMissingPositive(int[] A) {
        for (int i = 0; i < A.length; i++) {
            if (A[i] <= 0 || A[i] > A.length) A[i] = Integer.MAX_VALUE;
        }

        for (int i = 0; i < A.length; i++) {
            int abs = Math.abs(A[i]);
            if (abs <= A.length) A[abs-1] = -Math.abs(A[abs-1]);
        }

        for (int i = 0; i < A.length; i++) {
            if (A[i] > 0) return i+1;
        }

        return A.length+1;
    }

    // Alternate implementation
    public static int firstMissingPositiveAlt(int[] A) {
        int i = 0;
        while(i < A.length){
            if(A[i] == i+1 || A[i] <= 0 || A[i] > A.length) i++;
            else if(A[A[i]-1] != A[i]) swap(A, i, A[i]-1);
            else i++;
        }
        i = 0;
        while(i < A.length && A[i] == i+1) i++;
        return i+1;
    }

    private static void swap(int[] A, int i, int j){
        int temp = A[i];
        A[i] = A[j];
        A[j] = temp;
    }

    public static void main(String[] args) {
        int[] test_input_1 = {1, 2, 0};
        assert firstMissingPositive(test_input_1) == 3;

        int[] test_input_2 = {3, 4, -1, 1};
        assert firstMissingPositive(test_input_2) == 2;

        int[] test_input_3 = {7, 8, 9, 11, 12};
        assert firstMissingPositive(test_input_3) == 1;

        System.out.println("Passed all test cases");
    }

}
