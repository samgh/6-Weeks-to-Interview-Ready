/*
 *   Title: Serialize and Deserialize Binary Tree
 *
 *   Problem:
     Serialization is the process of converting a data structure or object
     into a sequence of bits so that it can be stored in a file or memory
     buffer, or transmitted across a network connection link to be
     reconstructed later in the same or another computer environment.

     Design an algorithm to serialize and deserialize a binary tree. There is no
     restriction on how your serialization/deserialization algorithm should
     work. You just need to ensure that a binary tree can be serialized to a
     string and this string can be deserialized to the original tree structure.
 *
 *   Execution: javac SerializeBinaryTree.java && java SerializeBinaryTree
 */
import java.util.*;


public class SerializeBinaryTree {

    public static class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode(int x) { val = x; }
    }

    public static class Codec {
        private static final char delimeter = ' ';
        private static final String nullStr = "N";

        // Encodes a tree to a single string.
        public static String serialize(TreeNode root) {
            if (root == null) return "";
            StringBuffer sb = new StringBuffer();
            serialize(root, sb);

            // remove trailing nulls
            int i = sb.length() - 2;
            while (sb.charAt(i) == 'N') i -= 2;
            return sb.delete(i + 1, sb.length()).toString().trim();
        }

        private static void serialize(TreeNode root, StringBuffer sb) {
            if (root == null) {
                sb.append(nullStr);
                sb.append(delimeter);
            } else {
                sb.append(root.val);
                sb.append(delimeter);
                serialize(root.left, sb);
                serialize(root.right, sb);
            }
        }

        // Decodes your encoded data to tree.
        public static TreeNode deserialize(String data) {
            if (data == null || data.trim().isEmpty()) return null;
            String[] nodes = data.split(" ");
            TreeNode root = new TreeNode(Integer.parseInt(nodes[0]));
            deserialize(nodes, root, new int[1]);
            return root;
        }

        private static void deserialize(String[] nodes, TreeNode root, int[] i) {
            if (i[0] >= nodes.length || nullStr.equals(nodes[i[0]])) return;
            if (i[0] + 1 < nodes.length) {
                root.left = nullStr.equals(nodes[i[0] + 1]) ? null : new TreeNode(Integer.parseInt(nodes[i[0] + 1]));
                i[0]++;
                deserialize(nodes, root.left, i);
            }

            if (i[0] + 1 < nodes.length) {
                root.right = nullStr.equals(nodes[i[0] + 1]) ? null : new TreeNode(Integer.parseInt(nodes[i[0] + 1]));
                i[0]++;
                deserialize(nodes, root.right, i);
            }
        }
    }

    public static void main(String[] args) {
        Codec codec = new Codec();

        TreeNode tree = new TreeNode(1);
        tree.left = new TreeNode(2);
        tree.right = new TreeNode(3);
        tree.right.left = new TreeNode(4);
        tree.right.right = new TreeNode(5);
        
        String serialized = codec.serialize(tree);
        System.out.println(serialized);
        
        TreeNode newTree = codec.deserialize(serialized);
        System.out.println(newTree.val);
        System.out.println(newTree.left.val);
        System.out.println(newTree.right.val);

        System.out.println("Passed all test cases");
    }
    
}
