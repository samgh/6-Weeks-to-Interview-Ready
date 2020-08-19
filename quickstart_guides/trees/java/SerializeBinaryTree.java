/*
 *   Title: Serialize binary tree
 *
 * Problem:
 *   Serialization is the process of converting a data structure or object into a
 *   sequence of bits so that it can be stored in a file or memory buffer, or
 *   transmitted across a network connection link to be reconstructed later in
 *   the same or another computer environment.
 *
 *   Design an algorithm to serialize and deserialize a binary tree. There is no
 *   restriction on how your serialization/deserialization algorithm should work.
 *   You just need to ensure that a binary tree can be serialized to a string and
 *   this string can be deserialized to the original tree structure.
 *
 *   Execution: javac SerializeBinaryTree.java && java SerializeBinaryTree
 */
 import java.util.*;


public class SerializeBinaryTree {

     // Definition for a binary tree node.
     public static class TreeNode {
         int val;
         TreeNode left;
         TreeNode right;
         TreeNode(int x) { val = x; }
     }

    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        StringBuilder sb = new StringBuilder();
        preorder(root, sb);
        return sb.toString();
    }

    private void preorder(TreeNode root, StringBuilder sb) {
        if(root != null) {
            sb.append(root.val + ",");
            preorder(root.left, sb);
            preorder(root.right, sb);
        }
        else {
            sb.append("null,");
        }
    }


    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        String[] datas = data.split(",");
        return buildTree(datas);
    }

	/** Inspired by the iterative solution of
	question 1008. Construct Binary Search Tree from Preorder Traversal
	**/
    private TreeNode buildTree(String[] data) {
        if(data[0].equals("null")) return null;

        Stack<TreeNode> stack = new Stack();
        TreeNode head = new TreeNode(Integer.parseInt(data[0]));
        stack.push(head);
        for(int i = 1; i < data.length; i++) {
            TreeNode node = stack.peek();
            TreeNode next;
            if(data[i].equals("null")) {
                next = null;
            }
            else {
                next = new TreeNode(Integer.parseInt(data[i]));
            }

            boolean right = false;
            while(!stack.isEmpty() && node == null) {
                right = true;
                node = stack.pop();
            }

            if(right) {
                node.right = next;
            }
            else {
                node.left = next;
            }
            stack.push(next);
        }
        return head;
    }

    public static void main(String[] args)
    {
        SerializeBinaryTree codec = new SerializeBinaryTree();
        TreeNode tree = new TreeNode(1);
        tree.left = new TreeNode(2);
        tree.right = new TreeNode(3);
        tree.left.left = new TreeNode(4);
        tree.left.right = new TreeNode(5);

        codec.serialize(tree);

        System.out.println("All tests passed.");
    }
}