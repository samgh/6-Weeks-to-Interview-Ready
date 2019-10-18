/*
 *   Title: Search rotated array.
 *
 *   Problem:
 *   Suppose an array sorted in ascending order is rotated at some pivot
 *   unknown to you beforehand.
 *
 * (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
 * 
 * You are given a target value to search. If found in the array return its index,
 * otherwise return -1.
 * 
 * You may assume no duplicate exists in the array.
 *
 * Your algorithm's runtime complexity must be in the order of O(log n).
 *
 *   Execution: javac SearchRotatedArray.java && java SearchRotatedArray
 */


public class SearchRotatedArray {
    public static int searchRotatedArray(int A[], int n, int target) {
        int low = 0;
        int high = n-1;
        // Find the index of the smallest value using binary search.
        // Loop will terminate since mid < hi, and low or high 
        // will shrink by at least 1.
        
        // Proof by contradiction that mid < high: if mid==high, 
        // then low == high and loop would have been terminated.
        while(low < high){
            int mid = (low + high)/2;
            if(A[mid] > A[high]){
                low = mid+1;
            }
            else {
                high = mid;
            }
        }
        // low = high is the index of the smallest value 
        // and also the number of places rotated.
        int rot = low;
        low = 0;
        high = n-1;
        // The usual binary search and accounting for rotation.
        while(low <= high){
            int mid = (low + high)/2;
            int realmid=(mid + rot) % n;
            if(A[realmid] == target){
                return realmid;
            }
            if(A[realmid] < target){
                low = mid+1;
            }
            else {
                high = mid-1;
            }
        }
        return -1;
    }
    public static void main(String[] args) {
        int[] testInputArray1 = {4,5,6,7,0,1,2};
        assert searchRotatedArray(testInputArray1, 7, 0) == 4;

        int[] testInputArray2 = {4,5,6,7,0,1,2};
        assert searchRotatedArray(testInputArray2, 7, 3) == -1;

        System.out.println("Passed all test cases");
    }
    
}
