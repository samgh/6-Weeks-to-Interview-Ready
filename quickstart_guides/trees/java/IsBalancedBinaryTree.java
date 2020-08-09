/*
 *   Title: Is Balanced Binary Tree
 *
 * Problem:
 *    Given a binary tree, determine if it is height-balanced.
 *
 *   For this problem, a height-balanced binary tree is defined as:
 *
 *   a binary tree in which the left and right subtrees of every node differ in
 *   height by no more than 1.
 *
 *   Execution: javac IsBalancedBinaryTree.java && java IsBalancedBinaryTree
 */


class Node {
    int data;
    Node left, right;
    Node(int d)
    {
        data = d;
        left = right = null;
    }
}


class IsBalancedBinaryTree {
    Node root;

    /* Returns true if binary tree with root as root is height-balanced */
    boolean isBalancedBinaryTree(Node node)
    {
        int lh; /* for height of left subtree */

        int rh; /* for height of right subtree */

        /* If tree is empty then return true */
        if (node == null)
            return true;

        /* Get the height of left and right sub trees */
        lh = height(node.left);
        rh = height(node.right);

        if (Math.abs(lh - rh) <= 1
            && isBalancedBinaryTree(node.left)
            && isBalancedBinaryTree(node.right))
            return true;

        /* If we reach here then tree is not height-balanced */
        return false;
    }

    /* UTILITY FUNCTIONS TO TEST isBalanced() FUNCTION */
    /*  The function Compute the "height" of a tree. Height is the
        number of nodes along the longest path from the root node
        down to the farthest leaf node.*/
    int height(Node node)
    {
        /* base case tree is empty */
        if (node == null)
            return 0;

        /* If tree is not empty then height = 1 + max of left
         height and right heights */
        return 1 + Math.max(height(node.left), height(node.right));
    }

    public static void main(String args[])
    {
        IsBalancedBinaryTree tree = new IsBalancedBinaryTree();
        tree.root = new Node(1);
        tree.root.left = new Node(2);
        tree.root.right = new Node(3);
        tree.root.left.left = new Node(4);
        tree.root.left.right = new Node(5);
        tree.root.left.left.left = new Node(8);

        assert tree.isBalancedBinaryTree(tree.root) == false;
        System.out.println("Passed all test cases");
    }
}
