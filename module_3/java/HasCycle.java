/*
 *   Title: Has cycle
 *
 *   Problem:
 *      Given a linked list, determine if it has a cycle in it.
 *
 *      To represent a cycle in the given linked list, we use an integer pos which
 *      represents the position (0-indexed) in the linked list where tail connects to.
 *      If pos is -1, then there is no cycle in the linked list.
 *
 *   Code is adapted from https://geeksforgeeks.org/detect-loop-in-a-linked-list/
 *
 *   Execution: javac HasCycle.java && java HasCycle
 */
import java.util.*;


public class HasCycle {
    
    public static class LinkedList {

        static Node head; // head of list

        static class Node {
            int data;
            Node next;
            Node(int d) {
                data = d;
                next = null;
            }
        }

        /* Inserts a new Node at front of the list. */
        public static void push(int new_data) {
            /* 1 & 2: Allocate the Node &
                      Put in the data*/
            Node new_node = new Node(new_data);

            /* 3. Make next of new Node as head */
            new_node.next = head;

            /* 4. Move the head to point to new Node */
            head = new_node;
        }

        // Returns true if there is a loop in linked
        // list else returns false.
        public static boolean hasCycle(Node h) {
            HashSet<Node> s = new HashSet<Node>();
            while (h != null) {
                // If we have already has this node
                // in hashmap it means their is a cycle
                // (Because you we encountering the
                // node second time).
                if (s.contains(h))
                    return true;

                // If we are seeing the node for
                // the first time, insert it in hash
                s.add(h);

                h = h.next;
            }

            return false;
        }
    }

    public static void main(String[] args) {
        LinkedList llist = new LinkedList(); 
  
        llist.push(20); 
        llist.push(4); 
        llist.push(15); 
        llist.push(10); 
  
        llist.head.next.next.next.next = llist.head; 

        assert llist.hasCycle(llist.head) == true;
        System.out.println("Explanation: ");

        System.out.println("Passed all test cases");
    }
    
}
