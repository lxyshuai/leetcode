# coding=utf-8
"""
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

Example 1:

[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
Example 2:

[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.
Note: The length of each dimension in the given grid does not exceed 50.
"""


import collections
class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def visit(row, column):
            area = 0
            queue = collections.deque([(row, column)])
            has_visited[row][column] = True
            while queue:
                current_row, current_column = queue.popleft()
                area += 1
                for next_row, next_column in ((current_row - 1, current_column),
                                              (current_row + 1, current_column),
                                              (current_row, current_column + 1),
                                              (current_row, current_column - 1)):
                    if rows > next_row >= 0 and columns > next_column >= 0 and grid[next_row][next_column] == 1 and has_visited[next_row][next_column] is False:
                        queue.append((next_row, next_column))
                        has_visited[next_row][next_column] = True
            return area
        rows = len(grid)
        columns = len(grid[0]) if rows else 0
        has_visited = [[False for _ in range(columns)] for _ in range(rows)]
        max_area = 0
        for row in range(rows):
            for column in range(columns):
                if has_visited[row][column] == True:
                    continue
                if grid[row][column] == 1:
                    max_area = max(max_area, visit(row, column))
        return max_area


if __name__ == '__main__':
    print Solution().maxAreaOfIsland([[1, 1, 0, 0, 0],
                                      [1, 1, 0, 0, 0],
                                      [0, 0, 0, 1, 1],
                                      [0, 0, 0, 1, 1]])
