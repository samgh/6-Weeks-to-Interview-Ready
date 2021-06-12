/*
 *   Title: Find Anagrams
 *   Leetcode Link: https://leetcode.com/problems/find-all-anagrams-in-a-string/
 *
 *   Problem: Given a string s and a non-empty string p, find all the start
 *   indices of p's anagrams in s.
 *
 *   Input:
 *      string s       => string to seach
 *      string p       => string to find anagrams of
 *   Output:
 *      number[]       => inidices of anagrams in s
 *
 *   Execution: node FindAnagrams.js
 */

/**
 * Start by counting the number of occurrences of each character in p. Then
 * we use a sliding window to find every substring of s that contains the
 * same set of characters.
 *
 * Time Complexity: O(n)
 * Space Complexity: O(1)
 *
 * @param {string} s
 * @param {string} p
 * @return {number[]}
 */
var findAnagrams = function(s, p) {
    results = [];

    // If either string is empty or p is longer than s, we have no results
    if (s.length == 0 || p.length == 0 || s.length < p.length) {
        return results;
    }

    // Counts of characters. We are told that all chars are lowercase English
    // characters
    var pChars = [];
    var sChars = [];
    var arraySize = 26;
    while(arraySize--) {
        pChars.push(0);
        sChars.push(0);
    }

    // Cound characters in p
    [...p].forEach(function(c) {
        pChars[charIndex(c)]++;
    });

   // Track the start and end of our window in s, along with the chars in
   // that window. This should always be the size of p
   var start = 0
   var end = p.length-1;

   // Fill up initial sChars
   for (var i = 0; i < p.length; i++) sChars[charIndex(s.charAt(i))]++;

   // Iterate through every substring of length p
   while (end < s.length-1) {
       // This is a slow but constant time operation because the arrays
       // are always the same size ragardless of the input
       if (arraysEqual(pChars, sChars)) results.push(start);

       // Move our window by 1
       sChars[charIndex(s.charAt(start))] -= 1;
       start++; end++;
       sChars[charIndex(s.charAt(end))] += 1;
   }

   // Get the last substring if it's valid
   if (arraysEqual(pChars, sChars)) results.push(start);

   return results;
}

/**
 * Helper to convert character to index
 *
 * @param{char}
 * @return{number}
 */
var charIndex = function(c) {
    if (c.length == 1) {
        var result = c.charCodeAt()-'a'.charCodeAt();
        if (result >= 0 && result < 26) return result;
    }
    return -1;
}

/**
 * Helper to compare values of 2 arrays
 *
 * @param {number[]} a
 * @param {number[]} b
 * @return {boolean}
*/
var arraysEqual = function(a, b) {
    if (!a || !b) return false;
    if (a.length != b.length) return false;
    for (var i = 0; i < a.length; i++) {
        if (a[i] !== b[i]) return false;
    }
    return true;
}

// Test casese
var tester = function() {
    console.assert(arraysEqual(findAnagrams("cbaebabacd", "abc"), [0,6]));
    console.assert(arraysEqual(findAnagrams("abab", "ab"), [0,1,2]));

    // ADD YOUR OWN TEST HERE
}

tester();
