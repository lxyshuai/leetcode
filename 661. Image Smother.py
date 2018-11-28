"""
Given a 2D integer matrix M representing the gray scale of an image, you need to design a smoother to make the gray scale of each cell becomes the average gray scale (rounding down) of all the 8 surrounding cells and itself. If a cell has less than 8 surrounding cells, then use as many as you can.

Example 1:
Input:
[[1,1,1],
 [1,0,1],
 [1,1,1]]
Output:
[[0, 0, 0],
 [0, 0, 0],
 [0, 0, 0]]
Explanation:
For the point (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
For the point (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
For the point (1,1): floor(8/9) = floor(0.88888889) = 0
Note:
The value in the given matrix is in the range of [0, 255].
The length and width of the given matrix are in the range of [1, 150].
"""


class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        rows = len(M)
        columns = len(M[0]) if rows else 0
        result = [[0] * columns for _ in range(rows)]

        for row in range(rows):
            for column in range(columns):
                count = 0
                for neighbor_row in (row - 1, row, row + 1):
                    for neighbor_column in (column - 1, column, column + 1):
                        if 0 <= neighbor_row <= rows - 1 and 0 <= neighbor_column <= columns - 1:
                            result[row][column] += M[neighbor_row][
                                neighbor_column]
                            count += 1
                result[row][column] /= count
        return result


class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """

        def get_average(matrix, row, column, rows, columns):
            count = 0
            total_sum = 0
            for _row in (row - 1, row, row + 1):
                for _column in (column - 1, column, column + 1):
                    if 0 <= _row < rows and 0 <= _column < columns:
                        total_sum += matrix[_row][_column]
                        count += 1
            return total_sum / count

        rows = len(M)
        columns = len(M[0]) if rows else 0
        result = [[0 for _ in range(columns)] for _ in range(rows)]
        for row in range(rows):
            for column in range(columns):
                result[row][column] = get_average(M, row, column, rows, columns)
        return result


if __name__ == '__main__':
    print Solution().imageSmoother([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
