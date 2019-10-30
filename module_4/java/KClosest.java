/*
 *   Title: K-Closest
 *
 *   Problem:
 *   We have a list of points on the plane.  Find the K closest points to the
 *   origin (0, 0).

    (Here, the distance between two points on a plane is the Euclidean distance.)

    You may return the answer in any order.  The answer is guaranteed to be unique
    (except for the order that it is in.)
 *
 *   Execution: javac KClosest.java && java KClosest
 */
import java.util.*;


public class KClosest {
    public static int[][] kClosest(int[][] points, int K) {
        int N = points.length;
        int[] dists = new int[N];
        for (int i = 0; i < N; ++i)
            dists[i] = dist(points[i]);

        Arrays.sort(dists);
        int distK = dists[K-1];

        int[][] ans = new int[K][2];
        int t = 0;
        for (int i = 0; i < N; ++i)
            if (dist(points[i]) <= distK)
                ans[t++] = points[i];
        return ans;
    }

    public static int dist(int[] point) {
        return point[0] * point[0] + point[1] * point[1];
    }

    public static void main(String[] args) {

        /*
         *  The distance between (1, 3) and the origin is sqrt(10).
            The distance between (-2, 2) and the origin is sqrt(8).  Since
            sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.  We only want
            the closest K = 1 points from the origin, so the answer is just
            [[-2,2]].
         * */
        int[][] points_1 = {{1, 3}, {-2, 2}};
        int K_1 = 1;

        int[][] expected_out_1 = {{-2, 2}};
        assert kClosest(points_1, K_1) == expected_out_1;

        int[][] points_2 = {{3, 3}, {5, -1}, {-2, 4}};
        int K_2 = 2;

        int[][] expected_out_2 = {{3, 3}, {-2, 4}};
        assert kClosest(points_2, K_2) == expected_out_2;

        System.out.println("Passed all test cases");
    }
    
}
