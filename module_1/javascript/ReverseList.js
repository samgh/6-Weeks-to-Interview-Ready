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
 *   Execution: node ReverseList.js
 */

 /*
  * Basic node class
  */
class ListNode {
    constructor(val, next) {
        this.val = val;
        this.next = next;
    }
}

/**
 * Solution #1: Brute Force
 *
 * In this solution, we add all the nodes to an array, allowing us to easily
 * maintain order while swapping pointers.
 *
 * This is not recommended and for demonstrative purposes only.
 *
 * Time Complexity: O(n)
 * Space Complexity: O(n)
 *
 * @param {ListNode} head
 * @return {ListNode}
 */
 var reverseListBF = function(head) {
     if (!head) return head;

     // Create an array that contains references to all the list nodes
     var curr = head;
     var nodes = [];
     while (curr) {
         nodes.push(curr);
         curr = curr.next;
     }

     // Reverse pointers
     nodes[0].next = null;
     for (var i = 1; i < nodes.length; i++) {
         nodes[i].next = nodes[i-1];
     }

     return nodes[nodes.length - 1];
 }

 /**
  * Solution #2: Iterative
  *
  * Iterate over all the nodes and reverse pointers as we go
  *
  * Time Complexity: O(n)
  * Space Complexity: O(1)
  *
  * @param {ListNode} head
  * @return {ListNode}
  */
var reverseListIter = function(head) {
    var prev = null;
    var curr = head;

    // Iterate over the list and swap pointers as we go
    while (curr != null) {
        var nextTemp = curr.next;
        curr.next = prev;
        prev = curr;
        curr = nextTemp;
    }
    return prev;
}

/**
 * Solution #3: Recursive
 *
 * Recursively reverse the remainder of the list and point current node to
 * the previous
 *
 * Time Complexity: O(n)
 * Space Complexity: O(n)
 *
 * @param {ListNode} head
 * @return {ListNode}
 */
var reverseListRec = function(head) {
    // If we're at the end of the list, just return head
    if (!head || !head.next) {
        return head;
    }

    // Reverse the list from head.next to the end
    var rem = reverseListRec(head.next);

    // Point the last node of that reversed list to the current node
    head.next.next = head;
    head.next = null;
    return rem;
}

var tester = function() {
    var l = new ListNode(1);
    l.next = new ListNode(2);
    l.next.next = new ListNode(3);
    l.next.next.next = new ListNode(4);

    var r = reverseListRec(l);
    while (r) {
        console.log(r.val);
        r = r.next;
    }

    // ADD YOUR TESTS HERE
}

tester();
