/*
 *   Title: Stack from Queues
 *   Leetcode Link: https://leetcode.com/problems/implement-stack-using-queues/
 *
 *   Problem: Implement a LIFO stack with basic operations using 2 FIFO queues.
 *
 *   Execution: javac StackFromQueue.java && java -ea StackFromQueue
 */
import java.util.*;

class StackFromQueue {

    private Queue<Integer> queue;

    // Constructor
    public StackFromQueue() {
        this.queue = new LinkedList<>();
    }

    // Push an item onto the stack
    public void push(int x) {
        // We are going to just create a new queue here so we're using 2 queues
        // _at a time_. If we want to be more precise, we could allocate two
        // queues at the beginning and just alternate between which we're using
        // as the primary and secondary queues
        Queue<Integer> newQueue = new LinkedList<>();

        // Maintain our queue in stack order. To add an item to the end of the
        // queue we add that first before everything else
        newQueue.add(x);
        for (int i : queue) newQueue.add(i);

        // newQueue now contains all elements in proper order
        this.queue = newQueue;
    }

    // Remove the most recently added element from the stack
    public int pop() {
        // We've handled all the logic while pushing so this is easy
        return this.queue.remove();
    }

    // Return the top element of stack without removing it
    public int top() {
        return this.queue.peek();
    }

    // Return true if stack is empty
    public boolean empty() {
        return this.queue.size() == 0;
    }

    // Driver code
    public static void main(String[] args) {
        StackFromQueue stackFromQueue = new StackFromQueue();
        stackFromQueue.push(1);
        stackFromQueue.push(2);
        stackFromQueue.push(3);
        stackFromQueue.push(4);

        System.out.println(stackFromQueue.queue);
        stackFromQueue.pop();
        System.out.println(stackFromQueue.queue);

        // ADD YOUR TEST CASES HERE
    }
}
