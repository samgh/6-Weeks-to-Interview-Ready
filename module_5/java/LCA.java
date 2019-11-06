/*
 *   Title: Lowest common ancestor (LCA)
 *
 *   Problem:
 *   Given a binary tree, find the lowest common ancestor (LCA) of two given
 *   nodes in the tree.

     According to the definition of LCA on Wikipedia: “The lowest common ancestor is
     defined between two nodes p and q as the lowest node in T that has both p and q
     as descendants (where we allow a node to be a descendant of itself).”

     Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]
 *
 *   Execution: javac LCA.java && java LCA
 */
import java.util.*;


public class LCA {

    public static class Node {
        int data;
        Node left, right;
        public Node(int item) {
            data = item;
            left = right = null;
        }
    }

    public static class BinaryTree {
        static Node root;
        public static Node lca(int n1, int n2) {
            return lca(root, n1, n2);
        }

        public static Node lca(Node node, int n1, int n2) {
            if (node == null) {
                return null;
            }
            if (node.data == n1 || node.data == n2) {
                return node;
            }
            Node left_lca = lca(node.left, n1, n2);
            Node right_lca = lca(node.right, n1, n2);
            
            if (left_lca != null && right_lca != null) {
                return node;
            }

            return (left_lca != null) ? left_lca : right_lca;
        }
    }



    public static void main(String[] args) {
        BinaryTree tree = new BinaryTree();
        tree.root = new Node(1);
        tree.root.left = new Node(2);
        tree.root.right = new Node(3); 
        tree.root.left.left = new Node(4);
        tree.root.left.right = new Node(5);
        tree.root.right.left = new Node(6);
        tree.root.right.right = new Node(7);

        assert tree.lca(4, 5).data == 2;
        assert tree.lca(4, 6).data == 1;
        assert tree.lca(3, 4).data == 1;
        assert tree.lca(2, 4).data == 2;


        System.out.println("Passed all test cases");
    }
    
}
