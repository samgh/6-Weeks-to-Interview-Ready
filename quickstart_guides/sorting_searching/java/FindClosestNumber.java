/*
 *   Title: Find closest number
 *
 *   Problem:
 *      Given an array of sorted integers. We need to find the closest value to
 *      the given number. Array may contain duplicate values and negative
 *      numbers.
 *
 *   Execution: javac FindClosestNumber.java && java FindClosestNumber
 */

import java.util.*; 
import java.lang.*; 
import java.io.*; 
  
class FindClosestNumber { 
      
    // Returns element closest to target in arr[] 
    public static int findClosestNumber(int arr[], int target) 
    { 
        int n = arr.length; 
  
        // Corner cases 
        if (target <= arr[0]) 
            return arr[0]; 
        if (target >= arr[n - 1]) 
            return arr[n - 1]; 
  
        // Doing binary search  
        int i = 0, j = n, mid = 0; 
        while (i < j) { 
            mid = (i + j) / 2; 
  
            if (arr[mid] == target) 
                return arr[mid]; 
  
            /* If target is less than array element, 
               then search in left */
            if (target < arr[mid]) { 
         
                // If target is greater than previous 
                // to mid, return closest of two 
                if (mid > 0 && target > arr[mid - 1])  
                    return getClosest(arr[mid - 1],  
                                  arr[mid], target); 
                  
                /* Repeat for left half */
                j = mid;               
            } 
  
            // If target is greater than mid 
            else { 
                if (mid < n-1 && target < arr[mid + 1])  
                    return getClosest(arr[mid],  
                          arr[mid + 1], target);                 
                i = mid + 1; // update i 
            } 
        } 
  
        // Only single element left after search 
        return arr[mid]; 
    } 
  
    // Method to compare which one is the more close. We find the closest by
    // taking the difference between the target and both values. It assumes
    // that val2 is greater than val1 and target lies between these two.
    public static int getClosest(int val1, int val2,  
                                         int target) 
    { 
        if (target - val1 >= val2 - target)  
            return val2;         
        else 
            return val1;         
    } 
  
    public static void main(String[] args)
    { 
        int arr[] = { 1, 2, 4, 5, 6, 6, 8, 9 }; 
        assert findClosestNumber(arr, 11) == 9;
        assert findClosestNumber(arr, 1) == 0;
        System.out.println("Passed all test cases");
    } 
} 
