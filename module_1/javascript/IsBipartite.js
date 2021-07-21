/*
 *   Title: Is Graph Bipartite
 *   Leetcode Link: https://leetcode.com/problems/is-graph-bipartite/
 *
 *   Problem: Given an undirected graph, return true if and only if it is
 *   bipartite.
 *
 *   Recall that a graph is bipartite if we can split it's set of nodes into two
 *   independent subsets U and V such that every edge in the graph has one node
 *   in U and another node in B.
 *
 *   The graph is given in the following form:
 *      graph[i] is a list of indexes j for which the edge between nodes i and j
 *      exists.  Each node is an integer between 0 and graph.length - 1.  There
 *      are no self edges or parallel edges: graph[i] doesnot contain i, and it
 *      doesn't contain any element twice.
 *
 *   Input:
 *      number[][] graph      => Edge list representing graph
 *   Output:
 *      boolean               => True if and only if graph is bipartite
 *
 *   Execution: node IsBipartite.js
 */

/**
  * We select a random starting node and then  greedily assign each node to
  * either U or V. We do this using DFS. As we do this, we look for
  * contradictions. If we can successfully assign all the nodes, then the
  * graph is bipartite.
  *
  * Time Complexity: O(V+E)
  * Space Complexity: O(V)
  *
  * @param {number[][]} graph
  * @return {boolean}
  */

var isBipartite = function(graph) {
    // Track the coloring of each node that we visit. For simplicity, nodes
    // in U will be set to 1 and nodes in V will be -1
    var colors = [];
    var arraySize = graph.length;
    while(arraySize--) colors.push(0);

    // Our nodes aren't all necessarily connected, so we need to be sure to
    // iterate over every connected component of the graph
    for (var i = 0; i < graph.length; i++) {
        if (!isBipartiteInner(graph, i, colors)) return false;
    }

    return true;
}

/**
 * Inner recursive function
 *
 * @param {number[][]} graph
 * @param {number} curr
 * @param {number[]} colors
 */
var isBipartiteInner = function(graph, curr, colors) {
    // If the node hasn't been visited yet we need to initialize it. The
    // value doesn't matter
    if (colors[curr] === 0) colors[curr] = 1;

    // Use DFS to visit all nodes. Each time we visit a node, we'll set
    // it to be the opposite color. As we do this we look for
    // contradictions
    for (var i = 0; i < graph[curr].length; i++) {
        var next = graph[curr][i];

        // If the next node hasn't been visited, set it to the opposite of
        // the current color. Then continue DFS. Otherwise, if it has been
        // visited make sure it's the right color
        if (colors[next] === 0) {
            colors[next] = -colors[curr];
            if (!isBipartiteInner(graph, next, colors)) return false;
        } else if (colors[next] !== -colors[curr]) {
            return false;
        }
    }

    return true;
}

var tester = function() {
    console.assert(isBipartite([[1, 3], [0, 2], [1, 3], [0, 2]]) === true);
    console.assert(isBipartite([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]) === false);

    // ADD YOUR OWN TESTS HERE
}

tester();
