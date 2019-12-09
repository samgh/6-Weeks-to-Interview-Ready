/*
 *   Title: Stack from queue.
 *
 *   Problem: Implement a stack with push and pop
 *   operations using a queue data structure.
 *
 *   Execution: javac StackFromQueue.java && java StackFromQueue
 */
import java.util.*; 
  
class StackFromQueue {  
    static Queue<Integer> queue = new LinkedList<Integer>();
    
    public static void push(int value) {
        int qSize = queue.size();
        queue.add(value);

        for (int i = 0; i < qSize; i++) {
            queue.add(queue.remove());
        }
    }

    public static void pop() {
        System.out.println("Element removed from stack is:" + queue.remove());
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
    }  
}  

