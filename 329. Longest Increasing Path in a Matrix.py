"""
Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

Example 1:

Input: nums =
[
  [9,9,4],
  [6,6,8],
  [2,1,1]
]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].
Example 2:

Input: nums =
[
  [3,4,5],
  [3,2,6],
  [2,2,1]
]
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
"""


class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        rows = len(matrix)
        columns = len(matrix[0]) if rows else 0

        def process(row, column):
            if row >= rows or row < 0 or column >= columns or column < 0:
                return 0
            max_length = 0
            for next_row, next_column in (
                    (row + 1, column), (row - 1, column), (row, column + 1),
                    (row, column - 1)):
                if rows > next_row >= 0 and columns > next_column >= 0:
                    if matrix[next_row][next_column] > matrix[row][column]:
                        max_length = max(max_length,
                                         process(next_row, next_column))
                    else:
                        pass
                else:
                    max_length = max(max_length, process(next_row,
                                                         next_column))
            return max_length + 1

        result = 0
        for row in range(rows):
            for column in range(columns):
                result = max(result, process(row, column))
        return result


class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """

        def process(row, column):
            if row >= rows or row < 0 or column >= columns or column < 0:
                return 0
            if dp[row][column]:
                return dp[row][column]
            max_length = 0
            for next_row, next_column in (
                    (row + 1, column), (row - 1, column), (row, column + 1),
                    (row, column - 1)):
                if rows > next_row >= 0 and columns > next_column >= 0:
                    if matrix[next_row][next_column] > matrix[row][column]:
                        max_length = max(max_length,
                                         process(next_row, next_column))
                    else:
                        pass
                else:
                    max_length = max(max_length, process(next_row,
                                                         next_column))
            dp[row][column] = 1 + max_length
            return max_length + 1

        rows = len(matrix)
        columns = len(matrix[0]) if rows else 0
        result = 0
        dp = [[0 for _ in range(columns)] for _ in range(rows)]
        for row in range(rows):
            for column in range(columns):
                result = max(result, process(row, column))
        return result


if __name__ == '__main__':
    nums = [
        [7, 6, 1, 1],
        [2, 7, 6, 0],
        [1, 3, 5, 1],
        [6, 6, 3, 2]
    ]

    print Solution().longestIncreasingPath(nums)
