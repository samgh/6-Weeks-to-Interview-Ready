/*
 *   Title: Maximum subarray
 *
 *   Problem:Given an integer array nums, find the contiguous subarray
 *   (containing at least one number) which has the largest sum and return its
 *   sum.
 *
 *   Execution: javac MaximumSubarray && java MaximumSubarray
 */


public class MaximumSubarray {
    public static int maximumSubarray(int[] A) {
        int maxSoFar = A[0];
        int maxEndingHere = A[0];
        for (int i=1; i<A.length; ++i){
            maxEndingHere = Math.max(maxEndingHere+A[i], A[i]);
            maxSoFar = Math.max(maxSoFar, maxEndingHere);
        }
        return maxSoFar;
    }

    public static void main(String[] args) {
        int[] testInputArray = {-2,1,-3,4,-1,2,1,-5,4};
        assert maximumSubarray(testInputArray) == 6;
        System.out.println("Explanation: [4,-1,2,1] has the largest sum = 6.");

        System.out.println("Passed all test cases");
    }
    
}
