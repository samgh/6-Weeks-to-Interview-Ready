/*
 *   Title: Is bipartite
 *
 *   Problem:
 *     A Bipartite Graph is a graph whose vertices can be divided into two
 *     independent sets, U and V such that every edge (u, v) either connects a
 *     vertex from U to V or a vertex from V to U. In other words, for every edge
 *     (u, v), either u belongs to U and v to V, or u belongs to V and v to U.
 *
 *   We can also say that there is no edge that connects vertices of same set. *
 *
 *   Execution: javac IsBipartite.java && java IsBipartite
 */
import java.util.*;
import java.lang.*;
import java.io.*;

class IsBipartite
{
    // No. of Vertices.
    final static int vertices = 4;

    // This function returns true if graph G[V][V] is Bipartite, else false.
    boolean isBipartite(int G[][],int src)
    {
        // Create a color array to store colors assigned to all veritces. Vertex
        // number is used as index in this array. The value '-1' of colorArr[i]
        // is used to indicate that no color is assigned to vertex 'i'. The
        // value 1 is used to indicate first color is assigned and value 0
        // indicates second color is assigned.
        int color_arr[] = new int[vertices];
        for (int i=0; i<vertices; ++i)
            color_arr[i] = -1;

        // Assign first color to source.
        color_arr[src] = 1;

        // Create a queue (FIFO) of vertex numbers and enqueue source vertex for
        // BFS traversal.
        LinkedList<Integer>q = new LinkedList<Integer>();
        q.add(src);

        // Run while there are vertices in queue (Similar to BFS).
        while (q.size() != 0)
        {
            // Dequeue a vertex from queue
            int u = q.poll();

            // Return false if there is a self-loop
            if (G[u][u] == 1)
                return false;

            // Find all non-colored adjacent vertices
            for (int v=0; v<vertices; ++v)
            {
                // An edge from u to v exists and destination v is not colored.
                if (G[u][v]==1 && color_arr[v]==-1)
                {
                    // Assign alternate color to this adjacent v of u.
                    color_arr[v] = 1-color_arr[u];
                    q.add(v);
                }

                // An edge from u to v exists and destination v is colored with
                // same color as u.
                else if (G[u][v]==1 && color_arr[v]==color_arr[u])
                    return false;
            }
        }
        // If we reach here, then all adjacent vertices can be colored with
        // alternate color.
        return true;
    }

    public static void main (String[] args)
    {
        int G[][] = {{0, 1, 0, 1},
            {1, 0, 1, 0},
            {0, 1, 0, 1},
            {1, 0, 1, 0}
        };
        IsBipartite b = new IsBipartite();
        assert b.isBipartite(G, 0) == true;
    }
}
