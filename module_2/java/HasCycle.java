/*
 *   Title: Has Cycle
 *   Leetcode Link: https://leetcode.com/problems/linked-list-cycle/
 *
 *   Problem: Given a linked list, determine if it contains a cycle.
 *
 *   Input:
 *      Node n  => List head
 *   Output:
 *      boolean => True if the list contains a cycle
 *
 *   Execution: javac HasCycle.java && java -ea HasCycle
 */

import java.util.*;

public class HasCycle {

    // Simple Node class
    public static class Node {
        int val;
        Node next;
    }

    /*
     * Solution #1: Using extra memory
     *
     * We'll store all the nodes into a set. Then for each node we visit
     * we check whether we've already visited that node.
     *
     * Time Complexity: O(n)
     * Space Complexity: O(n)
     */
    public static boolean hasCycleExtraSpace(Node n) {
        // Set to store nodes we've already visited
        Set<Node> visited = new HashSet<>();

        // Keep looping until we get to the end of the list or see a node
        // we've already seen
        while (n != null) {
            if (visited.contains(n)) return true;
            visited.add(n);
            n = n.next;
        }

        // If we get here it means we reached the end of the list (no cycle)
        return false;
    }

    /*
     * Solution #2: No extra memory
     *
     * In this algorithm we use 2 pointers moving at different speeds. If there
     * is a cycle, the fast pointer should catch up to the slow pointer.
     * Otherwise, if the fast pointer reaches the end, there's no cycle
     *
     * Time Complexity: O(n)
     * Space Complexity: O(1)
     */
    public static boolean hasCycle(Node n) {
        if (n == null) return false;
        Node fast = n.next, slow = n;

        // Keep looping through and check if the fast and slow pointers overlap
        while (fast != null && fast.next != null) {
            if (fast == slow) return true;

            // Fast pointer moves 2x each loop, slow moves 1x
            fast = fast.next.next;
            slow = slow.next;
        }

        return false;
    }


    public static void main(String[] args) {
        Node list = new Node();
        list.next = new Node();
        list.next.next = new Node();

        assert !hasCycle(list);

        list.next.next.next = list;
        assert hasCycle(list);

        // ADD YOUR TEST CASES HERE

        System.out.println("Passed all test cases");
    }

}
