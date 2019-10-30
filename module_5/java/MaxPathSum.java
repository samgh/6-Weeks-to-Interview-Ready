/*
 *   Title: Max path sum.
 *
 *   Problem:
 *   Given a non-empty binary tree, find the maximum path sum.

     For this problem, a path is defined as any sequence of nodes from some starting
     node to any node in the tree along the parent-child connections. The path must
     contain at least one node and does not need to go through the root.
 *
 *   Execution: javac MaxPathSum.java && java MaxPathSum
 */
import java.util.*;


public class MaxPathSum {

    public static class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode(int x) { val = x; }
    }

    public static int maxPathSum(TreeNode root) {
        int[] max = {Integer.MIN_VALUE};
        maxPathSumRecursive(root, max);
        return max[0];
        
    }
    
    private static int maxPathSumRecursive(TreeNode root, int[] max) {
        if (root == null) {
            return 0;
        }
        
        int left = Math.max(maxPathSumRecursive(root.left, max), 0);
        int right = Math.max(maxPathSumRecursive(root.right, max), 0);

        max[0] = Math.max(max[0], root.val + left + right);

        return root.val + Math.max(left, right);        
    }

    public static void main(String[] args) {

        TreeNode tree1 = new TreeNode(1);
        tree1.left = new TreeNode(2);
        tree1.right = new TreeNode(3);

        assert maxPathSum(tree1) == 6;

        TreeNode tree2 = new TreeNode(-10);
        tree2.left = new TreeNode(9);
        tree2.right = new TreeNode(20);
        tree2.right.left = new TreeNode(15);
        tree2.right.right = new TreeNode(7);

        assert maxPathSum(tree2) == 42;

        System.out.println("Passed all test cases");
    }
    
}
