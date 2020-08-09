/*
 *   Title: Breadth-first Search
 *
 *   Problem:
 *      Breadth First Traversal (or Search) for a graph is similar to Breadth
 *       First Traversal of a tree. The only catch here is, unlike trees, graphs
 *       may contain cycles, so we may come to the same node again. To avoid
 *       processing a node more than once, we use a boolean visited array. For
 *       simplicity, it is assumed that all vertices are reachable from the
 *       starting vertex.
 *
 *   Execution: javac BFS.java && java BFS
 */
import java.io.*;
import java.util.*;

// This class represents a directed graph using adjacency list
// representation
class BFS
{
    // No. of vertices.
    private int V;
    // Adjacency Lists.
    private LinkedList<Integer> adj[];

    BFS(int v)
    {
        V = v;
        adj = new LinkedList[v];
        for (int i=0; i<v; ++i)
            adj[i] = new LinkedList();
    }

    // Function to add an edge into the graph.
    void addEdge(int v,int w)
    {
        adj[v].add(w);
    }

    // prints BFS traversal from a given source s.
    ArrayList<Integer> bfs(int s)
    {
        // Mark all the vertices as not visited(By default set as false).
        boolean visited[] = new boolean[V];

        // Create a queue for BFS.
        LinkedList<Integer> queue = new LinkedList<Integer>();
        ArrayList<Integer> result = new ArrayList<Integer>();

        // Mark the current node as visited and enqueue it.
        visited[s]=true;
        queue.add(s);

        while (queue.size() != 0)
        {
            // Dequeue a vertex from queue and print it.
            s = queue.poll();
            result.add(s);

            // Get all adjacent vertices of the dequeued vertex s. If a adjacent
            // has not been visited, then mark it visited and enqueue it.
            Iterator<Integer> i = adj[s].listIterator();
            while (i.hasNext())
            {
                int n = i.next();
                if (!visited[n])
                {
                    visited[n] = true;
                    queue.add(n);
                }
            }
        }
        return result;
    }

    public static void main(String args[])
    {
        BFS g = new BFS(4);

        g.addEdge(0, 1);
        g.addEdge(0, 2);
        g.addEdge(1, 2);
        g.addEdge(2, 0);
        g.addEdge(2, 3);
        g.addEdge(3, 3);

        ArrayList<Integer> output = g.bfs(2);

        ArrayList<Integer> exp_output = new ArrayList<Integer>();
        exp_output.add(2);
        exp_output.add(0);
        exp_output.add(3);
        exp_output.add(1);

        assert output.equals(exp_output) == true;
    }
}