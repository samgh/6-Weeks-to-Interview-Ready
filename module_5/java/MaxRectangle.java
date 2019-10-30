/*
 *   Title: Max rectangle
 *
 *   Problem:
 *   Given a 2D binary matrix filled with 0's and 1's, find the largest
 *   rectangle containing only 1's and return its area.
 *
 *   Execution: javac MaxRectangle.java && java MaxRectangle
 */
import java.util.*;


public class MaxRectangle {

    public static int maxRectangle(char[][] matrix) {
        if (matrix.length <= 0) {
            return 0;
        }
        int n = matrix.length;
        int m = matrix[0].length;
        int[][] dp = new int[n][m];
        int maxArea = 0;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
            if (i == 0) {
              dp[i][j] = matrix[i][j] == '1' ? 1 : 0;
            }
            else {
              dp[i][j] = matrix[i][j] == '1' ? (dp[i-1][j] + 1) : 0;
            }
            int min = dp[i][j];

            for (int k = j; k >= 0; k--) {
              if (min == 0) {
                  break;
              }
              if (dp[i][k] < min) {
                  min = dp[i][k];
              }
              maxArea = Math.max(maxArea, min * (j - k + 1));
            }
          }
        }
        return maxArea;
  }

    public static void main(String[] args) {
        char[][] matrix = { {'1', '0', '1', '0', '0'},
                            {'1', '0', '1', '1', '1'},  
                            {'1', '1', '1', '1', '1'},
                            {'1', '0', '0', '1', '0'}};
        assert maxRectangle(matrix) == 6;

        System.out.println("Passed all test cases");
    }
}
