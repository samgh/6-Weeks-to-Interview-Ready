/*
 * Title: Array Combinations
 *
 * Problem:
 *  Given two strings, write a function that determines the minimum edit
 * distance between the two strings. You can insert and modify characters.
 * 
 * eg.
 * editDistance("ABCD", "ACBD") = 2 (ABCD->ACCD->ACBD)
 * editDistance("AC", "ABCD") = 2 (AC->ABC->ABCD) 
 * 
 * Execution: javac EditDistance.java && java EditDistance
 */

public class EditDistance {
    
    // Brute force solution.
    public static int bruteForceEditDistance(String s1, String s2) {
        return bruteForceEditDistance(s1, s2, 0, 0);
    }
    
    // Overloaded recursive method.
    private static int bruteForceEditDistance(String s1, String s2, int i, int j) {
        if (i == s1.length()) return s2.length() - j;
        if (j == s2.length()) return s1.length() - i;
        
        // We can swap the characters if they're unequal or do nothing otherwise
        int min = bruteForceEditDistance(s1, s2, i+1, j+1);
        if (s1.charAt(i) != s2.charAt(j)) min++;
        
        // We can insert a character into s1 or s2.
        min = Math.min(min, bruteForceEditDistance(s1, s2, i+1, j) + 1);
        min = Math.min(min, bruteForceEditDistance(s1, s2, i, j+1) + 1);
        return min;
    }
    
    // Top-down dynamic solution.
    public static int topDownEditDistance(String s1, String s2) {
        int[][] dp = new int[s1.length() + 1][s2.length() + 1];
        for (int i = 0; i < dp.length; i++) {
            for (int j = 0; j < dp[0].length; j++) {
                dp[i][j] = -1;
            }
        }
        return topDownEditDistance(s1, s2, 0, 0, dp);
    }
    
    // Overloaded recursive method.
    private static int topDownEditDistance(String s1,
                                           String s2,
                                           int i,
                                           int j,
                                           int[][] dp) {
        if (dp[i][j] == -1) {
            if (i == s1.length()) return s2.length() - j;
            if (j == s2.length()) return s1.length() - i;
            
            int min = topDownEditDistance(s1, s2, i+1, j+1, dp);
            if (s1.charAt(i) != s2.charAt(j)) min++;
            
            min = Math.min(min, topDownEditDistance(s1, s2, i+1, j, dp) + 1);
            min = Math.min(min, topDownEditDistance(s1, s2, i, j+1, dp) + 1);
            dp[i][j] = min;
        }
        return dp[i][j];
    }
    
    // Bottom-up dynamic solution
    private static int bottomUpEditDistance(String s1, String s2) {
        int[][] dp = new int[s1.length() + 1][s2.length() + 1];
        for (int i = 0; i < dp.length; i++) {
            for (int j = 0; j < dp[0].length; j++) {
                if (i == 0) {
                    dp[i][j] = j;
                } else if (j == 0) {
                    dp[i][j] = i;
                } else {
                    int min = dp[i-1][j-1];
                    if (s1.charAt(i-1) != s2.charAt(j-1)) min++;
                    
                    min = Math.min(min, dp[i-1][j] + 1);
                    min = Math.min(min, dp[i][j-1] + 1);
                    dp[i][j] = min;
                }
            }
        }
        
        return dp[s1.length()][s2.length()];
    }
    
    // Sample testcases
    public static void main(String[] args) {
        (new TestCase("A", "A", 0)).run();
        (new TestCase("A", "B", 1)).run();
        (new TestCase("ABC", "ACB", 2)).run();
        (new TestCase("AC", "ABCD", 2)).run();
        (new TestCase("", "ABCD", 4)).run();
        System.out.println("Passed all test cases");
    }
    
    // Class for defining and running test cases
    private static class TestCase {
        private String s1;
        private String s2;
        private int output;
        
        private TestCase(String s1, String s2, int output) {
            this.s1 = s1;
            this.s2 = s2;
            this.output = output;
        }
        
        private void run() {
            assert bruteForceEditDistance(s1, s2) == output:
                "bruteForceEditDistance failed for input = " + s1 + " " + s2;
            assert topDownEditDistance(s1, s2) == output:
                "topDownEditDistance failed for input = " + s1 + " " + s2;
            assert bottomUpEditDistance(s1, s2) == output:
                "bottomUpEditDistance failed for input = " + s1 + " " + s2;
        }
    }
}