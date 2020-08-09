/*
 * Title: Remove sorted duplicates
 *
 * Problem:
 *  Given a sorted linked list, delete all duplicates such that each element
 *  appear only once.
 *
 * Execution: javac RemoveUnsortedDuplicates.java && java RemoveUnsortedDuplicates
 */


class RemoveSortedDuplicates {

    static Node head;

    static class Node {

        int data;
        Node next;

        Node(int d) {
            data = d;
            next = null;
        }
    }

    public static Node removeDuplicates(Node head) {
        Node current = head;
        while (current != null && current.next != null) {
            if (current.next.data == current.data) {
                current.next = current.next.next;
            } else {
                current = current.next;
            }
        }
        return head;
    }

    void printList(Node node) {
        while (node != null) {
            System.out.print(node.data + " ");
            node = node.next;
        }
    }

    public static void main(String[] args) {
        RemoveSortedDuplicates list = new RemoveSortedDuplicates();
        list.head = new Node(1);
        list.head.next = new Node(1);
        list.head.next.next = new Node(2);

        System.out.println("Linked List before removing duplicates : \n ");
        list.printList(head);

        list.removeDuplicates(list.head);
        System.out.println("");
        System.out.println("Linked List after removing duplicates : \n ");
        list.printList(head);
    }
}