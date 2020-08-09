/*
 *   Title: Merge K sorted list
 *
 *   Problem:
 *      Merge k sorted linked lists and return it as one sorted list. Analyze
 *      and describe its complexity.
 *
 *   Execution: javac MergeKSorted.java && java MergeKSorted
 */
import java.util.*;


public class MergeKSorted {
    public static class ListNode {
        int val;
        ListNode next;
        ListNode(int x) { val = x; }
    }
    public static ListNode mergeKLists(ListNode[] lists) {
        if (lists==null || lists.length==0) return null;

        PriorityQueue<ListNode> queue= new PriorityQueue<ListNode>(lists.length, (a,b)-> a.val-b.val);

        ListNode dummy = new ListNode(0);
        ListNode tail=dummy;

        for (ListNode node:lists)
            if (node!=null)
                queue.add(node);

        while (!queue.isEmpty()){
            tail.next=queue.poll();
            tail=tail.next;

            if (tail.next!=null)
                queue.add(tail.next);
        }
        return dummy.next;
    }
    public static void main(String[] args) {

        ListNode test_1 = new ListNode(1);
        test_1.next = new ListNode(4);
        test_1.next.next = new ListNode(5);

        ListNode test_2 = new ListNode(1);
        test_2.next = new ListNode(3);
        test_2.next.next = new ListNode(4);

        ListNode test_3 = new ListNode(2);
        test_3.next = new ListNode(6);

        ListNode[] test_input = {test_1, test_2, test_3};

        System.out.println(mergeKLists(test_input));

        System.out.println("Passed all test cases");
    }

}
