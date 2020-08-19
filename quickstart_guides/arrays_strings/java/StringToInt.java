/*
 *   Title: Convert string to integer
 *   Problem:
 *       Implement atoi which converts a string to an integer.
 *
 *       The function first discards as many whitespace characters as necessary
 *       until the first non-whitespace character is found. Then, starting from
 *       this character, takes an optional initial plus or minus sign followed
 *       by as many numerical digits as possible, and interprets them as a
 *       numerical value.
 *
 *       The string can contain additional characters after those that form the
 *       integral number, which are ignored and have no effect on the behavior
 *       of this function.
 *
 *       If the first sequence of non-whitespace characters in str is not a
 *       valid integral number, or if no such sequence exists because either str
 *       is empty or it contains only whitespace characters, no conversion is
 *       performed.
 *
 *       If no valid conversion could be performed, a zero value is returned.
 *
 *       Note:
 *
 *       Only the space character ' ' is considered as whitespace character.
 *       Assume we are dealing with an environment which could only store
 *       integers within the 32-bit signed integer range: [−231,  231 − 1]. If
 *       the numerical value is out of the range of representable values,
 *       INT_MAX (231 − 1) or INT_MIN (−231) is returned.
 *
 *   Execution: javac StringToInt.java && java StringToInt
 */
import java.util.*;


public class StringToInt {
    static int stringToInt(String str) {
        if(str.length() == 0) return 0;
        boolean neg = false;
        int i = 0;
        while(i < str.length() && str.charAt(i) == ' ') {
            i++;
        }
        str = str.substring(i, str.length());
        if(str.length() > 0 && str.charAt(0) == '-') {
            neg = true;
            str = str.substring(1, str.length());
        }
        if(str.length() > 0 && str.charAt(0) == '+') {
            if(neg) return 0;
            str = str.substring(1, str.length());
        }
        if(str.length() == 0 || !Character.isDigit(str.charAt(0))) return 0;
        i = 0;
        while(i < str.length() && Character.isDigit(str.charAt(i))) {
            i++;
        }
        str = str.substring(0, i);
        StringBuffer sb = new StringBuffer();
        for(int j=0;j<str.length();j++){
            sb.append(str.charAt(j));
        }
        String result = sb.toString();
        if(neg) {
           result = "-"+ result;
        }
        int resultInt = 0;
        try {
           resultInt =  Integer.valueOf(result);
        }
        catch(Exception ex) {
            if(neg) return Integer.MIN_VALUE;
            return Integer.MAX_VALUE;
        }
        return resultInt;
    }
    public static void main(String[] args) {
        assert stringToInt("42") == 42;
        assert stringToInt("    -42") == -42;
        assert stringToInt("4193 with words") == 4193;
        assert stringToInt("words and 987") == 0;
        assert stringToInt("-91283472332") == -2147483648;

        System.out.println("Passed all test cases");
    }
    
}
