/*
 * Title: Depth-first search
 *
 * Problem:
 *    Depth First Traversal (or Search) for a graph is similar to Depth First
 *    Traversal of a tree. The only catch here is, unlike trees, graphs may
 *    contain cycles, a node may be visited twice. To avoid processing a node more
 *    than once, use a boolean visited array.
 *
 *   Execution: javac DFS.java && java DFS
 *
 */
import java.io.*;
import java.util.*;

// This class represents a directed graph using adjacency list
// representation
class DFS
{
    private int V;   // No. of vertices

    // Array  of lists for Adjacency List Representation
    private LinkedList<Integer> adj[];
    public ArrayList<Integer> result = new ArrayList<Integer>();

    // Constructor
    DFS(int v)
    {
        V = v;
        adj = new LinkedList[v];
        for (int i=0; i<v; ++i)
            adj[i] = new LinkedList();
    }

    //Function to add an edge into the graph
    void addEdge(int v, int w)
    {
        adj[v].add(w);  // Add w to v's list.
    }

    // A function used by DFS
    void DFSUtil(int v,boolean visited[])
    {
        // Mark the current node as visited and print it
        visited[v] = true;
        result.add(v);

        // Recur for all the vertices adjacent to this vertex
        Iterator<Integer> i = adj[v].listIterator();
        while (i.hasNext())
        {
            int n = i.next();
            if (!visited[n])
                DFSUtil(n, visited);
        }
    }

    // The function to do DFS traversal. It uses recursive DFSUtil()
    ArrayList<Integer> dfs(int v)
    {
        // Mark all the vertices as not visited(set as
        // false by default in java)
        boolean visited[] = new boolean[V];

        // Call the recursive helper function to print DFS traversal
        DFSUtil(v, visited);
        return result;
    }

    public static void main(String args[])
    {
        DFS g = new DFS(4);

        g.addEdge(0, 1);
        g.addEdge(0, 2);
        g.addEdge(1, 2);
        g.addEdge(2, 0);
        g.addEdge(2, 3);
        g.addEdge(3, 3);

        ArrayList<Integer> result = g.dfs(2);

        ArrayList<Integer> exp_output = new ArrayList<Integer>();
        exp_output.add(2);
        exp_output.add(0);
        exp_output.add(1);
        exp_output.add(3);

        assert result.equals(exp_output) == true;
    }
}
