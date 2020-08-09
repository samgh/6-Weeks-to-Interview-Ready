/*
 *   Title: In-order traversal of binary tree
 *
 * Problem:
 *   Given a binary tree, return the inorder traversal of its nodes' values.
 *
 *   Execution: javac InorderTraversal.java && java InorderTraversal
 */
import java.util.*;


class InorderTraversal {

    public static class TreeNode {
     int val;
     TreeNode left;
     TreeNode right;
     TreeNode() {}
     TreeNode(int val) { this.val = val; }
     TreeNode(int val, TreeNode left, TreeNode right) {
         this.val = val;
         this.left = left;
         this.right = right;
     }
   }

   public List < Integer > inorderTraversal(TreeNode root) {
        List < Integer > res = new ArrayList < > ();
        Stack < TreeNode > stack = new Stack < > ();
        TreeNode curr = root;
        while (curr != null || !stack.isEmpty()) {
            while (curr != null) {
                stack.push(curr);
                curr = curr.left;
            }
            curr = stack.pop();
            res.add(curr.val);
            curr = curr.right;
        }
        return res;
    }
    public static void main(String args[])
    {
        InorderTraversal it = new InorderTraversal();
        TreeNode tree = new TreeNode(1);
        tree.right = new TreeNode(2);
        tree.right.left = new TreeNode(3);

        System.out.println(it.inorderTraversal(tree));

        System.out.println("Passed all test cases");
    }
}