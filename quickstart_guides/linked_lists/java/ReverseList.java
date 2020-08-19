/*
 *   Title: Reverse List.
 *
 *   Problem:
 *      Reverse a singly linked list.
 *
 *   Execution: javac ReverseList.java && java ReverseList
 */

import java.util.ArrayList;
import java.util.List;


public class ReverseList {

    public static class ListNode {
        int val;
        ListNode next;
        ListNode(int x) {
            val = x;
        }
    }

    public static List<Integer> printList(ListNode n) {
        List<Integer> list = new ArrayList<>();
        while (n != null) {
            list.add(n.val);
            n = n.next;
        }
        return list;
    }

    public static ListNode reverseListIterative(ListNode head) {
        /* Iterative algorithm to reverse nodes in linked list. 
            Time complexity: O(n).
            Space complexity: O(1).
         */
        ListNode prev = null;
        ListNode curr = head;

        // Keep going until the head node is null, that is, 
        // keep going until we reach the end of the list.
        while (curr != null) {
            ListNode nextTemp = curr.next;
            curr.next = prev;
            prev = curr;
            curr = nextTemp;
        }
        return prev;
    }

    public static ListNode reverseListRecursive(ListNode head) {
        /* Recursive algorithm to reverse nodes in linked list. 
            Time complexity: O(n).
            Space complexity: O(n).
         */
        if (head == null || head.next == null) {
            return head;
        }
        ListNode p = reverseListRecursive(head.next);
        head.next.next = head;
        head.next = null;
        return p;
    }

    public static void main(String[] args) {

        ListNode input_1 = new ListNode(1);
        input_1.next = new ListNode(2);
        input_1.next.next = new ListNode(3);
        input_1.next.next.next = new ListNode(4);
        input_1.next.next.next.next = new ListNode(5);

        ListNode expected_output_1 = new ListNode(5);
        expected_output_1.next = new ListNode(4);
        expected_output_1.next.next = new ListNode(3);
        expected_output_1.next.next.next = new ListNode(2);
        expected_output_1.next.next.next.next = new ListNode(1);

        List<Integer> list_expected_output_1 = printList(expected_output_1);
        List<Integer> list_output_iterative_1 = printList(reverseListIterative(input_1));
        List<Integer> list_output_recursive_1 = printList(reverseListRecursive(input_1));

        if (list_expected_output_1.equals(list_output_iterative_1)) {
            System.out.println("Passed reverseListIterative: converted 1->2->3->4->5 to 5->4->3->2->1");
        } else {
            System.out.println("Failed reverseListIterative for input: 1->2->3->4->5.");
        } 

        System.out.println("Passed all test cases");
    }
    
}
