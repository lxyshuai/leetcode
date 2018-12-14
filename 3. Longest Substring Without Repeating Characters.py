"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        last_appear_dict = {}
        max_length = 0
        left = -1
        for index, char in enumerate(s):
            if char in last_appear_dict and left < last_appear_dict[char]:
                left = last_appear_dict[char]
            last_appear_dict[char] = index
            max_length = max(max_length, index - left)
        return max_length
