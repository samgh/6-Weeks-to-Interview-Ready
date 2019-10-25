/*
 *   Title: Missing number
 *
 *   Problem:Given an array containing n distinct numbers taken from 0, 1, 2,
 *   ..., n, find the one that is missing from the array.
 *
 *   Execution: javac MissingNumber.java && java MissingNumber
 */
import java.util.*;


public class MissingNumber {
    public static int missingNumber(int[] nums) {
        Arrays.sort(nums);

        // Ensure that n is at the last index
        if (nums[nums.length-1] != nums.length) {
            return nums.length;
        }
        // Ensure that 0 is at the first index
        else if (nums[0] != 0) {
            return 0;
        }

        // If we get here, then the missing number is on the range (0, n)
        for (int i = 1; i < nums.length; i++) {
            int expectedNum = nums[i-1] + 1;
            if (nums[i] != expectedNum) {
                return expectedNum;
            }
        }

        // Array was not missing any numbers
        return -1;
    }
    public static void main(String[] args) {
        int[] test_input_1 = {3, 0, 1};
        assert missingNumber(test_input_1) == 2;

        int[] test_input_2 = {9, 6, 4, 2, 3, 5, 7, 0, 1};
        assert missingNumber(test_input_2) == 8;

        System.out.println("Passed all test cases");
    }
    
}
