/*
 *   Title: Diameter of Binary Tree
 *   Leetcode Link: https://leetcode.com/problems/diameter-of-binary-tree/
 *
 *   Problem: Given a binary tree, you need to compute the length of the
 *   diameter of the tree. The diameter of a binary tree is the length of the
 *   longest path between any two nodes in a tree. This path may or may not pass
 *   through the root.
 *
 *   Input:
 *      TreeNode root   => the root of the tree
 *   Output:
 *      int             => the diameter of the tree whose root is root
 *
 *   Execution: javac DiameterOfBinaryTree.java && java -ea DiameterOfBinaryTree
 */

import java.util.*;

public class DiameterOfBinaryTree {

    // Our simple class for the tree nodes
    public static class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode(int x) { val = x; }
    }

    /*
     * The diameter of the tree is either:
     *   a) The diameter of the left subtree
     *   b) The diameter of the right subtree
     *   c) height(left subtree) + height(right subtree) + 1
     * We will solve this by recursively computing the diameters of the left
     * and right subtree while simultaneously computing the heights
     *
     * Time Complexity: O(n)
     * Space Complexity: O(n)
     */
    public static int diameterOfBinaryTree(TreeNode root) {
        // We need pointers to store the heights, since we can't return multiple
        // values. We can simulate this with an array or simple wrapper class
        int[] height = new int[1];

        // Our approach counts the number of nodes in the path, but Leetcode
        // requires the number of edges, which is # nodes - 1
        return diameterOfBinaryTree(root, height)-1;
    }

    private static int diameterOfBinaryTree(TreeNode root, int[] height) {
        // Base Case. If root is null, diameter of empty tree is 0
        if (root == null) return 0;

        // We need pointers to store the heights, since we can't return multiple
        // values. We can simulate this with an array or simple wrapper class
        int[] leftHeight = new int[1];
        int[] rightHeight = new int[1];

        // Find the diameter and height of the two subtrees
        int leftDiam = diameterOfBinaryTree(root.left, leftHeight);
        int rightDiam = diameterOfBinaryTree(root.right, rightHeight);

        // Find the maximum of the diameters and the combined heights
        int diam = Math.max(leftDiam, rightDiam);
        diam = Math.max(diam, leftHeight[0]+rightHeight[0]+1);

        // Update the height of the current subtree so it can be used after we
        // return
        height[0] = Math.max(leftHeight[0], rightHeight[0])+1;
        return diam;
    }

    // Test cases
    public static void main(String[] args) {
        TreeNode input1 = new TreeNode(1);
        input1.left = new TreeNode(2);
        input1.right = new TreeNode(3);
        input1.left.left = new TreeNode(4);
        input1.left.right= new TreeNode(5);

        // Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3]
        assert diameterOfBinaryTree(input1) == 3;

        // ADD YOUR OWN TESTS HERE

        System.out.println("Passed all test cases");
    }

}
