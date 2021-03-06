"""
In MATLAB, there is a very useful function called 'reshape', which can reshape a matrix into a new one with different size but keep its original data.

You're given a matrix represented by a two-dimensional array, and two positive integers r and c representing the row number and column number of the wanted reshaped matrix, respectively.

The reshaped matrix need to be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the 'reshape' operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

Example 1:
Input:
nums =
[[1,2],
 [3,4]]
r = 1, c = 4
Output:
[[1,2,3,4]]
Explanation:
The row-traversing of nums is [1,2,3,4]. The new reshaped matrix is a 1 * 4 matrix, fill it row by row by using the previous list.
Example 2:
Input:
nums =
[[1,2],
 [3,4]]
r = 2, c = 4
Output:
[[1,2],
 [3,4]]
Explanation:
There is no way to reshape a 2 * 2 matrix to a 2 * 4 matrix. So output the original matrix.
Note:
The height and width of the given matrix is in range [1, 100].
The given r and c are all positive.
"""


class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        rows = len(nums)
        columns = len(nums[0]) if rows else 0
        if rows * columns < c * r:
            return nums
        result = [[0 for _ in range(c)] for _ in range(r)]
        new_row = 0
        new_column = 0
        for row in range(rows):
            for column in range(columns):
                result[new_row][new_column] = nums[row][column]
                if new_column + 1 == c:
                    new_row += 1
                    new_column = 0
                else:
                    new_column += 1
        return result


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits[-1] += 1
        current_index = len(digits) - 1
        while current_index >= 0:
            if digits[current_index] == 10:
                digits[current_index] = 0
                if current_index == 0:
                    digits.insert(0, 1)
                else:
                    digits[current_index - 1] += 1
                current_index -= 1
            else:
                break
        return digits


if __name__ == '__main__':
    print Solution().matrixReshape([[1, 2],
                                    [3, 4]], 4, 1)
