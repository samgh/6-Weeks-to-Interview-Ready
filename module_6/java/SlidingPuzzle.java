/*
 *   Title: Sliding puzzle
 *
 *   Problem:
 *   On a 2x3 board, there are 5 tiles represented by the integers 1 through 5,
 *   and an empty square represented by 0.

     A move consists of choosing 0 and a 4-directionally adjacent number and
     swapping it.

     The state of the board is solved if and only if the board is [[1,2,3],[4,5,0]].

     Given a puzzle board, return the least number of moves required so that the
     state of the board is solved. If it is impossible for the state of the board to
     be solved, return -1.
 *
 *   Execution: javac SlidingPuzzle.java && java SlidingPuzzle
 */
import java.util.*;


public class SlidingPuzzle {
    public static int slidingPuzzle(int[][] board) {
        String target = "123450";
        String start = "";
        for (int i = 0; i < 2; i++) {
            for (int j = 0; j < 3; j++) {
                start += board[i][j];
            }
        }

        Deque<String> q = new ArrayDeque<>();
        Set<String> seen = new HashSet<>();
        int[][] dirs = new int[][]{{1, 3}, {0, 2, 4}, {1, 5}, {0, 4}, {1, 3, 5}, {2, 4}};

        q.add(start);
        seen.add(start);
        int move = 0;
        while (!q.isEmpty()) {
            int size = q.size();
            for (int i = 0; i < size; i++) {
                start = q.poll();
                if (start.equals(target))
                    return move;
                int zero = start.indexOf('0');
                for (int j :
                        dirs[zero]) {
                    String tmp = swap(start, zero, j);
                    if (seen.add(tmp))
                        q.add(tmp);
                }
            }
            move++;
        }
        return -1;
    }

    private static String swap(String str, int i, int j) {
        StringBuilder sb = new StringBuilder(str);
        sb.setCharAt(i, str.charAt(j));
        sb.setCharAt(j, '0');
        return sb.toString();
    }

    public static void main(String[] args) {
        int[][] board_1 = {{1,2, 3}, {4, 0, 5} };
        assert slidingPuzzle(board_1) == 1;
        System.out.println("Explanation: Swap the 0 and the 5 in one move.");

        int[][] board_2 = {{1, 2, 3}, {5, 4, 0} };
        assert slidingPuzzle(board_2) == -1;
        System.out.println("Explanation: No number of moves will make the baord solved.");

        int[][] board_3 = {{4, 1, 2}, {5, 0, 3} };
        assert slidingPuzzle(board_3) == 5;
        System.out.println("Explanation: 5 is the smallest number of moves that solves the board.");

        int[][] board_4 = {{3, 2, 4}, {1, 5, 0} };
        assert slidingPuzzle(board_4) == 14;

        System.out.println("Passed all test cases");
    }
    
}
