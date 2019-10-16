/*
 *   Title: Maximum depth of binary tree.
 *
 *   Problem:
 *      Given a binary tree, find its maximum depth.
 *
 *      The maximum depth is the number of nodes along the longest path from the root
 *      node down to the farthest leaf node.
 *
 *      Note: A leaf is a node with no children.
 *
 *   Execution: javac MaxDepthBinaryTree.java && java MaxDepthBinaryTree
 */
import java.util.*;

public class MaxDepthBinaryTree {

    public static class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode(int x) { val = x; }
    }

    public static int maxDepthBinaryTree(TreeNode root) {
        if(root == null) {
            return 0;
        }
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);
        int count = 0;
        while(!queue.isEmpty()) {
            int size = queue.size();
            while(size-- > 0) {
                TreeNode node = queue.poll();
                if(node.left != null) {
                    queue.offer(node.left);
                }
                if(node.right != null) {
                    queue.offer(node.right);
                }
            }
            count++;
        }
        return count;
    }

    public static void main(String[] args) {
        /*
        Given binary tree [3,9,20,null,null,15,7],
                3
               / \
              9  20
                /  \
               15   7
        */
        MaxDepthBinaryTree mdbt = new MaxDepthBinaryTree();

        TreeNode tree = new TreeNode(3);
        tree.left = new TreeNode(9);
        tree.right = new TreeNode(20);
        tree.right.right = new TreeNode(7);
        tree.right.left = new TreeNode(15);

        assert mdbt.maxDepthBinaryTree(tree) == 3;

        System.out.println("Passed all test cases");
    }
    
}
