/*
 *   Title: Find fixed point
 *
 *   Problem:
 *      Given an array of n duplicates or distinct integers sorted in ascending
 *      order, write a function that returns a Fixed Point in the array, if
 *      there is any Fixed Point present in the array, else returns -1. Fixed
 *      Point in an array is an index i such that arr[i] is equal to i. Note
 *      that integers in the array can be negative.
 *
 *   Execution: javac FindFixedPoint.java && java FindFixedPoint
 */
class FindFixedPoint
{
	// Main Function to find fixed
	// index using binary search
	public static int findFixedPoint(int arr[], int low,
									int high)
	{
		if (high < low)
			return -1;

		// low + (high - low) / 2
		int mid = (low + high) / 2;
		int midValue = arr[mid];

		if (mid == arr[mid])
			return mid;

		// Search left.
		int leftindex = Math.min(mid - 1, midValue);
		int left = findFixedPoint(arr, low, leftindex);

		if (left >= 0)
			return left;

		// Search right.
		int rightindex = Math.max(mid + 1, midValue);
		int right = findFixedPoint(arr, rightindex, high);

		return right;
	}

	public static void main(String[] args)
	{
		// input 1
		int arr[] = {-10, -5, 2, 2, 2,
					3, 4, 7, 9, 12, 13};

        assert findFixedPoint(arr, 0, arr.length - 1) == 2;

		// input 2
		int arr1[] = {-10, -1, 3, 3, 10,
						30, 30, 50, 100};

        assert findFixedPoint(arr1, 0, arr1.length - 1) == 3;

		System.out.println("All tests passed.");
	}
}
