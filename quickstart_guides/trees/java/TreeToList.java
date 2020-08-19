/*
 *   Title: Tree to list
 *
 * Problem:
 *   Given a tree, write a function to convert it into a circular doubly linked
 *   list from left to right by only modifying the existing pointers.
 *
 *   Execution: javac TreeToList.java && java TreeToList
 */
import java.util.*;


class TreeToList {

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

    public void flatten(TreeNode root) {

        if(root == null) return;

        TreeNode rightTmp = null;
        flatten(root.left);
        flatten(root.right);
        rightTmp = root.right;

        if(root.left != null){
            root.right = root.left;
            TreeNode endNode = getEndNode(root.right);
            endNode.right = rightTmp;
            root.left = null;
        }

    }

    TreeNode getEndNode(TreeNode node){
        if(node == null) return null;

        while(node.right != null){
            node = node.right;
        }
        return node;
    }

    public static void main(String args[])
    {
        TreeToList d = new TreeToList();
        TreeNode tree = new TreeNode(1);
        tree.right = new TreeNode(2);
        tree.right.left = new TreeNode(3);

        assert d.getEndNode(tree).val == 2;
        d.flatten(tree);
        assert d.getEndNode(tree).val == 3;

        System.out.println("Passed all test cases");
    }
}