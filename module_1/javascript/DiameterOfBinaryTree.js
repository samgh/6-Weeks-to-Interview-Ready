/*
 *   Title: Diameter of Binary Tree
 *   Leetcode Link: https://leetcode.com/problems/diameter-of-binary-tree/
 *
 *   Problem: Given a binary tree, you need to compute the length of the
 *   diameter of the tree. The diameter of a binary tree is the length of the
 *   longest path between any two nodes in a tree. This path may or may not pass
 *   through the root.
 *
 *   Input:
 *      TreeNode root   => the root of the tree
 *   Output:
 *      number          => the diameter of the tree whose root is root
 *
 *   Execution: node DiameterOfBinaryTree.js
 */

// Simple class for the tree nodes
class TreeNode {
    constructor(val, left, right) {
        this.val = (val===undefined ? 0 : val)
        this.left = (left===undefined ? null : left)
        this.right = (right===undefined ? null : right)
    }
}

/**
 * The diameter of the tree is either:
 *   a) The diameter of the left subtree
 *   b) The diameter of the right subtree
 *   c) height(left subtree) + height(right subtree) + 1
 * We will solve this by recursively computing the diameters of the left
 * and right subtree while simultaneously computing the heights
 *
 * Time Complexity: O(n)
 * Space Complexity: O(n)
 *
 * @param{TreeNode} root
 * @return {number}
 */

var diameterOfBinaryTree = function(root) {
    // Our approach counts the number of nodes in the path, but Leetcode
    // requires the number of edges, which is # nodes - 1
    return diameterOfBinaryTreeInner(root)[0]-1
}

/**
 * Inner function that computes height in addition to diameter.
 *
 * Returns [diameter, height]
 *
 * @param{TreeNode} root
 * @return{number[]}
 */
var diameterOfBinaryTreeInner = function(root) {
    // Base Case. If root is null, diameter of empty tree is 0 and height is 0
    if (root == null) return [0,0];

    // Find the diameter and height of the two subtrees
    var left = diameterOfBinaryTreeInner(root.left);
    var right = diameterOfBinaryTreeInner(root.right);

    // Find the maximum of the diameters and the combined heights
    var diam = Math.max(left[0], right[0]);
    diam = Math.max(diam, left[1]+right[1]+1);

    // Find the height of the current subtree
    var height = Math.max(left[1], right[1])+1;

    return [diam, height];
}

var tester = function() {
    const input1 = new TreeNode(1);
    input1.left = new TreeNode(2);
    input1.right = new TreeNode(3);
    input1.left.left = new TreeNode(4);
    input1.left.right= new TreeNode(5);

    console.assert(diameterOfBinaryTree(input1) === 3);

    // ADD YOUR OWN TESTS HERE
}

tester();
