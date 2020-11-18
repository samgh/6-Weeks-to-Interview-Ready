/*
 *   Title: Network Delay
 *
 *   Problem:
 *   There are N network nodes, labelled 1 to N.
 *
 *   Given times, a list of travel times as directed edges times[i] = (u, v, w),
 *   where u is the source node, v is the target node, and w is the time it
 *   takes for a signal to travel from source to target.
 *
 *   Now, we send a signal from a certain node K. How long will it take for all
 *   nodes to receive the signal? If it is impossible, return -1.
 *
 *   Execution: javac NetworkDelay.java && java NetworkDelay
 */
import java.io.*;
import java.util.*;


public class NetworkDelay {
    Map<Integer, Integer> dist;

     public int networkDelayTime(int[][] times, int N, int K) {
        Map<Integer, List<int[]>> graph = new HashMap();
        for (int[] edge: times) {
            if (!graph.containsKey(edge[0]))
                graph.put(edge[0], new ArrayList<int[]>());
            graph.get(edge[0]).add(new int[]{edge[2], edge[1]});
        }

        dist = new HashMap();
        for (int node = 1; node <= N; ++node)
            dist.put(node, Integer.MAX_VALUE);

        dfs(graph, K, 0);
        int ans = 0;
        for (int cand: dist.values()) {
            if (cand == Integer.MAX_VALUE) return -1;
            ans = Math.max(ans, cand);
        }
        return ans;
    }

    public void dfs(Map<Integer, List<int[]>> graph, int node, int elapsed) {
        if (elapsed >= dist.get(node)) return;
        dist.put(node, elapsed);
        if (graph.containsKey(node))
            for (int[] info: graph.get(node))
                dfs(graph, info[1], elapsed + info[0]);
    }

    public static void main(String[] args) {
        int[][] times = {{2, 1, 1}, {2, 3, 1}, {3, 4, 1}};

        NetworkDelay net = new NetworkDelay();
        assert net.networkDelayTime(times, 4, 2) == 2;

        System.out.println("Passed all test cases");
    }
}
