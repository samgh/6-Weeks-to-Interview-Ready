/*
 *   Title: Find first duplicate entry
 *
 *   Problem:
 *   Write a function that takes an array of sorted integers and a key and
 *   returns the index of the first occurrence of that key from the array.
 *   Example:
 *       idx   0     1  2   3    4    5    6    7    8    9
 *       A = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
 *       target = 108
 *       Returns index 3 since 108 appears for the first time at
 *       index 3.
 *
 *   Execution: javac FindFirstDuplicateEntry.java && java FindFirstDuplicateEntry
 */


class FindFirstDuplicateEntry
{
	// Main Function to find fixed index using binary search.
	public static int findFirstDuplicatEnry(int arr[], int target)
	{
	    int low = 0;
	    int high = arr.length - 1;

	    while (low <= high) {
	        int mid = (low + high) / 2;

	        if (arr[mid] < target) {
	            low = mid + 1;
	        }
	        else if (arr[mid] > target) {
	            high = mid - 1;
	        }
	        else {
	            if (mid - 1 < 0) {
	                return mid;
	            }
	            if (arr[mid-1] != target) {
	                return mid;
	            }
	            high = mid - 1;
	        }
	    }
	    return -1;
	}

	public static void main(String[] args)
	{
		int arr[] = {-14, -10, 2, 108, 108, 243, 285, 285, 285, 401};
        int target = 108;
        assert findFirstDuplicatEnry(arr, target) == 3;

		System.out.println("All tests passed.");
	}
}

