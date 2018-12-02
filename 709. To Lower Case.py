"""
Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.



Example 1:

Input: "Hello"
Output: "hello"
Example 2:

Input: "here"
Output: "here"
Example 3:

Input: "LOVELY"
Output: "lovely"
"""


class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        result = ''
        for index, char in enumerate(str):
            if 65 <= ord(char) <= 90:
                result += chr(ord(char) + 32)
            else:
                result += char
        return result
