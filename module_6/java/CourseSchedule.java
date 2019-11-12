/*
 *   Title: Course schedule
 *
 *   Problem:
 *   There are a total of n courses you have to take, labeled from 0 to n-1.

     Some courses may have prerequisites, for example to take course 0 you have to
     first take course 1, which is expressed as a pair: [0,1]

     Given the total number of courses and a list of prerequisite pairs, is it
     possible for you to finish all courses?
 *
 *   Execution: javac CourseSchedule.java && java CourseSchedule
 */
import java.util.*;


public class CourseSchedule {

    public static boolean canFinish(int n, int[][] a) {
        Map<Integer, List<Integer>> g = new HashMap();
        for(int[] i : a) {
            int k = i[1];
            List<Integer> cs = g.containsKey(k) ? g.get(k) : new ArrayList();
            cs.add(i[0]);
            g.put(k, cs);
        }

        Set<Integer> visited = new HashSet();
        for(int k : g.keySet()) {
            int c = helper(n, k, g, visited, new HashSet());
            if(c == -1) {
                return false;
            }

            if(c == n) {
                return true;
            }
        }

        return true;
    }

    public static int helper(int n, int k, Map<Integer, List<Integer>> g,
                       Set<Integer> visited, Set<Integer> visiting) {
        if(visiting.contains(k)) {
            return -1;
        }

        if(visited.contains(k)) {
            return 0;
        }

        int count = 1;

        if(g.containsKey(k)) {
            visiting.add(k);
            List<Integer> cs = g.get(k);
            for(int i : cs) {
                if(count >= n) {
                    return count;
                }
                int t = helper(n, i, g, visited, visiting);
                if(t < 0) {
                    return -1;
                }
                count += t;
            }
            visiting.remove(k);
        }

        visited.add(k);

        return count;
    }

    public static void main(String[] args) {
        int[][] test_input_1 = {{1, 0}};
        assert canFinish(2, test_input_1) == true;
        System.out.println("Explanation: There are a total of 2 courses to take. To take course 1 you should have finsihed course 0. So it is possible.");

        int[][] test_input_2 = {{1, 0}, {0, 1}};
        assert canFinish(2, test_input_2) == false;
        System.out.println("Explanation: There are  a total of 2 courses to take. To take course 1 you should have finished course 0 and to take course 0 you should also have finished course 1. So it is impossible");

        System.out.println("Passed all test cases");
    }
    
}
