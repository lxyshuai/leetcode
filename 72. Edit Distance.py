"""
Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character
Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation:
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
"""


class Solution(object):
    def minDistance(self, w1, w2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """

        def process(w1_current_index, w2_current_index):
            if w2_current_index == len(w2):
                return len(w1) - w1_current_index
            if w1_current_index == len(w1):
                return len(w2) - w2_current_index

            if w1[w1_current_index] == w2[w2_current_index]:
                return process(w1_current_index + 1, w2_current_index + 1)
            else:
                insert = process(w1_current_index, w2_current_index + 1)
                delete = process(w1_current_index + 1, w2_current_index)
                replace = process(w1_current_index + 1, w2_current_index + 1)
                return 1 + min(insert, delete, replace)

        return process(0, 0)


class Solution(object):
    def minDistance(self, w1, w2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dp = [[0 for _ in range(len(w1) + 1)] for _ in range(len(w2) + 1)]
        dp[len(w2)][len(w1)] = 0
        for _w1 in range(0, len(w1)):
            dp[len(w2)][_w1] = len(w1) - _w1
        for _w2 in range(0, len(w2)):
            dp[_w2][len(w1)] = len(w2) - _w2

        for _w2 in range(len(w2) - 1, -1, -1):
            for _w1 in range(len(w1) - 1, -1, -1):
                if w1[_w1] == w2[_w2]:
                    dp[_w2][_w1] = dp[_w2 + 1][_w1 + 1]
                else:
                    insert = dp[_w2 + 1][_w1]
                    delete = dp[_w2][_w1 + 1]
                    replace = dp[_w2 + 1][_w1 + 1]
                    dp[_w2][_w1] = 1 + min(insert, delete, replace)
        return dp[0][0]


if __name__ == '__main__':
    print Solution().minDistance('horse', 'ros')
