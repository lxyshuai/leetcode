"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
Example 2:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false
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

        start_row = 0
        end_row = rows - 1
        row = None
        while start_row <= end_row:
            middle_row = start_row + (end_row - start_row) / 2
            if target < matrix[middle_row][0]:
                end_row = middle_row - 1
            elif target > matrix[middle_row][-1]:
                start_row = middle_row + 1
            else:
                row = middle_row
                break
        else:
            return False

        start_column = 0
        end_column = columns - 1
        while start_column <= end_column:
            middle_column = start_column + (end_column - start_column) / 2
            if target == matrix[row][middle_column]:
                return True
            elif target < matrix[row][middle_column]:
                end_column = middle_column - 1
            else:
                start_column = middle_column + 1
        return False


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        rows = len(matrix)
        columns = len(matrix[0]) if rows else 0
        nums = rows * columns

        left = 0
        right = nums - 1
        while left <= right:
            middle = left + (right - left) / 2
            number = matrix[middle / columns][middle % columns]
            if number == target:
                return True
            elif number > target:
                right = middle - 1
            else:
                left = middle + 1
        return False


if __name__ == '__main__':
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]
    target = 3
    print Solution().searchMatrix([[1, 3]], 3)
