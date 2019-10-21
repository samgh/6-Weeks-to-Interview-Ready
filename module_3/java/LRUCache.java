/*
 *   Title: LRU Cache
 *
 *   Problem: 
 *     Design and implement a data structure for Least Recently Used
 *     (LRU) cache. It should support the following operations: get and put.
 *
 *     get(key) - Get the value (will always be positive) of the key if the key exists
 *     in the cache, otherwise return -1.  put(key, value) - Set or insert the value
 *     if the key is not already present. When the cache reached its capacity, it
 *     should invalidate the least recently used item before inserting a new item.
 *
 *     The cache is initialized with a positive capacity.
 *
 *   Execution: javac LRUCache.java && java LRUCache
 */
import java.util.*;

public class LRUCache {

    public static class Node {
        int key;
        int value;
        Node prev;
        Node next;

        public Node(int key, int value) {
            this.key = key;
            this.value = value;
        }
    }

    public static class Cache {
        Node head;
        Node tail;
        HashMap<Integer, Node> map = null;
        int cap = 0;

        public Cache(int capacity) {
            this.cap = capacity;
            this.map = new HashMap<>();
        }

        public int get(int key) {
            if(map.get(key) == null){
                return -1;
            }
            // Move to tail
            Node t = map.get(key);
     
            removeNode(t);
            offerNode(t);
     
            return t.value;
        }
 
        public void put(int key, int value) {
            if(map.containsKey(key)){
                Node t = map.get(key);
                t.value = value;
     
                // Move to tail
                removeNode(t);
                offerNode(t);
            } else {
                if(map.size()>=cap){
                    //delete head
                    map.remove(head.key);
                    removeNode(head);
                }
     
                // Add to tail
                Node node = new Node(key, value);
                offerNode(node);
                map.put(key, node);
            }
        }
     
        public void removeNode(Node n){
            if(n.prev != null) {
                n.prev.next = n.next;
            } else {
                head = n.next;
            }
     
            if(n.next!=null) {
                n.next.prev = n.prev;
            } else {
                tail = n.prev;
            }
        }
     
        public void offerNode(Node n){
            if(tail != null) {
                tail.next = n;
            }
     
            n.prev = tail;
            n.next = null;
            tail = n;
     
            if(head == null) {
                head = tail;   
            }
        }

    }

    public static void main(String[] args) {
        Cache cache = new Cache(2);
        cache.put(1, 1);
        cache.put(2, 2);
        assert cache.get(1) == 1;    // returns 1 (key found)
        System.out.println("Calling cache.get(1) returns " + Integer.toString(cache.get(1)));
        cache.put(3, 3);             // evicts key 2
        assert cache.get(2) == -1;   // returns -1 (not found)
        System.out.println("Calling cache.get(2) returns " + Integer.toString(cache.get(2)));
        cache.put(4, 4);             // evicts key 1
        assert cache.get(1) == -1;   // returns -1 (not found)
        System.out.println("Calling cache.get(1) returns " + Integer.toString(cache.get(1)));
        assert cache.get(3) == 3;    // returns 3
        System.out.println("Calling cache.get(3) returns " + Integer.toString(cache.get(3)));
        assert cache.get(4) == 4;    // returns 4
        System.out.println("Calling cache.get(4) returns " + Integer.toString(cache.get(4)));

        System.out.println("Passed all test cases");
    }
    
}
