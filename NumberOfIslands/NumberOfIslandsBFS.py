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


The following algorithm is a BFS traversal through the n x m grid.
"""
from collections import deque
class Solution(object):
    def NumberofIslands(self, grid):
        if grid is None: # if grid is empty, there are no islands
            return 0

        visited = set()  # create a set to add islands that we already visited
        rows = len(grid)  # length of row
        cols = len(grid[0])  # length of columns
        islands = 0  # initialize islands to 0

        def BFS(r, c):
            q = deque()  # initialize q
            visited.add((r, c))  # add coordinates to visited, so we do not count them twice
            q.append((r, c))  # add row and column indices to q

            while q:
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]  # we need to check UP, DOWN, RIGHT, LEFT  respectively
                for dr, dc in directions:
                    row, col = q.popleft()
                    nr, nc = r + dr, c + dc
                    # If new directions are in scope of our grid (they don't exceed length of row and column)
                    # Check to see if new coordinates are in visited and if the value at new coordinates is "1"
                    if 0 < nr < row and 0 < nc < col and (nr, nc) not in visited and grid[nr][nc] == "1":
                        visited.add((nr, nc))
                        q.append((nr, nc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    islands += 1
                    BFS(r, c)
        return islands

