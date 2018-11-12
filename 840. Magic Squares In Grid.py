"""
A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column, and both diagonals all have the same sum.

Given an grid of integers, how many 3 x 3 "magic square" subgrids are there?  (Each subgrid is contiguous).



Example 1:

Input: [[4,3,8,4],
        [9,5,1,9],
        [2,7,6,2]]
Output: 1
Explanation:
The following subgrid is a 3 x 3 magic square:
438
951
276

while this one is not:
384
519
762

In total, there is only one magic square inside the given grid.
Note:

1 <= grid.length <= 10
1 <= grid[0].length <= 10
0 <= grid[i][j] <= 15
"""


class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        columns = len(grid[0]) if rows else 0

        def magic(a, b, c, d, e, f, g, h, i):
            return (sorted([a, b, c, d, e, f, g, h, i]) == range(1, 10) and
                    (a + b + c == d + e + f == g + h + i == a + d + g ==
                     b + e + h == c + f + i == a + e + i == c + e + g == 15))

        result = 0
        for row in xrange(1, rows - 1):
            for column in xrange(1, columns - 1):
                if grid[row][column] != 5:
                    continue
                if magic(grid[row - 1][column - 1], grid[row - 1][column],
                         grid[row - 1][column + 1],
                         grid[row][column - 1], grid[row][column],
                         grid[row][column + 1],
                         grid[row + 1][column - 1], grid[row + 1][column],
                         grid[row + 1][column + 1]):
                    result += 1
        return result


if __name__ == '__main__':
    print Solution().numMagicSquaresInside(
        [[3, 10, 2, 3, 4],
         [4, 5, 6, 8, 1],
         [8, 8, 1, 6, 8],
         [1, 3, 5, 7, 1],
         [9, 4, 9, 2, 9]])
