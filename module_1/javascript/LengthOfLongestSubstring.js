/*
 *   Title: Longest Substring Without Repeating Characters
 *   Leetcode Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
 *
 *   Problem: Given a string, find the length of the longest substring without
 *   repeating characters.
 *
 *   Input:
 *      string s    => String in which to find substring
 *   Output:
 *      number      => Length of longest substring
 *
 *   Execution: node LengthOfLongestSubstring.js
 */

/**
 * Solution #1: Using a sliding window with a set
 *
 * In this solution, we use a sliding window to keep track of the longest
 * substring. In a set, we store all the characters in the current substring
 * so that we can quickly see whether we can expand string or not.
 *
 * Time Complexity: O(n)
 * Space Complexity: O(1) - Our set has a max size of 26, so O(1)
 *
 * @param {string} s
 * @return {number}
 */

var lengthOfLongestSubstring = function(s) {
    // Set to store all chars in current substring
    var inSubstring = new Set();

    var maxLength = 0;

    // i is the start of our substring and j is the end
    // We're using a sliding window here. Expand j out as far as possible
    // until there are duplicate characters, then increment i until there
    // are no longer any duplicates
    var i = 0;
    for (var j = 0; j < s.length; j++) {
        // If the character at j is already in string, increase i until it
        // is no longer in the string so that we can update j
        while (inSubstring.has(s[j])) {
            inSubstring.delete(s.charAt(i));
            i++;
        }
        inSubstring.add(s[j]);

        // Keep track of longest substring
        maxLength = Math.max(maxLength, j-i+1);
    }

    return maxLength;
}

/**
 * Solution #2: Using a sliding window tracking previous indices
 *
 * This is similar to the previous solution except that we track the index
 * of the previous occurence of each character. This allows us to quickly
 * update i to the right value rather than having to increment
 *
 * Time Complexity: O(n)
 * Space Complexity: O(1)
 *
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstringImproved = function(s) {
    // Index of the previous occurrence of character
    var index = {}

    var maxLength = 0;

    // i is the start of our substring and j is the end
    // We're using a sliding window here. Expand j out as far as possible
    // until there are duplicate characters, then move i to 1 plus the
    // previous occurrence of that character
    var i = 0;
    for (var j = 0; j < s.length; j++) {
        // If the current character previously occurred after i's position
        // update i
        if (s[j] in index) {
            i = Math.max(index[s[j]], i);
        }

        maxLength = Math.max(maxLength, j-i+1);
        index[s[j]] = j+1;
    }

    return maxLength;
}

var tester = function() {
    console.assert(lengthOfLongestSubstringImproved("abcabcbb") === 3);
    console.assert(lengthOfLongestSubstringImproved("bbbbb") === 1);
    console.assert(lengthOfLongestSubstringImproved("pwwkew") === 3);

    // ADD YOUR OWN TESTS HERE
}

tester();
