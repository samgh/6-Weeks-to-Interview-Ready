/*
 *   Title: Search In Rotated Array
 *   Leetcode Link: https://leetcode.com/problems/search-in-rotated-sorted-array/
 *
 *   Problem: Given a a sorted array that is rotated around some unknown pivot
 *   point, write a function to find the index of a target value.
 *   (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2])
 *
 *   You can assume the array contains no duplicates.
 *
 *   Input:
 *      int[] arr   => The array to search in
 *      int target  => The value to search for
 *   Output:
 *      int         => The index of target. Return -1 if not found
 *
 *   Execution: javac SearchRotatedArray.java && java -ea SearchRotatedArray
 */

public class SearchRotatedArray {

    /*
     * Perform a modified binary search. In addition to considering whether the
     * value is to the left or the right of the midpoint, we also have to
     * consider whether the pivot point is to the left or righ.
     *
     * Time Complexity: O(log n)
     * Space Complexity: O(1)
     */
    public static int searchRotatedArray(int[] arr, int target) {
        // The bounds of our current subarray
        int low = 0;
        int high = arr.length-1;

        // Keep dividing subarray in half until we either find the value we're
        // looking for or the subarray length is 0 (aka low >= high)
        while (low <= high) {
            // The midpoint of our subarray
            int mid = (low + high)/2;

            // If we've found the value, return the index
            if (target == arr[mid]) return mid;

            // If the target < arr[mid], we have 3 possible options:
            // 1. Left subarray contains pivot. This means all values lower than
            // arr[mid] are in the left subarray
            // 2. target >= arr[low]. This means target is in left subarray
            // 3. target < arr[low]. This means there could be a pivot in the
            // right subarray so if our target is in the array it must be there
            if (target < arr[mid]) {
                // A subarray must contain pivot if arr[low] > arr[high]
                if (arr[low] > arr[mid] || target >= arr[low]) {
                    high = mid-1;
                } else {
                    low = mid+1;
                }
            } else {
                // If target > arr[mid] we just do the opposite of above
                if (arr[mid] > arr[high] || target <= arr[high]) {
                    low = mid+1;
                } else {
                    high = mid-1;
                }
            }
        }

        return -1;
    }

    public static void main(String[] args) {
        assert searchRotatedArray(new int[]{4,5,6,7,0,1,2}, 0) == 4;
        assert searchRotatedArray(new int[]{4,5,6,7,0,1,2}, 3) == -1;

        // ADD YOUR TESTCASES HERE

        System.out.println("Passed all test cases");
    }

}
