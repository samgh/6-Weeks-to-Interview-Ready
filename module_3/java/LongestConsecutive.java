/*
 *   Title: Longest consecutive sequence
 *
 *   Problem:Given an unsorted array of integers, find the length of the
 *   longest consecutive elements sequence.
 *
 *   Your algorithm should run in O(n) complexity.
 *
 *   Execution: javac LongestConsecutive.java && java LongestConsecutive
 */
import java.util.*;


public class LongestConsecutive {
    private static boolean arrayContains(int[] arr, int num) {
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == num) {
                return true;
            }
        }
        return false;
    }

    public static int longestConsecutiveBF(int[] nums) {
        /* Brute-force implementation of longest consecutive sequence. */
        int longestStreak = 0;

        for (int num : nums) {
            int currentNum = num;
            int currentStreak = 1;

            while (arrayContains(nums, currentNum + 1)) {
                currentNum += 1;
                currentStreak += 1;
            }

            longestStreak = Math.max(longestStreak, currentStreak);
        }
        return longestStreak;
    }

    public static int longestConsecutiveSorting(int[] nums) {
        /* Sorting implementation of longest consecutive sequence. */
        if (nums.length == 0) {
            return 0;
        }

        Arrays.sort(nums);

        int longestStreak = 1;
        int currentStreak = 1;

        for (int i = 1; i < nums.length; i++) {
            if (nums[i] != nums[i-1]) {
                if (nums[i] == nums[i-1]+1) {
                    currentStreak += 1;
                }
                else {
                    longestStreak = Math.max(longestStreak, currentStreak);
                    currentStreak = 1;
                }
            }
        }
        return Math.max(longestStreak, currentStreak);
    }

    public static int longestConsecutiveHashSet(int[] nums) {
        /* Hash-set implementation of longest consecutive sequence. */
        Set<Integer> num_set = new HashSet<Integer>();
        for (int num : nums) {
            num_set.add(num);
        }

        int longestStreak = 0;

        for (int num : num_set) {
            if (!num_set.contains(num-1)) {
                int currentNum = num;
                int currentStreak = 1;

                while (num_set.contains(currentNum+1)) {
                    currentNum += 1;
                    currentStreak += 1;
                }

                longestStreak = Math.max(longestStreak, currentStreak);
            }
        }
        return longestStreak;
    }

    public static void main(String[] args) {
        int[] testArr = {100, 4, 200, 1, 3, 2};
        assert longestConsecutiveBF(testArr) == 4;
        assert longestConsecutiveSorting(testArr) == 4;
        assert longestConsecutiveHashSet(testArr) == 4;
        System.out.println("Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.");

        System.out.println("Passed all test cases");
    }
    
}
