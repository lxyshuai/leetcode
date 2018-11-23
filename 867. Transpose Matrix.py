"""
Given a matrix A, return the transpose of A.

The transpose of a matrix is the matrix flipped over it's main diagonal, switching the row and column indices of the matrix.



Example 1:

Input: [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]
Example 2:

Input: [[1,2,3],[4,5,6]]
Output: [[1,4],[2,5],[3,6]]


Note:

1 <= A.length <= 1000
1 <= A[0].length <= 1000
"""


class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        rows = len(A)
        columns = len(A[0]) if rows else 0
        new_rows = columns
        new_columns = rows
        result = [[0 for _ in range(new_columns)] for _ in range(new_rows)]

        for row in range(rows):
            for column in range(columns):
                result[column][row] = A[row][column]

        return result


class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        rows = len(A)
        columns = len(A[0])
        result_matrix = [[0 for _ in range(rows)] for _ in range(columns)]

        for row in range(rows):
            for column in range(columns):
                result_matrix[column][row] = A[row][column]
        return result_matrix


if __name__ == '__main__':
    print Solution().transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
