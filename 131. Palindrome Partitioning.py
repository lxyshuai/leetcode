# coding=utf-8
"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example:

Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]
"""


class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        """
        需要一个判断是否是回文串的函数 is_palindrome
        需要一个递归遍历字符串的函数process(str, path):
            1.首先判断要当前前缀是否为回文串,不是直接continue
            2.如果当前前缀是回文串,对剩下的字符串递归调用process(str[:],path+...)
        """

        def is_palindrome(string):
            left = 0
            right = len(string) - 1
            while left < right:
                if string[left] != string[right]:
                    return False
                left += 1
                right -= 1
            return True

        def process(string, path):
            if not string:
                result.append(path)
                return
            for index in range(0, len(string)):
                prefix = string[0:index + 1]
                if is_palindrome(prefix):
                    process(string[index + 1:], path + [prefix])

        if not s:
            return [[]]
        result = []
        process(s, [])
        return result


class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        """
        需要一个判断是否是回文串的函数 is_palindrome
        需要一个递归遍历字符串的函数process(str, path):
            1.首先判断要当前前缀是否为回文串,不是直接continue
            2.如果当前前缀是回文串,对剩下的字符串递归调用process(str[:],path+...)
        用set记录下已经计算过的回文串
        """

        def is_palindrome(string):
            if string in is_palindrome_set:
                return True
            left = 0
            right = len(string) - 1
            while left < right:
                if string[left] != string[right]:
                    return False
                left += 1
                right -= 1
            is_palindrome_set.add(string)
            return True

        def process(string, path):
            if not string:
                result.append(path)
                return
            for index in range(0, len(string)):
                prefix = string[0:index + 1]
                if is_palindrome(prefix):
                    process(string[index + 1:], path + [prefix])

        if not s:
            return [[]]
        is_palindrome_set = set()
        result = []
        process(s, [])
        return result


if __name__ == '__main__':
    print Solution().partition('aab')
