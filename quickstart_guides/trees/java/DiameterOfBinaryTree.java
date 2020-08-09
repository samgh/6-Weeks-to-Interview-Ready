/*
 *   Title: Diameter of binary tree
 *
 * Problem:
 *   Given a binary tree, you need to compute the length of the diameter of the
 *   tree. The diameter of a binary tree is the length of the longest path
 *   between any two nodes in a tree. This path may or may not pass through the
 *   root.
 *
 *
 *   Execution: javac DiameterOfBinaryTree.java && java DiameterOfBinaryTree
 */
import java.util.*;


class DiameterOfBinaryTree {

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

    int ans;
    public int diameterOfBinaryTree(TreeNode root) {
        ans = 1;
        depth(root);
        return ans - 1;
    }
    public int depth(TreeNode node) {
        if (node == null) return 0;
        int L = depth(node.left);
        int R = depth(node.right);
        ans = Math.max(ans, L+R+1);
        return Math.max(L, R) + 1;
    }
    public static void main(String args[])
    {
        DiameterOfBinaryTree d = new DiameterOfBinaryTree();
        TreeNode tree = new TreeNode(1);
        tree.right = new TreeNode(2);
        tree.right.left = new TreeNode(3);

        assert d.depth(tree) == 3;

        System.out.println("Passed all test cases");
    }
}