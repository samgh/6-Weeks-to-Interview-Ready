/*
 *   Title: Compare version
 *   Problem:
 *         Compare two version numbers version1 and version2.  If version1 >
 *        version2 return 1; if version1 < version2 return -1;otherwise return
 *        0.
 *
 *       You may assume that the version strings are non-empty and contain only
 *       digits and the . character.
 *
 *       The . character does not represent a decimal point and is used to
 *       separate number sequences.
 *
 *       For instance, 2.5 is not "two and a half" or "half way to version
 *       three", it is the fifth second-level revision of the second first-level
 *       revision.
 *
 *       You may assume the default revision number for each level of a version
 *       number to be 0. For example, version number 3.4 has a revision number
 *       of 3 and 4 for its first and second level revision number. Its third
 *       and fourth level revision number are both 0.
 *
 *   Execution: javac CompareVersion.java && java CompareVersion
 */
import java.util.*;


public class CompareVersion {
    static int compareVersion(String version1, String version2) {
        version1 = version1 + ".";
        version2 = version2 + ".";
        int l1 = version1.length();
        int l2 = version2.length();
        int i=0, j=0, v1, v2;
        while(i<l1 || j<l2) {
            if (i < l1) {
                int x1 = version1.indexOf('.', i);
                v1 = Integer.parseInt(version1.substring(i, x1));
                i = x1+1;
            } else {
                v1 = 0;
            }

            if (j < l2) {
                int x2 = version2.indexOf('.', j);
                v2 = Integer.parseInt(version2.substring(j, x2));
                j = x2+1;
            } else {
                v2 = 0;
            }

            if(v1 < v2) {
                return -1;
            } else if (v1 > v2) {
                return 1;
            }
        }
        return 0;
    }

    // Sample test cases
    public static void main(String[] args) {
        assert compareVersion("0.1", "1.1") == -1;
        assert compareVersion("1.0.1", "1") == 1;
        assert compareVersion("7.5.2.4", "7.5.3") == -1;
        assert compareVersion("1.01", "1.001") == 0;
        assert compareVersion("1.0", "1.0.0") == 0;

        System.out.println("Passed all test cases");
    }
}
