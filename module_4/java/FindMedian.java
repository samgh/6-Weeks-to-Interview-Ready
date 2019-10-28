/*
 *   Title: Find median
 *
 *   Problem:
     Median is the middle value in an ordered integer list. If the size of
     the list is even, there is no middle value. So the median is the mean
     of the two middle value.

    For example, [2,3,4], the median is 3

    [2,3], the median is (2 + 3) / 2 = 2.5

    Design a data structure that supports the following two operations:

    void addNum(int num) - Add a integer number from the data stream to the
    data structure.  double findMedian() - Return the median of all elements so
    far.
 *
 *   Execution: javac FindMedian.java && java FindMedian
 */
import java.util.*;


public class FindMedian {
    List<Integer> store;

    public FindMedian() {
        store = new ArrayList<Integer>();
    }

    public void addNum(int n) {
        store.add(n);
    }

    public double findMedian() {
        Collections.sort(store);
        int n = store.size();
        if ((n & 1) == 1) {
            return store.get(n / 2);
        } else {
            return (store.get(n/2-1) + store.get(n/2))*0.5;
        }
    }

    public static void main(String[] args) {
        FindMedian obj = new FindMedian();
        
        obj.addNum(1);
        obj.addNum(2);
        assert obj.findMedian() == 1.5;
        obj.addNum(3);
        assert obj.findMedian() == 2;

        System.out.println("Passed all test cases");
    }
    
}
