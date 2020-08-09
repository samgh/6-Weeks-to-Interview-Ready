/*
 * Title: Reorder List
 *
 * Problem:
 *    Given a singly linked list L: L0→L1→…→Ln-1→Ln,
 *   reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
 *
 *   You may not modify the values in the list's nodes, only nodes itself may be
 *   changed.
 *
 * Execution: javac ReorderList.java && java ReorderList
 */



public class ReorderList {

    // Private node class
    private static class Node {
        private int value;
        private Node next;

        private Node(int value) {
            this.value = value;
        }
    }
   public static void reorderList(Node head) {
        if (head != null && head.next != null) {
             step(head, head);
        }
    }

    Node step(Node l, Node r) {
        if (r.next == null) { // reached right most position
            if (l.next != r) { // list has more than two elements
                Node temp = l.next;
                l.next = r;
                r.next = temp;
                return temp;
            }
            return null;
        } else {
            Node newL = step(l, r.next);

            if (newL == null) { // we're already done
                return null;
            }
            if (newL == r) { // odd number of nodes, meet in the middle
                newL.next = null; // terminate the list
                return null;
            }
            else if (newL.next == r) { // even number of nodes, meet back to back
                r.next = null; // terminate the list
                return null;
            } else {    // update middle of the string
                Node temp = newL.next;
                newL.next = r;
                r.next = temp;
                return temp;
            }
        }
    }

    public static void main(String[] args) {
        Node n = new Node(1);
        n.next = new Node(2);
        n.next.next = new Node(3);
        n.next.next.next = new Node(4);
        n.next.next.next.next = new Node(5);

    }
}