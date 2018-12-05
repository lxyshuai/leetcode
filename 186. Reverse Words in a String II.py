"""
Given an input string, reverse the string word by word. A word is defined as a sequence of non-space characters.
The input string does not contain leading or trailing spaces and the words are always separated by a single space.
For example,
Given s = "the sky is blue",
return "blue is sky the".
Could you do it in-place without allocating extra space?
"""


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        def reverse(string_list, left, right):
            while left < right:
                string_list[left], string_list[right] = string_list[right], string_list[left]
                left += 1
                right -= 1

        string_list = list(s)
        reverse(string_list, 0, len(string_list) - 1)
        left = 0
        right = 0
        while right < len(string_list):
            if string_list[right].isspace():
                reverse(string_list, left, right - 1)
                left = right + 1
            right += 1
        return ''.join(string_list)


if __name__ == '__main__':
    print Solution().reverseWords('a b c d')
