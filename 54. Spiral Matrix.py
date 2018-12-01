"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        rows = len(matrix)
        columns = len(matrix[0]) if rows else 0
        left = 0
        right = columns - 1
        up = 0
        down = rows - 1

        result = []
        while True:
            for column in range(left, right + 1):
                result.append(matrix[up][column])
            up += 1
            if up > down:
                break

            for row in range(up, down + 1):
                result.append(matrix[row][right])
            right -= 1
            if right < left:
                break

            for column in range(right, left - 1, -1):
                result.append(matrix[down][column])
            down -= 1
            if down < up:
                break

            for row in range(down, up - 1, -1):
                result.append(matrix[row][left])
            left += 1
            if left > right:
                break
        return result
