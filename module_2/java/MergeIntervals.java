/*
 *   Title: Merge intevals
 *
 *   Problem: Given a collection of intervals, merge all overlapping intervals.
 *
 *   Execution: javac MergeIntervals.java && java MergeIntervals
 */
import java.util.*;
import java.util.Arrays;



public class MergeIntervals {

	public static int[][] mergeIntervals(int[][] intervals) {
		if (intervals.length <= 1)
			return intervals;

		// Sort by ascending starting point
		Arrays.sort(intervals, (i1, i2) -> Integer.compare(i1[0], i2[0]));

		List<int[]> result = new ArrayList<>();
		int[] newInterval = intervals[0];
		result.add(newInterval);
		for (int[] interval : intervals) {
			if (interval[0] <= newInterval[1]) // Overlapping intervals, move the end if needed
				newInterval[1] = Math.max(newInterval[1], interval[1]);
			else {                             // Disjoint intervals, add the new interval to the list
				newInterval = interval;
				result.add(newInterval);
			}
		}

		return result.toArray(new int[result.size()][]);
	}

    public static void main(String[] args) {
        int[][] testIn_1 = { { 1, 3 }, { 2, 6 }, {8, 10}, {15, 18} };
        int[][] testOut_1 = { {1, 6}, {8, 10}, {15, 18} };
        assert Arrays.equals(mergeIntervals(testIn_1), testOut_1);
        System.out.println("Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].");

        int[][] testIn_2 = { { 1, 4 }, {4, 5} };
        int[][] testOut_2 = { {1, 5} };
        assert Arrays.equals(mergeIntervals(testIn_2), testOut_2);
        System.out.println("Explanation: Intervals [1,4] and [4,5] are considered overlapping.");


        System.out.println("Passed all test cases");
    }
    
}
