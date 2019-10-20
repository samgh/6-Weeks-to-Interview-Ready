/*
 *   Title: Find median sorted arrays.
 *
 *   Problem:
 *    There are two sorted arrays nums1 and nums2 of size m and n
 *    respectively.
 *
 *    Find the median of the two sorted arrays. The overall run time complexity
 *    should be O(log (m+n)).
 *
 *    You may assume nums1 and nums2 cannot be both empty.
 *
 *   Execution: javac FindMedianSortedArrays.java && java FindMedianSortedArrays
 */


public class FindMedianSortedArrays {
    public static double findMedianSortedArrays(int[] A, int[] B) {
        int m = A.length;
        int n = B.length;
        if (m > n) { // to ensure m<=n
            int[] temp = A; A = B; B = temp;
            int tmp = m; m = n; n = tmp;
        }
        int iMin = 0, iMax = m, halfLen = (m + n + 1) / 2;
        while (iMin <= iMax) {
            int i = (iMin + iMax) / 2;
            int j = halfLen - i;
            if (i < iMax && B[j-1] > A[i]){
                iMin = i + 1; // i is too small
            }
            else if (i > iMin && A[i-1] > B[j]) {
                iMax = i - 1; // i is too big
            }
            else { // i is perfect
                int maxLeft = 0;
                if (i == 0) { 
                    maxLeft = B[j-1]; 
                }
                else if (j == 0) { 
                    maxLeft = A[i-1]; 
                }
                else { 
                    maxLeft = Math.max(A[i-1], B[j-1]); 
                }
                if ( (m + n) % 2 == 1 ) { 
                    return maxLeft; 
                }

                int minRight = 0;
                if (i == m) { 
                    minRight = B[j]; 
                }
                else if (j == n) { 
                    minRight = A[i]; 
                }
                else {
                    minRight = Math.min(B[j], A[i]); 
                }
                return (maxLeft + minRight) / 2.0;
            }
        }
        return 0.0;
    }

    public static void main(String[] args) {
        int[] nums_1 = {1, 3};
        int[] nums_2 = {2};
        assert findMedianSortedArrays(nums_1, nums_2) == 2.0;
        System.out.println("Explanation: The median is 2.0");

        int[] nums_3 = {1, 2};
        int[] nums_4 = {3, 4};
        assert findMedianSortedArrays(nums_3, nums_4) == 2.5;
        System.out.println("Explanation: The median is (2 + 3)/2 = 2.5");

        System.out.println("Passed all test cases");
    }
    
}
