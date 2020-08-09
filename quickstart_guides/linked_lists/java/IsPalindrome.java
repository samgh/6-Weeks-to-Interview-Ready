/*
 * Title: Is palindrome
 *
 * Problem:
 *  Check if linked list is a palindrome.
 *
 * Execution: javac IsPalindrome.java && java IsPalindrome
 */
import java.util.*;


class IsPalindrome {
    static ListNode head;

    public static class ListNode {
        int val;
        ListNode next;
        ListNode() {}
        ListNode(int val) { this.val = val; }
        ListNode(int val, ListNode next) { this.val = val; this.next = next; }
    }

    public static boolean isPalindrome(ListNode head) {
        if(head!=null) {
            List<Integer> s=new ArrayList<>();
            ListNode c=head;

            while(c!=null){
                s.add(c.val);
                c=c.next;
            }

            boolean isPalindrome=true;
            for(int i=0;i<s.size()/2+1;i++){
                if(s.get(i)!=s.get(s.size()-i-1)){
                    isPalindrome=false;
                    break;
                }
            }

            return isPalindrome;
        }else{
            return true;
        }
    }


    public static void main(String[] args) {
        IsPalindrome list1 = new IsPalindrome();
        list1.head = new ListNode(1);
        list1.head.next = new ListNode(2);

        assert list1.isPalindrome(list1.head) == false;

        IsPalindrome list2 = new IsPalindrome();
        list2.head = new ListNode(1);
        list2.head.next = new ListNode(2);
        list2.head.next.next = new ListNode(2);
        list2.head.next.next.next = new ListNode(1);

        assert list2.isPalindrome(list2.head) == true;

        System.out.println("All tests have passed.");

    }
}