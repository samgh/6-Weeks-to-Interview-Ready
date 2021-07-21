"""
Title: Longest Substring Without Repeating Characters
Leetcode Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/

Problem: Given a string, find the length of the longest substring without
repeating characters.

Input:
  string: s   => String in which to find substring
Output:
  int         => Length of longest substring

Execution: python length_of_longest_substring.py
"""
import unittest

"""
Solution #1: Using a sliding window with a set

In this solution, we use a sliding window to keep track of the longest
substring. In a set, we store all the characters in the current substring
so that we can quickly see whether we can expand string or not.

Time Complexity: O(n)
Space Complexity: O(1) - Our set has a max size of 26, so O(1)
"""
def length_of_longest_substring(s: str)->int:
    # Set to store all chars in current substring
    in_substring = set()
    max_length = 0

    # i is the start of our substring and j is the end
    # We're using a sliding window here. Expand j out as far as possible
    # until there are duplicate characters, then increment i until there
    # are no longer any duplicates
    i = 0
    for j in range(len(s)):

        # If the character at j is already in string, increase i until it
        # is no longer in the string so that we can update j
        while s[j] in in_substring:
            in_substring.remove(s[i])
            i = i+1
        in_substring.add(s[j])

        # Keep track of longest substring
        max_length = max(max_length, j-i+1)

    return max_length

"""
Solution #2: Using a sliding window tracking previous indices

This is similar to the previous solution except that we track the index
of the previous occurence of each character. This allows us to quickly
update i to the right value rather than having to increment

Time Complexity: O(n)
Space Complexity: O(1)
"""
def length_of_longest_substring_improved(s: str)->int:
    # Index of the previous occurence of character
    index = {}

    max_length = 0;

    # i is the start of our substring and j is the end
    # We're using a sliding window here. Expand j out as far as possible
    # until there are duplicate characters, then move i to 1 plus the
    # previous occurrence of that character
    i = 0
    for j in range(len(s)):
        # If the current character previously occurred after i's position
        # update i
        if s[j] in index:
            i = max(index[s[j]], i)

        max_length = max(max_length, j-i+1)
        index[s[j]] = j+1

    return max_length

class TestLengthOfLongestSubstring(unittest.TestCase):
    """Unit tests for length_of_longest_substring."""

    def test_1(self):
        """Test for string: abcabcbb."""
        self.assertEqual(length_of_longest_substring_improved("abcabcbb"), 3)
        print("Explanation: The answer is 'abc', with the length of 3.")

    def test_2(self):
        """Test for string: bbbbb."""
        self.assertEqual(length_of_longest_substring_improved("bbbbb"), 1)
        print("Explanation: The answer is 'b', with the length of 1.")

    def test_3(self):
        """Test for string: pwwkew."""
        self.assertEqual(length_of_longest_substring_improved("pwwkew"), 3)
        print("Explanation: The answer is 'wke', with the length 3.")
        print("Note that the answer must be a substring, 'pwke' ")
        print("is a subsequence and not a substring.")

    # ADD YOUR TESTS HERE

if __name__ == '__main__':
    unittest.main()
