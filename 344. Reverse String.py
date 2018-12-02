"""
Write a function that takes a string as input and returns the string reversed.

Example 1:

Input: "hello"
Output: "olleh"
Example 2:

Input: "A man, a plan, a canal: Panama"
Output: "amanaP :lanac a ,nalp a ,nam A"
"""


class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 1:
            return s
        return self.reverseString(s[len(s) / 2:]) + self.reverseString(s[:len(s) / 2])


class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = list(s)
        left = 0
        right = len(s) - 1
        while left < right:
            result[left], result[right] = result[right], result[left]
            left += 1
            right -= 1
        return "".join(result)


class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]
