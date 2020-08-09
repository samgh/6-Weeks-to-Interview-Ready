/*
 *   Title: Max path sum
 *
 * Problem:
 *    Given a non-empty binary tree, find the maximum path sum.
 *
 *   For this problem, a path is defined as any sequence of nodes from some
 *   starting node to any node in the tree along the parent-child connections.
 *   The path must contain at least one node and does not need to go through the
 *   root.
 *
 *   Execution: javac MaxPathSum.java && java MaxPathSum
 */
import java.util.*;


class MaxPathSum {

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
    static int max_sum;
    public static int maxPathSum(TreeNode root) {
        max_sum = Integer.MIN_VALUE;
        max_gain(root);
        return max_sum;
    }

    public static int max_gain(TreeNode root){
        if(root == null){
            return 0;
        }

        int leftGain = Math.max(max_gain(root.left), 0);
        int rightGain = Math.max(max_gain(root.right), 0);
        int sum = root.val + leftGain + rightGain;
        max_sum = Math.max(max_sum, sum);
        return root.val + Math.max(leftGain, rightGain);
    }

    public static void main(String args[])
    {
        MaxPathSum mbt = new MaxPathSum();

        TreeNode tree1 = new TreeNode(1);
        tree1.left = new TreeNode(3);
        tree1.right = new TreeNode(2);
        tree1.left.left = new TreeNode(5);

        assert mbt.maxPathSum(tree1) == 1 + 2 + 3 + 5;

        System.out.println("Passed all test cases");
    }
}
