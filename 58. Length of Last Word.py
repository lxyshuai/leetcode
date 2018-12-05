"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

Example:

Input: "Hello World"
Output: 5
"""


class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None and len(s) == 0:
            return 0
        last = -1
        while last >= -len(s) and s[last] == ' ':
            last -= 1
        first = last
        while first >= -len(s) and s[first] != ' ':
            first -= 1
        return last - first
