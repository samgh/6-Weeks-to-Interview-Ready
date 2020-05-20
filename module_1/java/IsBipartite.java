/*
 *   Title: Is graph bipartite
 *
 *   Problem:Given an undirected graph, return true if and only if it is
 *   bipartite.
 *  
 * Recall that a graph is bipartite if we can split it's set of nodes into two
 * independent subsets A and B such that every edge in the graph has one node in A
 * and another node in B.
 * 
 * The graph is given in the following form: graph[i] is a list of indexes j for
 * which the edge between nodes i and j exists.  Each node is an integer between 0
 * and graph.length - 1.  There are no self edges or parallel edges: graph[i] does
 * not contain i, and it doesn't contain any element twice.
 *
 *   Execution: javac IsBipartite.java && java IsBipartite
 */
import java.util.*;


public class IsBipartite {
    public static boolean isBipartite(int[][] graph) {
        int len = graph.length;
        int[] colors = new int[len];

        for (int i = 0; i < len; i++) {
            if (colors[i] != 0) continue;
            Queue<Integer> queue = new LinkedList<>();
            queue.offer(i);
            colors[i] = 1;   // Blue: 1; Red: -1.

            while (!queue.isEmpty()) {
                int cur = queue.poll();
                for (int next : graph[cur]) {
                    if (colors[next] == 0) {          // If this node hasn't been colored;
                        colors[next] = -colors[cur];  // Color it with a different color;
                        queue.offer(next);
                    } else if (colors[next] != -colors[cur]) {   // If it is colored and its color is different, return false;
                        return false;
                    }
                }
            }
        }

        return true;
    }

    public static void main(String[] args) {
        int[][] arr1 = { { 1, 3 }, { 0, 2 }, {1, 3}, {0, 2} };
        assert isBipartite(arr1) == true;

        int[][] arr2 = { {1, 2, 3}, { 0, 2 }, {0, 1, 3}, {0, 2} };
        assert isBipartite(arr2) == false;

        System.out.println("Passed all test cases");
    }
    
}
