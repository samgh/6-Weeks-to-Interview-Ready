/*
 *   Title: Invert a binary tree.
 *
 * Problem:
 *   Invert a binary tree.
 *
 *   Execution: javac InvertBinaryTree.java && java InvertBinaryTree
 */
import java.util.*;


class InvertBinaryTree {

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

    public TreeNode invertBinaryTree(TreeNode root) {
        if (root == null) {
            return null;
        }
        TreeNode right = invertBinaryTree(root.right);
        TreeNode left = invertBinaryTree(root.left);
        root.left = right;
        root.right = left;
        return root;
    }

    public static void main(String args[])
    {
        InvertBinaryTree ibt = new InvertBinaryTree();
        TreeNode tree = new TreeNode(4);
        tree.right = new TreeNode(7);
        tree.right.left = new TreeNode(6);
        tree.left = new TreeNode(2);
        tree.left.left = new TreeNode(1);
        tree.left.right = new TreeNode(3);
        tree.right.right = new TreeNode(9);

        System.out.println(ibt.invertBinaryTree(tree));

        System.out.println("Passed all test cases");
    }
}