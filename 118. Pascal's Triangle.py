"""
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []
        for number in range(numRows):
            row = [None for _ in range(number + 1)]
            row[0] = 1
            row[-1] = 1
            for num in range(1, number):
                row[num] = result[number - 1][num] + result[number - 1][num - 1]
            result.append(row)
        return result


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []
        for row_index in range(numRows):
            row = [0 for _ in range(row_index + 1)]
            row[0] = 1
            row[-1] = 1
            for index in range(1, row_index):
                row[index] = result[row_index - 1][index - 1] + result[row_index - 1][index]
            result.append(row)
        return result
