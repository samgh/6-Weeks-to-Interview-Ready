/*
 *   Title: Level-order traversal of binary tree
 *
 * Problem:
 *   Given a binary tree, return the level-order traversal of its nodes' values.
 *
 *   Execution: javac LevelorderTraversal.java && java LevelorderTraversal
 */
import java.util.*;


// A Binary Tree node
class Node {
    int data;
    Node left, right;

    Node(int value) {
        data = value;
        left = right = null;
    }
}


class LevelorderTraversal {
    Node root;

    public static List<List<Integer>> levelOrderTraversal(Node root) {
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        if(root == null) return res;

        Queue<Node> q = new LinkedList<Node>();
        q.add(root);

        while(q.isEmpty() == false) {
            List<Integer> currli = new ArrayList<Integer>();
            int qsize = q.size();
            for(int i = 0; i < qsize; i++) {
                Node curr = q.poll();
                currli.add(curr.data);
                if(curr.left != null) q.add(curr.left);
                if(curr.right != null) q.add(curr.right);
            }
            res.add(currli);
        }

        return res;
    }

    public static void main(String args[])
    {
        LevelorderTraversal tree = new LevelorderTraversal();
        tree.root = new Node(1);
        tree.root.left = new Node(2);
        tree.root.right = new Node(3);
        tree.root.left.left = new Node(4);
        tree.root.left.right = new Node(5);
        tree.root.right.left = new Node(6);
        tree.root.right.right = new Node(7);

        System.out.println(levelOrderTraversal(tree.root));

        System.out.println("Passed all test cases");
    }
}
