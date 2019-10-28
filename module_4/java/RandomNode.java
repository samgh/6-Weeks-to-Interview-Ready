/*
 *   Title: Linked list random node
 *
 *   Problem:
 *   Given a singly linked list, return a random node's value from the linked
 *   list. Each node must have the same probability of being chosen.
 *
 *   Follow up: What if the linked list is extremely large and its length is unknown
 *   to you? Could you solve this efficiently without using extra space?
 *
 *   Execution: javac RandomNode.java && java RandomNode
 */
import java.util.*;


public class RandomNode {
    ListNode head;
    Random random;

    public static class ListNode {
        int val;
        ListNode next;
        ListNode(int x) { val = x; }
    }

    public RandomNode(ListNode h) {
        head = h;       
        random = new Random();        
    }
    
    public int getRandom() {
        
        ListNode c = head;
        int r = c.val;
        for(int i=1;c.next != null;i++){
            
            c = c.next;
            if(random.nextInt(i + 1) == i) r = c.val;                        
        }
        
        return r;
    }
    public static boolean checkRandomNodeFunction(int random_value) {
        if (random_value == 1 || random_value == 2 || random_value == 3) {
            return true;
        }
        return false;
    }
    

    public static void main(String[] args) {
        // Init a singly linked list [1,2,3].
        ListNode head = new ListNode(1);
        head.next = new ListNode(2);
        head.next.next = new ListNode(3);
        RandomNode r_node = new RandomNode(head);
        
        // getRandom() should return either 1, 2, or 3 randomly. Each element
        // should have equal probability of returning.
        int rand_node = r_node.getRandom();
        System.out.println(rand_node);
        assert checkRandomNodeFunction(rand_node) == true;

        System.out.println("Passed all test cases");
    }
    
}
