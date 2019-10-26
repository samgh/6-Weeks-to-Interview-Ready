/*
 *   Title: Add two numbers
 *
 *   Problem:
 *   You are given two non-empty linked lists representing two
 *   non-negative integers. The most significant digit comes first and each of
 *   their nodes contain a single digit. Add the two numbers and return it as a
 *   linked list.
 *
 *   You may assume the two numbers do not contain any leading zero, except the
 *   number 0 itself.
 *
 *   Follow up: What if you cannot modify the input lists? In other words, reversing
 *   the lists is not allowed.
 *
 *   Execution: javac AddTwoNumbers.java && java AddTwoNumbers
 */
import java.util.*;


public class AddTwoNumbers {

    public static class ListNode {
        int val;
        ListNode next;
        ListNode(int x) { val = x; }
    }

    public static ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        Stack<Integer> s1 = new Stack<Integer>();
        Stack<Integer> s2 = new Stack<Integer>();

        while(l1 != null) {
            s1.push(l1.val);
            l1 = l1.next;
        };
        while(l2 != null) {
            s2.push(l2.val);
            l2 = l2.next;
        }

        int sum = 0;
        ListNode list = new ListNode(0);
        while (!s1.empty() || !s2.empty()) {
            if (!s1.empty()) sum += s1.pop();
            if (!s2.empty()) sum += s2.pop();
            list.val = sum % 10;
            ListNode head = new ListNode(sum / 10);
            head.next = list;
            list = head;
            sum /= 10;
        }

        return list.val == 0 ? list.next : list;
    }

    public static boolean compareLists(ListNode l1, ListNode l2) {
        while (l1 != null) {
            if (l1.val != l2.val) {
                return false;
            }
            l1 = l1.next;
            l2 = l2.next;
        }
        return true;
    }


    public static void main(String[] args) {
        ListNode l1 = new ListNode(7);
        l1.next = new ListNode(2);
        l1.next.next = new ListNode(4);
        l1.next.next.next = new ListNode(3);

        ListNode l2 = new ListNode(5);
        l2.next = new ListNode(6);
        l2.next.next = new ListNode(4);

        ListNode out = addTwoNumbers(l1, l2);

        ListNode expected_out = new ListNode(7);
        expected_out.next = new ListNode(8);
        expected_out.next.next = new ListNode(0);
        expected_out.next.next.next = new ListNode(7);

        assert compareLists(out, expected_out) == true;

        System.out.println("Passed all test cases");
    }
}
