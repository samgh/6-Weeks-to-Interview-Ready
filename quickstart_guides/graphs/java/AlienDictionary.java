/*
 *   Title: Alien Dictionary
 *
 *   Problem:
 *       Given a sorted dictionary (array of words) of an alien language, find
 *       order of characters in the language.
 *
 *   Execution: javac AlienDictionary.java && java AlienDictionary
 */
import java.io.*;
import java.util.*;

class Graph
{

    // An array representing the graph as an adjacency list.
    private final LinkedList<Integer>[] adjacencyList;

    Graph(int nVertices)
    {
        adjacencyList = new LinkedList[nVertices];
        for (int vertexIndex = 0; vertexIndex < nVertices; vertexIndex++)
        {
            adjacencyList[vertexIndex] = new LinkedList<>();
        }
    }

    // function to add an edge to graph
    void addEdge(int startVertex, int endVertex)
    {
        adjacencyList[startVertex].add(endVertex);
    }

    private int getNoOfVertices()
    {
        return adjacencyList.length;
    }

    // A recursive function used by topologicalSort.
    private void topologicalSortUtil(int currentVertex, boolean[] visited,
                                     Stack<Integer> stack)
    {
        // Mark the current node as visited.
        visited[currentVertex] = true;

        // Recur for all the vertices adjacent to this vertex.
        for (int adjacentVertex : adjacencyList[currentVertex])
        {
            if (!visited[adjacentVertex])
            {
                topologicalSortUtil(adjacentVertex, visited, stack);
            }
        }

        // Push current vertex to stack which stores result
        stack.push(currentVertex);
    }

    // prints a Topological Sort of the complete graph
    ArrayList<Character> topologicalSort()
    {
        Stack<Integer> stack = new Stack<>();

        // Mark all the vertices as not visited.
        boolean[] visited = new boolean[getNoOfVertices()];
        for (int i = 0; i < getNoOfVertices(); i++)
        {
            visited[i] = false;
        }

        // Call the recursive helper function to store Topological
        // Sort starting from all vertices one by one.
        for (int i = 0; i < getNoOfVertices(); i++)
        {
            if (!visited[i])
            {
                topologicalSortUtil(i, visited, stack);
            }
        }

        ArrayList<Character> result = new ArrayList<Character>();
        while (!stack.isEmpty()) {
            result.add((char)('a' + stack.pop()));
        }
      return result;
    }
}

public class AlienDictionary
{
    // This function finds and prints order of character from a sorted array of
    // words. alpha is number of possible alphabets starting from 'a'. For
    // simplicity, this function is written in a way that only first 'alpha'
    // characters can be there in words array. For example if alpha is 7, then
    // words[] should contain words having only 'a', 'b','c' 'd', 'e', 'f', 'g'.
    private static ArrayList<Character> printOrder(String[] words, int alpha)
    {
        Graph graph = new Graph(alpha);

        for (int i = 0; i < words.length - 1; i++)
        {
            // Take the current two words and find the first mismatching
            // character.
            String word1 = words[i];
            String word2 = words[i+1];
            for (int j = 0; j < Math.min(word1.length(), word2.length()); j++)
            {
                // If we find a mismatching character, then add an edge
                // from character of word1 to that of word2.
                if (word1.charAt(j) != word2.charAt(j))
                {
                    graph.addEdge(word1.charAt(j) - 'a', word2.charAt(j)- 'a');
                    break;
                }
            }
        }

        ArrayList<Character> result = graph.topologicalSort();
        return result;
    }

    public static void main(String[] args)
    {
        String[] words = {"caa", "aaa", "aab"};
        ArrayList<Character> result = printOrder(words, 3);
        ArrayList<Character> exp_result = new ArrayList<Character>();
        exp_result.add('c');
        exp_result.add('a');
        exp_result.add('b');

        assert result.equals(exp_result);
    }
}
