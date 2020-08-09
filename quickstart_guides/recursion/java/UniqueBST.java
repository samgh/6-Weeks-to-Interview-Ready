/*
 * Title: Unique BST
 *
 * Problem:
 *  Construct all possible BSTs for keys 1 to N.
 *
 * Execution: javac UniqueBST.java && java UniqueBST
 *
 */

import java.util.ArrayList;

class Node
{
    int key;
    Node left, right;
    Node(int data)
    {
        this.key=data;
        left=right=null;
    }
}

public class UniqueBST {

    static ArrayList<Node> constructTrees(int start, int end) {
        ArrayList<Node> list=new ArrayList<>();

        // If start > end then subtree will be empty so returning NULL in list.
        if (start > end)
        {
            list.add(null);
            return list;
        }

        // Iterate through all values for constructing left and right.
        for (int i = start; i <= end; i++) {
            // Constructing left subtree.
            ArrayList<Node> leftSubtree  = constructTrees(start, i - 1);

            // Constructing right subtree.
            ArrayList<Node> rightSubtree = constructTrees(i + 1, end);

            // Loop through all left and right subtrees and connecting
            // them to ith root  below  */
            for (int j = 0; j < leftSubtree.size(); j++) {
                Node left = leftSubtree.get(j);
                for (int k = 0; k < rightSubtree.size(); k++) {
                    Node right = rightSubtree.get(k);
                    Node node = new Node(i);        // making value i as root
                    node.left = left;              // connect left subtree
                    node.right = right;            // connect right subtree
                    list.add(node);                // add this tree to list
                }
            }
        }
        return list;
    }

    // A utility function to do pre-order traversal of BST
    static void preorder(Node root) {
        if (root != null)
        {
            System.out.print(root.key+" ") ;
            preorder(root.left);
            preorder(root.right);
        }
    }

    public static void main(String args[]) {
        ArrayList<Node> totalTreesFrom1toN = constructTrees(1, 3);

        System.out.println("Preorder traversals of all constructed BSTs are ");
        for (int i = 0; i < totalTreesFrom1toN.size(); i++) {
            preorder(totalTreesFrom1toN.get(i));
            System.out.println();
        }
    }
}
