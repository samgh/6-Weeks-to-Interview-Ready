/*
 *   Title: Sort linked list
 *
 *   Problem:
 *      Sort a linked list in O(n log n) time using constant space complexity.
 *
 *   Execution: javac SortLinkedList.java && java SortLinkedList
 */
class Node
{
	int data;
	Node next;

	Node(int data, Node next) {
		this.data = data;
		this.next = next;
	}
}

class SortLinkedList
{
	// Helper function to print given linked list.
	public static void printList(Node head)
	{
		Node ptr = head;
		while (ptr != null)
		{
			System.out.print(ptr.data + " -> ");
			ptr = ptr.next;
		}

		System.out.println("null");
	}

	// Takes two lists sorted in increasing order, and merge their nodes
	// together to make one big sorted list which is returned.
	public static Node SortedMerge(Node a, Node b)
	{
		// Base cases
		if (a == null)
			return b;

		else if (b == null)
			return a;

		Node result;

		// Pick either a or b, and recur
		if (a.data <= b.data)
		{
			result = a;
			result.next = SortedMerge(a.next, b);
		}
		else
		{
			result = b;
			result.next = SortedMerge(a, b.next);
		}

		return result;
	}

	/*
	Split the nodes of the given list into front and back halves,
	If the length is odd, the extra node should go in the front list.
	It uses the fast/slow pointer strategy
	*/
	public static Node[] FrontBackSplit(Node source)
	{
		// if length is less than 2, handle separately
		if (source == null || source.next == null) {
			return new Node[]{ source, null } ;
		}

		Node slow = source;
		Node fast = source.next;

		// Advance 'fast' two nodes, and advance 'slow' one node
		while (fast != null)
		{
			fast = fast.next;
			if (fast != null)
			{
				slow = slow.next;
				fast = fast.next;
			}
		}

		// 'slow' is before the midpoint in the list, so split it in two
		// at that point.
		Node[] arr = new Node[]{ source, slow.next };
		slow.next = null;

		return arr;
	}

	// Sort given linked list using Merge sort algorithm
	public static Node MergeSort(Node head)
	{
		// Base case -- length 0 or 1
		if (head == null || head.next == null) {
			return head;
		}

		// Split head into 'a' and 'b' sublists
		Node[] arr = FrontBackSplit(head);
		Node front = arr[0];
		Node back = arr[1];

		// Recursively sort the sublists
		front = MergeSort(front);
		back = MergeSort(back);

		// answer = merge the two sorted lists together
		return SortedMerge(front, back);
	}

	// Sort given linked list using Merge sort algorithm
	public static void main(String[] args)
	{
		// input keys
		int[] keys = { 8, 6, 4, 9, 3, 1 };

		Node head = null;
		for (int key: keys) {
			head = new Node(key, head);
		}

		// sort the list
		head = MergeSort(head);

		// print the sorted list
		printList(head);
	}
}