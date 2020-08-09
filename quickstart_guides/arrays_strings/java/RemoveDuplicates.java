/*
 * Title: Remove duplicates
 *
 * Problem:
 *    Given a sorted array nums, remove the duplicates in-place such that each
 *   element appear only once and return the new length.
 *
 *   Do not allocate extra space for another array, you must do this by modifying
 *   the input array in-place with O(1) extra memory. *
 *
 *   Execution: javac RemoveDuplicates.java && java RemoveDuplicates
 */


public class RemoveDuplicates {
    public static long removeDuplicates(int[] nums) {
        if (nums.length == 0) {
            return 0;
        }
        int i = 0;
        for (int j = 1; j < nums.length; j++) {
            if (nums[j] != nums[i]) {
                i++;
                nums[i] = nums[j];
            }
        }
        return i + 1;
    }

    public static void main(String[] args) {
        int[] arr_1 = {1, 1, 2};
        assert removeDuplicates(arr_1) == 2;

        int[] arr_2 = {0, 0, 1, 1, 1, 2, 2, 3, 3, 4};
        assert removeDuplicates(arr_2) == 5;

        System.out.println("Passed all test cases");
    }
    
}
