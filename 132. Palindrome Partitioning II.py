# coding=utf-8
"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

Example:

Input: "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
"""


class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        """
        需要一个判断是否是回文串的函数 is_palindrome
        需要一个递归遍历字符串的函数process(index, count):
            1.首先判断要当前前缀是否为回文串,不是直接continue
            2.如果当前前缀是回文串,可以切一刀,对剩下的字符串递归调用process(index + 1, count + 1)
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

        def process(begin_index, count):
            if begin_index == len(s):
                return count - 1
            min_count = float('inf')
            for end_index in range(begin_index + 1, len(s) + 1):
                prefix = s[begin_index:end_index]
                if is_palindrome(prefix):
                    min_count = min(min_count, process(end_index, count + 1))
            return min_count

        return process(0, 0)


class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """

        # def is_palindrome(string):
        #     if string in is_palindrome_set:
        #         return True
        #     left = 0
        #     right = len(string) - 1
        #     while left < right:
        #         if string[left] != string[right]:
        #             return False
        #         left += 1
        #         right -= 1
        #     is_palindrome_set.add(string)
        #     return True
        def is_palindrome(string):
            return string == string[::-1]

        if not s:
            return 0
        is_palindrome_set = set()
        dp = [float('inf') for _ in range(len(s) + 1)]
        dp[-1] = -1
        dp[-2] = 0
        for index in range(len(s) - 2, -1, -1):
            for end_index in range(index + 1, len(s) + 1):
                prefix = s[index: end_index]
                if is_palindrome(prefix):
                    dp[index] = min(dp[index], 1 + dp[end_index])
        return dp[0]


if __name__ == '__main__':
    print Solution().minCut('aab')
