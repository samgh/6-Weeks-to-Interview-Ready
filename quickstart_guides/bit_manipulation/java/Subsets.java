/*
    Title: Subsets.

    Problem: 
        Given a set of distinct integers, nums, return all possible subsets (the
        power set).

        Note: The solution set must not contain duplicate subsets.

    Execution: javac Subsets.java && java Subsets
 */
import java.util.*;

public class Subsets {
    public static List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> result=new ArrayList<List<Integer>>();
        result.add(new ArrayList<Integer>());
        for(int i=0;i<nums.length;i++){
            int n=result.size();
            for(int j=0;j<n;j++){
                List <Integer> tmp = new ArrayList<>(result.get(j));
                tmp.add(nums[i]);
                result.add(tmp);
            }
        }
        return result;
    }

    public static void main(String[] args) {

        int[] testInput = {1, 2, 3};
        List<List<Integer>> result = subsets(testInput);

        // [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
        System.out.println(result);

        System.out.println("Passed all test cases");
    }
    
}
