/*
 *   Title: Merge Sort
 *
 *   Problem:
 *      Implement MergeSort on an array
 *
 *   Execution: javac MergeSort.java && java MergeSort
 */
class MergeSort {
    void merge(int arr[], int l, int m, int r) {
        int n1 = m - l + 1;
        int n2 = r - m;

        int left[] = new int [n1];
        int right[] = new int [n2];

        for (int i=0; i < n1; ++i)
            left[i] = arr[l + i];
        for (int j=0; j < n2; ++j)
            right[j] = arr[m + 1+ j];

        int i = 0, j = 0;

        int k = l;
        while (i < n1 && j < n2) {
            if (left[i] <= right[j]) {
                arr[k] = left[i];
                i++;
            }
            else {
                arr[k] = right[j];
                j++;
            }
            k++;
        }

        /* Copy remaining elements of left[] if any */
        while (i < n1) {
            arr[k] = left[i];
            i++;
            k++;
        }

        /* Copy remaining elements of right[] if any */
        while (j < n2) {
            arr[k] = right[j];
            j++;
            k++;
        }
    }

    void sort(int arr[], int l, int r) {
        if (l < r) {
            // Find the middle point
            int m = (l+r)/2;

            // Sort first and second halves
            sort(arr, l, m);
            sort(arr , m+1, r);

            // Merge the sorted halves
            merge(arr, l, m, r);
        }
    }

    static void printArray(int arr[]) {
        int n = arr.length;
        for (int i=0; i<n; ++i)
            System.out.print(arr[i] + " ");
        System.out.println();
    }

    public static void main(String[] args) {

        int arr[] = {12, 11, 13, 5, 6, 7};
        System.out.println("Input");
        printArray(arr);

        MergeSort ob = new MergeSort();
        ob.sort(arr, 0, arr.length-1);

        System.out.println("\nSorted output");
        printArray(arr);
    }
}
