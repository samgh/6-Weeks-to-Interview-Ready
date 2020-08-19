/*
 *   Title: Lowest common ancestor
 *
 * Problem:
 *   Given a binary tree (not a binary search tree) and two values say n1 and n2,
 *   write a program to find the least common ancestor.
 *
 *   Execution: javac LowestCommonAncestor.java && java LowestCommonAncestor
 */
import java.util.ArrayList;
import java.util.List;

// A Binary Tree node
class Node {
    int data;
    Node left, right;

    Node(int value) {
        data = value;
        left = right = null;
    }
}

public class LowestCommonAncestor
{

    Node root;
    private List<Integer> path1 = new ArrayList<>();
    private List<Integer> path2 = new ArrayList<>();

    // Finds the path from root node to given root of the tree.
    int findLCA(int n1, int n2) {
        path1.clear();
        path2.clear();
        return findLCAInternal(root, n1, n2);
    }

    private int findLCAInternal(Node root, int n1, int n2) {

        if (!findPath(root, n1, path1) || !findPath(root, n2, path2)) {
            System.out.println((path1.size() > 0) ? "n1 is present" : "n1 is missing");
            System.out.println((path2.size() > 0) ? "n2 is present" : "n2 is missing");
            return -1;
        }

        int i;
        for (i = 0; i < path1.size() && i < path2.size(); i++) {

        // System.out.println(path1.get(i) + " " + path2.get(i));
            if (!path1.get(i).equals(path2.get(i)))
                break;
        }

        return path1.get(i-1);
    }

    // Finds the path from root node to given root of the tree, Stores the
    // path in a vector path[], returns true if path exists otherwise false
    private boolean findPath(Node root, int n, List<Integer> path)
    {
        // base case
        if (root == null) {
            return false;
        }

        // Store this node . The node will be removed if
        // not in path from root to n.
        path.add(root.data);

        if (root.data == n) {
            return true;
        }

        if (root.left != null && findPath(root.left, n, path)) {
            return true;
        }

        if (root.right != null && findPath(root.right, n, path)) {
            return true;
        }

        // If not present in subtree rooted with root, remove root from
        // path[] and return false
        path.remove(path.size()-1);

        return false;
    }
    public static void main(String[] args)
    {
        LowestCommonAncestor tree = new LowestCommonAncestor();
        tree.root = new Node(1);
        tree.root.left = new Node(2);
        tree.root.right = new Node(3);
        tree.root.left.left = new Node(4);
        tree.root.left.right = new Node(5);
        tree.root.right.left = new Node(6);
        tree.root.right.right = new Node(7);

        assert tree.findLCA(4, 5) == 2;
        assert tree.findLCA(4, 6) == 1;
        assert tree.findLCA(3, 4) == 1;
        assert tree.findLCA(2, 4) == 2;
        System.out.println("Passed all test cases");
    }
}
