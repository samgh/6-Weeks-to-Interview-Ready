/*
 *   Title: Count number of islands
 *
 *   Problem:Given a 2d grid map of '1's (land) and '0's (water), count the
 *   number of islands. An island is surrounded by water and is formed by
 *   connecting adjacent lands horizontally or vertically. You may assume all
 *   four edges of the grid are all surrounded by water.
 *
 *   Execution: javac NumIslands.java && java NumIslands
 */


public class NumIslands{
    private static int n;
    private static int m;

    public static int numIslands(char[][] grid) {
        int count = 0;
        n = grid.length;
        if (n == 0) return 0;
        m = grid[0].length;
        for (int i = 0; i < n; i++){
            for (int j = 0; j < m; j++)
                if (grid[i][j] == '1') {
                    DFSMarking(grid, i, j);
                    ++count;
                }
        }    
        return count;
    }

    public static void DFSMarking(char[][] grid, int i, int j) {
        if (i < 0 || j < 0 || i >= n || j >= m || grid[i][j] != '1') return;
        grid[i][j] = '0';
        DFSMarking(grid, i + 1, j);
        DFSMarking(grid, i - 1, j);
        DFSMarking(grid, i, j + 1);
        DFSMarking(grid, i, j - 1);
    }

    public static void main(String[] args) {
        char[][] testInput = new char[][]{
          {'1', '1', '1', '1', '0'},
          {'1', '1', '0', '1', '0'},
          {'1', '1', '0', '0', '0'},
          {'0', '0', '0', '0', '0'}
        };
        assert numIslands(testInput) == 1;

        System.out.println("Passed all test cases");
    }
    
}
