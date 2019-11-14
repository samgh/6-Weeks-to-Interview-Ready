/*
 *   Title: Container with Most Water
 *
 *   Problem:
 *   Given n non-negative integers a1, a2, ..., an , where each represents a
 *   point at coordinate (i, ai). n vertical lines are drawn such that the two
 *   endpoints of line i is at (i, ai) and (i, 0). Find two lines, which
 *   together with x-axis forms a container, such that the container contains
 *   the most water.

     Note: You may not slant the container and n is at least 2.
 *
 *   Execution: javac MaxArea.java && java MaxArea
 */
import java.util.*;


public class MaxArea {

    public static int maxAreaBruteForce(int[] height) {
        int maxarea = 0;
        for (int i = 0; i < height.length; i++)
            for (int j = i + 1; j < height.length; j++)
                maxarea = Math.max(maxarea, Math.min(height[i], height[j]) * (j - i));
        return maxarea;
    }

    public static int maxAreaPointer(int[] height) {
        int maxarea = 0, l = 0, r = height.length - 1;
        while (l < r) {
            maxarea = Math.max(maxarea, Math.min(height[l], height[r]) * (r - l));
            if (height[l] < height[r])
                l++;
            else
                r--;
        }
        return maxarea;
    }

    public static void main(String[] args) {
        int[] test_input = {1, 8, 6, 2, 5, 4, 8, 3, 7};
        assert maxAreaBruteForce(test_input) == 49;
        assert maxAreaPointer(test_input) == 49;

        System.out.println("Passed all test cases");
    }
}
