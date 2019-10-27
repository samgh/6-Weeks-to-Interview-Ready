/*
 *   Title: Sort List
 *
 *   Problem:Sort a linked list in O(n log n) time using constant space
 *   complexity.
 *
 *   Execution: javac SortList.java && java SortList
 */
import java.util.*;


public class SortList {

    public static class ListNode {
        int val;
        ListNode next;
        ListNode(int x) { val = x; }
    }

    public static ListNode sortList(ListNode head) {
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        int n = 0;
        while (head != null) {
            head = head.next;
            n++;
        }
        
        for (int step = 1; step < n; step <<= 1) {
            ListNode prev = dummy;
            ListNode cur = dummy.next;
            while (cur != null) {
                ListNode left = cur;
                ListNode right = split(left, step);
                cur = split(right, step);
                prev = merge(left, right, prev);
            } 
        }
        
        return dummy.next;
    }
    
    private static ListNode split(ListNode head, int step) {
        if (head == null) return null;
    	
        for (int i = 1; head.next != null && i < step; i++) {
            head = head.next;
        }
        
        ListNode right = head.next;
        head.next = null;
        return right;
    }
    
    private static ListNode merge(ListNode left, ListNode right, ListNode prev) {
        ListNode cur = prev;
        while (left != null && right != null) {
            if (left.val < right.val) {
                cur.next = left;
                left = left.next;
            }
            else {
                cur.next = right;
                right = right.next;
            }
            cur = cur.next;
        }
        
        if (left != null) cur.next = left;
        else if (right != null) cur.next = right;
        while (cur.next != null) cur = cur.next;
        return cur;
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
        ListNode l1 = new ListNode(4);
        l1.next = new ListNode(2);
        l1.next.next = new ListNode(1);
        l1.next.next.next = new ListNode(3);

        ListNode expected_l1 = new ListNode(1);
        expected_l1.next = new ListNode(2);
        expected_l1.next = new ListNode(3);
        expected_l1.next = new ListNode(4);

        assert compareLists(sortList(l1), expected_l1) == true;

        ListNode l2 = new ListNode(1);
        l2.next = new ListNode(5);
        l2.next.next = new ListNode(3);
        l2.next.next.next = new ListNode(4);
        l2.next.next.next.next = new ListNode(0);

        ListNode expected_l2 = new ListNode(1);
        expected_l2.next = new ListNode(0); 
        expected_l2.next.next = new ListNode(3);
        expected_l2.next.next.next = new ListNode(4);
        expected_l2.next.next.next.next = new ListNode(5);

        assert compareLists(sortList(l2), expected_l2) == true;

        System.out.println("Passed all test cases");
    }
    
}
