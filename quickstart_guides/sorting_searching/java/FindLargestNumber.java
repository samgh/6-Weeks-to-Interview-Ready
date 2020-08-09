/*
 *   Title: Find largest number
 *
 *   Problem:
 *       Given a list of non negative integers, arrange them such that they form
 *       the largest number.
 *
 *
 *   Execution: javac FindLargestNumber.java && java FindLargestNumber
 */
 import java.util.*;


class FindLargestNumber {
    private static class LargerNumberComparator implements Comparator<String> {
        @Override
        public int compare(String a, String b) {
            String order1 = a + b;
            String order2 = b + a;
           return order2.compareTo(order1);
        }
    }

    public static String findLargestNumber(int[] nums) {
        // Get input integers as strings.
        String[] asStrs = new String[nums.length];
        for (int i = 0; i < nums.length; i++) {
            asStrs[i] = String.valueOf(nums[i]);
        }

        // Sort strings according to custom comparator.
        Arrays.sort(asStrs, new LargerNumberComparator());

        // If, after being sorted, the largest number is `0`, the entire number
        // is zero.
        if (asStrs[0].equals("0")) {
            return "0";
        }

        // Build largest number from sorted array.
        String largestNumberStr = new String();
        for (String numAsStr : asStrs) {
            largestNumberStr += numAsStr;
        }

        return largestNumberStr;
    }

	public static void main(String[] args)
	{
		// input 1
		int arr_1[] = {10, 2};

        assert findLargestNumber(arr_1) == "210";

		// input 2
		int arr_2[] = {3, 30, 34, 5, 9};

        assert findLargestNumber(arr_2) == "9534330";


		System.out.println("All tests passed.");
	}
}
