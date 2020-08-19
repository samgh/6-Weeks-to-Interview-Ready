/*
 *   Title: Post-order traversal of binary tree
 *
 * Problem:
 *   Given a binary tree, return the postorder traversal of its nodes' values.
 *
 *   Execution: javac PostorderTraversal.java && java PostorderTraversal
 */
import java.util.*;


class PostorderTraversal {

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
    class Pair {
        TreeNode node;
        boolean leftChecked;
        boolean rightChecked;
        Pair(TreeNode n) {
            this.node = n;
        }
    }

    public List<Integer> postorderTraversal(TreeNode root) {
        List<Integer> ans = new ArrayList<>();
        if (root == null) return ans;

        Stack<Pair> stack = new Stack<>();
        stack.push(new Pair(root));

        while (!stack.isEmpty()) {
            Pair p = stack.peek();
            if (!p.leftChecked && p.node.left != null) {
                p.leftChecked = true;
                stack.push(new Pair(p.node.left));
                continue;
            } else if (!p.rightChecked && p.node.right != null) {
                p.rightChecked = true;
                stack.push(new Pair(p.node.right));
                continue;
            } else {
                stack.pop();
                ans.add(p.node.val);
            }
        }

        return ans;
    }
    public static void main(String args[])
    {
        PostorderTraversal pt = new PostorderTraversal();
        TreeNode tree = new TreeNode(1);
        tree.right = new TreeNode(2);
        tree.right.left = new TreeNode(3);

        System.out.println(pt.postorderTraversal(tree));

        System.out.println("Passed all test cases");
    }
}