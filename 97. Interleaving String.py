"""
Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

Example 1:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Example 2:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
"""


class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """

        def process(s1_current_index, s2_current_index, s3_current_index):
            if s1_current_index == len(s1):
                return s2[s2_current_index:] == s3[s3_current_index:]
            if s2_current_index == len(s2):
                return s1[s1_current_index:] == s3[s3_current_index:]

            result = False
            if s1[s1_current_index] == s3[s3_current_index]:
                result = result or process(s1_current_index + 1, s2_current_index, s3_current_index + 1)
            if s2[s2_current_index] == s3[s3_current_index]:
                result = result or process(s1_current_index, s2_current_index + 1, s3_current_index + 1)
            return result

        return process(0, 0, 0)


class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s1) + len(s2) != len(s3):
            return False
        dp = [[False for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
        dp[len(s1)][len(s2)] = True

        for _s2 in range(len(s2) - 1, -1, -1):
            if s2[_s2:] == s3[len(s1) + _s2:]:
                dp[len(s1)][_s2] = True
            else:
                dp[len(s1)][_s2] = False

        for _s1 in range(len(s1) - 1, -1, -1):
            if s1[_s1:] == s3[len(s2) + _s1:]:
                dp[_s1][len(s2)] = True
            else:
                dp[_s1][len(s2)] = False

        for _s1 in range(len(s1) - 1, -1, -1):
            for _s2 in range(len(s2) - 1, -1, -1):
                if s1[_s1] == s3[_s2 + _s1]:
                    dp[_s1][_s2] = dp[_s1][_s2] or dp[_s1 + 1][_s2]
                if s2[_s2] == s3[_s2 + _s1]:
                    dp[_s1][_s2] = dp[_s1][_s2] or dp[_s1][_s2 + 1]
        return dp[0][0]
