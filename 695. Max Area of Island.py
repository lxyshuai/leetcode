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


class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        max_area = 0
        rows = len(grid)
        columns = len(grid[0]) if rows else 0
        has_visited = [[False for _ in range(columns)] for _ in range(rows)]
        for row in range(rows):
            for column in range(columns):
                # 如果该点访问过,跳过
                if has_visited[row][column]:
                    continue
                if grid[row][column] == 1:
                    area = self.visit(grid, has_visited, rows, columns, row,
                                      column)
                    max_area = max(max_area, area)
        return max_area

    def visit(self, grid, has_visited, rows, columns, row, column):
        # bfs
        visited = set()
        queue = list()
        visited.add((row, column))
        queue.append((row, column))
        has_visited[row][column] = True
        area = 0
        while queue:
            current_row, current_column = queue.pop(0)
            area += 1
            for next_row, next_column in ((current_row - 1, current_column),
                                          (current_row + 1, current_column),
                                          (current_row, current_column + 1),
                                          (current_row, current_column - 1)):
                if 0 <= next_row < rows and 0 <= next_column < columns and \
                        grid[next_row][next_column] == 1 and \
                        has_visited[next_row][next_column] == False:
                    has_visited[next_row][next_column] = True
                    queue.append((next_row, next_column))
        return area


if __name__ == '__main__':
    print Solution().maxAreaOfIsland([[1, 1, 0, 0, 0],
                                      [1, 1, 0, 0, 0],
                                      [0, 0, 0, 1, 1],
                                      [0, 0, 0, 1, 1]])
