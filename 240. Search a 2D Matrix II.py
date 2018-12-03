"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
Example:

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.
"""


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        rows = len(matrix)
        columns = len(matrix[0]) if rows else 0
        if rows == 0 or columns == 0:
            return False

        current_row = 0
        current_column = columns - 1
        while current_row <= rows - 1 and current_column >= 0:
            if matrix[current_row][current_column] == target:
                return True
            elif matrix[current_row][current_column] < target:
                current_row += 1
            else:
                current_column -= 1
        return False
