"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


Above is a 7 x 3 grid. How many possible unique paths are there?

Note: m and n will be at most 100.

Example 1:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right
Example 2:

Input: m = 7, n = 3
Output: 28
"""


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        self.count = 0

        def process(row, column):
            if row >= m or column >= n:
                return
            if row == m - 1 and column == n - 1:
                self.count += 1
                return
            process(row + 1, column)
            process(row, column + 1)

        process(0, 0)
        return self.count


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0 for _ in range(m)] for _ in range(n)]
        dp[n - 1][m - 1] = 0
        for _n in range(n):
            dp[_n][m - 1] = 1
        for _m in range(m):
            dp[n - 1][_m] = 1
        for _n in range(n - 2, -1, -1):
            for _m in range(m - 2, -1, -1):
                dp[_n][_m] = dp[_n + 1][_m] + dp[_n][_m + 1]
        return dp[0][0]
