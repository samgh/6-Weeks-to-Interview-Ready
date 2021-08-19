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
 *   Execution: node HasCycle.js
 */

// Simple Node class
function Node(val) {
    this.val = val;
    this.next = null;
}

/**
 * Solution #1: Using extra memory
 *
 * We'll store all the nodes into a set. Then for each node we visit
 * we check whether we've already visited that node.
 *
 * Time Complexity: O(n)
 * Space Complexity: O(n)
 *
 * @param{Node} n
 * @return{boolean}
 */
var hasCycleExtraSpace = function(n) {
    // Set to store nodes we've already visited
    var visited = new Set();

    // Keep looping until we get to the end of the list or see a node
    // we've already seen
    while (n != null) {
        if (visited.has(n)) return true;
        visited.add(n);
        n = n.next;
    }

    // If we get here it means we reached the end of the list (no cycle)
    return false;
}

/**
 * Solution #2: No extra memory
 *
 * In this algorithm we use 2 pointers moving at different speeds. If there
 * is a cycle, the fast pointer should catch up to the slow pointer.
 * Otherwise, if the fast pointer reaches the end, there's no cycle
 *
 * Time Complexity: O(n)
 * Space Complexity: O(1)
 *
 * @param{Node} n
 * @return{boolean}
 */
var hasCycle = function(n) {
    if (n == null) return false;
    var fast = n.next, slow = n;

    // Keep looping through and check if the fast and slow pointers overlap
    while (fast != null && fast.next != null) {
        if (fast == slow) return true;

        // Fast pointer moves 2x each loop, slow moves 1x
        fast = fast.next.next;
        slow = slow.next;
    }

    return false;
}

var tester = function() {
    var list = new Node(1);
    list.next = new Node(2);
    list.next.next = new Node(3);

    console.assert(hasCycle(list) === false);

    list.next.next.next = list;

    console.assert(hasCycle(list) === true);

    // ADD YOUR TEST CASES HERE
}

tester();
