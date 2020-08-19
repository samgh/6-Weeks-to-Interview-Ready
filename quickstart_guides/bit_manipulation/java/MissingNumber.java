/*
*    Title: Missing number
*
*    Problem:
*        Given an array containing n distinct numbers taken from 0, 1, 2, ..., n,
*        find the one that is missing from the array.
*
*    Execution: javac MissingNumber.java && java MissingNumber
*/
import java.util.*;


public class MissingNumber {
    public static int missingNumberSorting(int[] nums) {
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

    public static int missingNumberHashSet(int[] nums) {
        Set<Integer> numSet = new HashSet<Integer>();
        for (int num : nums) numSet.add(num);

        int expectedNumCount = nums.length + 1;
        for (int number = 0; number < expectedNumCount; number++) {
            if (!numSet.contains(number)) {
                return number;
            }
        }
        return -1;
    }

    public static int missingNumberBitManip(int[] nums) {
        int missing = nums.length;
        for (int i = 0; i < nums.length; i++) {
            missing ^= i ^ nums[i];
        }
        return missing;
    }

    public static void main(String[] args) {

        int[] testInput1 = {3, 0, 1};
        assert missingNumberSorting(testInput1) == 2;
        assert missingNumberHashSet(testInput1) == 2;
        assert missingNumberBitManip(testInput1) == 2;

        int[] testInput2 = {9, 6, 4, 2, 3, 5, 7, 0, 1};
        assert missingNumberSorting(testInput2) == 8;
        assert missingNumberHashSet(testInput2) == 8;
        assert missingNumberBitManip(testInput2) == 8;

        System.out.println("Passed all test cases");
    }
}
