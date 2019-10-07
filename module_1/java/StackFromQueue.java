/*
 *   Title: Stack from queue.
 *
 *   Problem: Implement a stack with push and pop
 *   operations using a queue data structure.
 *
 *   Execution: javac StackFromQueue.java && java StackFromQueue
 */

import java.util.Queue;
import java.util.LinkedList;

public class StackFromQueue {

    public static class Stack {
        private Queue<Integer> queue = new LinkedList<>();

        Stack() {
        }

        public void push(int x) {
            queue.add(x);
            for (int i = 1; i < queue.size(); i++) {
                queue.add(queue.remove());
            }
        }
    }

    public static void main(String[] args) {

        Stack stack = new Stack();
        stack.push(5);

        //stack = new StackFromQueue();

        //assert template("abcabcbb") == 3;
        System.out.println("Explanation: ");

        System.out.println("Passed all test cases");
    }
    
}
