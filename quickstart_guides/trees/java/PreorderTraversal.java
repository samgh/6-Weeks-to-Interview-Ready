/*
 *   Title: Pre-order traversal of binary tree
 *
 * Problem:
 *   Given a binary tree, return the preorder traversal of its nodes' values.
 *
 *   Execution: javac PreorderTraversal.java && java PreorderTraversal
 */
import java.util.*;


class PreorderTraversal {

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

   public List<Integer> preorderTraversal(TreeNode root) {
        List<Integer> list = new ArrayList<>();
        return porder(root, list);
    }

    public List<Integer> porder(TreeNode root, List<Integer> list) {
        if(root == null) return list;
        list.add(root.val);
        porder(root.left, list);
        porder(root.right, list);
        return list;
    }

    public static void main(String args[])
    {
        PreorderTraversal pt = new PreorderTraversal();
        TreeNode tree = new TreeNode(1);
        tree.right = new TreeNode(2);
        tree.right.left = new TreeNode(3);

        System.out.println(pt.preorderTraversal(tree));

        System.out.println("Passed all test cases");
    }
}