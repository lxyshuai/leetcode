# coding=utf-8
"""
Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

Range Sum Query 2D
The above rectangle (with the red border) is defined by (row1, col1) = (2, 1) and (row2, col2) = (4, 3), which contains sum = 8.

Example:
Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
sumRegion(1, 1, 2, 2) -> 11
sumRegion(1, 2, 2, 4) -> 12
Note:
You may assume that the matrix does not change.
There are many calls to sumRegion function.
You may assume that row1 ≤ row2 and col1 ≤ col2.
"""


class NumMatrix(object):
    def __init__(self, matrix):
        if matrix is None or not matrix:
            return
        n, m = len(matrix), len(matrix[0])
        self.sums = [[0 for j in xrange(m + 1)] for i in xrange(n + 1)]
        for i in xrange(1, n + 1):
            for j in xrange(1, m + 1):
                self.sums[i][j] = matrix[i - 1][j - 1] + self.sums[i][j - 1] + self.sums[i - 1][j] - self.sums[i - 1][
                    j - 1]

    def sumRegion(self, row1, col1, row2, col2):
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        return self.sums[row2][col2] - self.sums[row2][col1 - 1] - self.sums[row1 - 1][col2] + self.sums[row1 - 1][
            col1 - 1]


class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        rows = len(matrix)
        columns = len(matrix[0]) if rows else 0
        if rows == 0 or columns == 0:
            return
        self.dp = [[0 for _ in range(columns)] for _ in range(rows)]
        self.dp[0][0] = matrix[0][0]
        for row in range(1, rows):
            self.dp[row][0] = self.dp[row - 1][0] + matrix[row][0]
        for column in range(1, columns):
            self.dp[0][column] = self.dp[0][column - 1] + matrix[0][column]
        for row in range(1, rows):
            for column in range(1, columns):
                self.dp[row][column] = self.dp[row - 1][column] + self.dp[row][column - 1] - self.dp[row - 1][
                    column - 1] + matrix[row][column]

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.dp[row2][col2] + (self.dp[row1 - 1][col1 - 1] if row1 > 0 and col1 > 0 else 0) - (
            self.dp[row2][col1 - 1] if col1 > 0 else 0) - (self.dp[row1 - 1][col2] if row1 > 0 else 0)

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
