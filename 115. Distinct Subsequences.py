"""
Given a string S and a string T, count the number of distinct subsequences of S which equals T.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Example 1:

Input: S = "rabbbit", T = "rabbit"
Output: 3
Explanation:

As shown below, there are 3 ways you can generate "rabbit" from S.
(The caret symbol ^ means the chosen letters)

rabbbit
^^^^ ^^
rabbbit
^^ ^^^^
rabbbit
^^^ ^^^
Example 2:

Input: S = "babgbag", T = "bag"
Output: 5
Explanation:

As shown below, there are 5 ways you can generate "bag" from S.
(The caret symbol ^ means the chosen letters)

babgbag
^^ ^
babgbag
^^    ^
babgbag
^    ^^
babgbag
  ^  ^^
babgbag
    ^^^
"""


class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """

        def process(before_string, current_index):
            if current_index == len(s):
                if before_string == t:
                    self.count += 1
                return
            process(before_string + s[current_index], current_index + 1)
            process(before_string, current_index + 1)

        self.count = 0
        process('', 0)
        return self.count


class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """

        def process(s_current_index, t_current_index):
            if t_current_index == len(t):
                return 1
            if s_current_index == len(s):
                return 0

            total = 0
            if s[s_current_index] == t[t_current_index]:
                total += process(s_current_index + 1, t_current_index + 1)
            total += process(s_current_index + 1, t_current_index)
            return total

        return process(0, 0)


class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        if len(s) < len(t):
            return 0
        dp = [[0 for _ in range(len(s) + 1)] for _ in range(len(t) + 1)]
        dp[len(t)][len(s)] = 1
        for _t in range(len(t)):
            dp[_t][len(s)] = 0
        for _s in range(len(s)):
            dp[len(t)][_s] = 1

        for _t in range(len(t) - 1, -1, -1):
            for _s in range(len(s) - 1, -1, -1):
                if s[_s] == t[_t]:
                    dp[_t][_s] += dp[_t + 1][_s + 1] + dp[_t][_s + 1]
                else:
                    dp[_t][_s] += dp[_t][_s + 1]
        return dp[0][0]
