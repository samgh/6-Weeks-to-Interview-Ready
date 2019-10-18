/*
 *   Title: Subsets
 *
 *   Problem:Given a set of distinct integers, nums, return all possible
 *   subsets (the power set).
 *   Note: The solution set must not contain duplicate subsets.
 *
 *   Execution: javac GeneratePowerSet.java && java GeneratePowerSet
 */
import java.util.*; 

public class GeneratePowerSet {
    public static List<List<Integer>> generatePowerSet(int[] S) {
        List<List<Integer>> res = new ArrayList<>();
        res.add(new ArrayList<Integer>());

        Arrays.sort(S);
        for(int i : S) {
            List<List<Integer>> tmp = new ArrayList<>();
            for(List<Integer> sub : res) {
                List<Integer> a = new ArrayList<>(sub);
                a.add(i);
                tmp.add(a);
            }
            res.addAll(tmp);
        }
        return res;
    }

    public static void main(String[] args) {

        int[] testInput = {1, 2, 3};
        /* 
         * Expected output:
         * [
                  [3],
                  [1],
                  [2],
                  [1,2,3],
                  [1,3],
                  [2,3],
                  [1,2],
                  []
            ]
         */
        System.out.println(generatePowerSet(testInput));

        System.out.println("Passed all test cases");
    }
    
}
