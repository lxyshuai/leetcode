"""
Given an input string, reverse the string word by word.

Example:

Input: "the sky is blue",
Output: "blue is sky the".
Note:

A word is defined as a sequence of non-space characters.
Input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
You need to reduce multiple spaces between two words to a single space in the reversed string.
Follow up: For C programmers, try to solve it in-place in O(1) space.
"""
import re


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.strip()
        words = re.split(' +', s)
        words = words[::-1]
        return ' '.join(words)


class Solution(object):
    def reverseWords(self, s):
        arr = list(s)
        self.reverse_string(arr, 0, len(arr) - 1)
        self.reverse_word(arr)
        word = self.trim_sides(arr)
        res = self.trim_space(word)
        return ''.join(res)

    def reverse_string(self, arr, l, r):
        '''reverse a given string'''
        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1

    def reverse_word(self, arr):
        '''reverse every words in a string'''
        left = 0
        right = 0
        while right < len(arr):
            while right < len(arr) and not arr[right].isspace():
                right += 1
            self.reverse_string(arr, left, right - 1)
            right += 1
            left = right

    def trim_sides(self, arr):
        '''str.strip() basically'''
        if ''.join(arr).isspace():
            return []
        left = 0
        right = len(arr) - 1
        while left < right:
            if arr[right].isspace():
                right -= 1
            else:
                break
        while left < right:
            if arr[left].isspace():
                left += 1
            else:
                break
        return arr[left:right + 1]

    def trim_space(self, word):
        '''remove duplicating space in a word'''
        if not word: return []
        res = [word[0]]
        for i in range(1, len(word)):
            if res[-1].isspace() and word[i].isspace(): continue
            res.append(word[i])
        return res
