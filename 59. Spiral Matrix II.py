"""
Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:

Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""


class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        rows = n
        columns = n
        left = 0
        right = columns - 1
        up = 0
        down = rows - 1

        result = [[0 for _ in range(n)] for _ in range(n)]
        count = 1
        while True:
            for column in range(left, right + 1):
                result[up][column] = count
                count += 1
            up += 1
            if up > down:
                break

            for row in range(up, down + 1):
                result[row][right] = count
                count += 1
            right -= 1
            if right < left:
                break

            for column in range(right, left - 1, -1):
                result[down][column] = count
                count += 1
            down -= 1
            if down < up:
                break

            for row in range(down, up - 1, -1):
                result[row][left] = count
                count += 1
            left += 1
            if left > right:
                break
        return result
