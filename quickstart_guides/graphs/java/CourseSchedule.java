/*
 *   Title: Course schedule
 *
 *   Problem:
 *   There are a total of numCourses courses you have to take, labeled from 0 to
 *   numCourses-1.
 *
 *   Some courses may have prerequisites, for example to take course 0 you have
 *   to first take course 1, which is expressed as a pair: [0,1]
 *
 *   Given the total number of courses and a list of prerequisite pairs, is it
 *   possible for you to finish all courses?
 *
 *   Execution: javac CourseSchedule.java && java CourseSchedule
 */
import java.io.*;
import java.util.*;


public class CourseSchedule {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        if (numCourses <= 0) {
            return true;
        }

        if (prerequisites == null || prerequisites.length == 0) {
            return true;
        }

        // First transform the edge list to adj. list.
        Map<Integer, List<Integer>> adjList = new HashMap<>();
        for (int[] edge : prerequisites) {
            if (adjList.containsKey(edge[0])) {
                List<Integer> neighbors = adjList.get(edge[0]);
                neighbors.add(edge[1]);
                adjList.put(edge[0], neighbors);
            } else {
                List<Integer> neighbors = new ArrayList<Integer>();
                neighbors.add(edge[1]);
                adjList.put(edge[0], neighbors);
            }
        }

        int[] visited = new int[numCourses];
        // Check if the graph contains a circle, if yes, return false.
        for (int i = 0; i < numCourses; i++) {
            if (hasCircles(i, visited, adjList)) {
                return false;
            }
        }

        return true;
    }

    private boolean hasCircles(int vertexId, int[] visited, Map<Integer, List<Integer>> adjList) {
        if (visited[vertexId] == -1) {
            return true;
        }

        if (visited[vertexId] == 1) {
            return false;
        }

        visited[vertexId] = -1;

        List<Integer> neighbors = adjList.get(vertexId);
        if (neighbors != null) {
            for (int neighbor : neighbors) {
                if (hasCircles(neighbor, visited, adjList)) {
                    return true;
                }
            }
        }

        visited[vertexId] = 1;

        return false;
    }
    public static void main(String[] args) {
        CourseSchedule cs = new CourseSchedule();

        int[][] prerequisites = {{1, 0}};
        assert cs.canFinish(2, prerequisites) == true;
        System.out.println("Passed all test cases");
    }
}