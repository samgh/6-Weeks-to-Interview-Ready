/*
 *   Title: Binary search
 *
 * Problem:
 *   Binary search is a search algorithm that finds the position of a target
 *   value within a sorted array. Binary search compares the target value to the
 *   middle element of the array.
 *
 *   If they are not equal, the half in which the target cannot lie is
 *   eliminated and the search continues on the remaining half, again taking the
 *   middle element to compare to the target value, and repeating this until the
 *   target value is found. If the search ends with the remaining half being
 *   empty, the target is not in the array.
 *
 *   Execution: javac BinarySearch.java && java BinarySearch
 */
import java.util.Arrays;


public class BinarySearch {
    // Returns index of x if it is present in arr[l..r], else return -1.
    public static int binarySearch(int arr[], int l, int r, int x)
    {
        if (r >= l) {
            int mid = l + (r - l) / 2;

            // If the element is present at the middle itself.
            if (arr[mid] == x)
                return mid;

            // If element is smaller than mid, then it can only be present in
            // left subarray.
            if (arr[mid] > x)
                return binarySearch(arr, l, mid - 1, x);

            // Else the element can only be present in right subarray.
            return binarySearch(arr, mid + 1, r, x);
        }

        // We reach here when element is not present in array.
        return -1;
    }

    public static void main(String[] args) {

        BinarySearch ob = new BinarySearch();
        int arr[] = { 2, 3, 4, 10, 40 };
        int n = arr.length;
        int x = 10;
        int result = ob.binarySearch(arr, 0, n - 1, x);
        assert result == 10;

        System.out.println("Passed all test cases");
    }

}
