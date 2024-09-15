"""
Given an m x n 2D binary grid, grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1


The following algorithm is a DFS traversal through the n x m grid using stack frame.
"""

class Solution(object):
    def numIslands(self, grid):
        count = 0  # counts number of islands

        # iterate through grid and check call DFS function when "1" is encountered
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    count += 1  # increment islands
                    self.BFS(grid, i, j)
        return count

    def BFS(self, grid, i, j):
        if (i < 0) or (i >= len(grid)) or (j < 0) or (j >= len(grid[i])) or (grid[i][j] == "0"):
            return
        grid[i][j] = "0"  # we turn coordinate to 0, so we don't end in a continuous loop of calling DFS function
        self.BFS(grid, i + 1, j)  # Check UP
        self.BFS(grid, i - 1, j)  # Check Down
        self.BFS(grid, i, j + 1)  # Check Right
        self.BFS(grid, i, j - 1)  # Check Left

