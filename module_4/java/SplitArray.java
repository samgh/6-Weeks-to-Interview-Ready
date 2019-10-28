/*
 *   Title: Split array
 *
 *   Problem:
 *      Given an array which consists of non-negative integers and an integer m,
 *      you can split the array into m non-empty continuous subarrays.  Write an
 *      algorithm to minimize the largest sum among these m subarrays.

        Note: If n is the length of array, assume the following constraints are
        satisfied:

        1 ≤ n ≤ 1000 1 ≤ m ≤ min(50, n)
 *
 *   Execution: javac SplitArray.java && java SplitArray
 */
import java.util.*;


public class SplitArray {
    public static int splitArray(int[] nums, int m) {
        int max = 0; long sum = 0;
        for (int num : nums) {
            max = Math.max(num, max);
            sum += num;
        }
        if (m == 1) return (int)sum;
        //binary search
        long l = max; long r = sum;
        while (l <= r) {
            long mid = (l + r)/ 2;
            if (valid(mid, nums, m)) {
                r = mid - 1;
            } else {
                l = mid + 1;
            }
        }
        return (int)l;
    }
    public static boolean valid(long target, int[] nums, int m) {
        int count = 1;
        long total = 0;
        for(int num : nums) {
            total += num;
            if (total > target) {
                total = num;
                count++;
                if (count > m) {
                    return false;
                }
            }
        }
        return true;
    }
    public static void main(String[] args) {
        int[] nums = {7, 2, 5, 10, 8};
        int m = 2;
        assert splitArray(nums, m) == 18;

        System.out.println("Passed all test cases");
    }
    
}
