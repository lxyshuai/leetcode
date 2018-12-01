# coding=utf-8
"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
"""


class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.result = float('inf')
        rows = len(grid)
        columns = len(grid[0]) if rows else 0

        def process(row, column, before_sum):
            if row >= rows or column >= columns:
                return
            if row == rows - 1 and column == columns - 1:
                self.result = min(self.result, before_sum + grid[row][column])
                return
            process(row + 1, column, before_sum + grid[row][column])
            process(row, column + 1, before_sum + grid[row][column])

        process(0, 0, 0)
        return self.result


class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        columns = len(grid[0]) if rows else 0
        dp = [[0 for _ in range(columns)] for _ in range(rows)]
        dp[rows - 1][columns - 1] = grid[rows - 1][columns - 1]
        for column in range(columns - 2, -1, -1):
            dp[rows - 1][column] = dp[rows - 1][column + 1] + grid[rows - 1][column]
        for row in range(rows - 2, -1, -1):
            dp[row][columns - 1] = dp[row + 1][columns - 1] + grid[row][columns - 1]

        for row in range(rows - 2, -1, -1):
            for column in range(columns - 2, -1, -1):
                dp[row][column] = min(dp[row + 1][column], dp[row][column + 1]) + grid[row][column]
        return dp[0][0]
