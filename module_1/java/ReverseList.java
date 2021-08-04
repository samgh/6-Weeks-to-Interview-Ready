/*
 *   Title: Reverse Linked List
 *   Leetcode Link: https://leetcode.com/problems/reverse-linked-list/
 *
 *   Problem: Given a singly linked list, reverse the list.
 *
 *   Input:
 *      ListNode head   => The head of the linked list
 *   Output:
 *      ListNode        => The head of the reversed list
 *
 *   Execution: javac ReverseList.java && java -ea ReverseList
 */

import java.util.ArrayList;
import java.util.List;

public class ReverseList {

    /*
     * Basic node class
     */
    public static class ListNode {
        int val;
        ListNode next;

        ListNode(int x) {
            val = x;
        }
    }

    /*
     * Solution #1: Brute Force
     *
     * In this solution, we add all the nodes to an array, allowing us to easily
     * maintain order while swapping pointers.
     *
     * This is not recommended and for demonstrative purposes only.
     *
     * Time Complexity: O(n)
     * Space Complexity: O(n)
     */
    public static ListNode reverseListBF(ListNode head) {
        if (head == null) return head
        // We're going to add nodes to an array so we need to know how many
        // nodes there are
        int len = 0;
        ListNode curr = head;
        while (curr != null) {
            len++;
            curr = curr.next;
        }

        // Create an array that contains references to all the list nodes
        ListNode[] nodes = new ListNode[len];
        curr = head;
        int idx = 0;
        while (curr != null) {
            nodes[idx] = curr;
            idx++;
        }

        // Reverse pointers
        nodes[0].next = null;
        for (int i = 1; i < nodes.length; i++) {
            nodes[i].next = nodes[i-1];
        }

        return nodes[nodes.length - 1];
    }

    /*
     * Solution #2: Iterative
     *
     * Iterate over all the nodes and reverse pointers as we go
     *
     * Time Complexity: O(n)
     * Space Complexity: O(1)
     */
    public static ListNode reverseListIter(ListNode head) {
        ListNode prev = null;
        ListNode curr = head;

        // Iterate over the list and swap pointers as we go
        while (curr != null) {
            ListNode nextTemp = curr.next;
            curr.next = prev;
            prev = curr;
            curr = nextTemp;
        }
        return prev;
    }

    /*
     * Solution #3: Recursive
     *
     * Recursively reverse the remainder of the list and point current node to
     * the previous
     *
     * Time Complexity: O(n)
     * Space Complexity: O(n)
     */
    public static ListNode reverseListRec(ListNode head) {
        // If we're at the end of the list, just return head
        if (head == null || head.next == null) {
            return head;
        }

        // Reverse the list from head.next to the end
        ListNode rem = reverseListRec(head.next);

        // Point the last node of that reversed list to the current node
        head.next.next = head;
        head.next = null;
        return rem;
    }

    public static void main(String[] args) {
        ListNode l = new ListNode(1);
        l.next = new ListNode(2);
        l.next.next = new ListNode(3);
        l.next.next.next = new ListNode(4);

        ListNode r = reverseListIter(l);
        while (r != null) {
            System.out.println(r.val);
            r = r.next;
        }

        // ADD YOUR TESTS HERE

        System.out.println("Passed all test cases");
    }

}
