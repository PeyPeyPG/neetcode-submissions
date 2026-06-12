class Solution:
    directions = [[1,0], [-1,0], [0,1], [0,-1]]
    def del_island(self, grid, i, j):
        if (i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == "0"):
            return
        grid[i][j] = "0"
        for dr, dc in self.directions:
            self.del_island(grid, i + dr, j + dc)
        # grid[i][j] = "0"
        # if ((i - 1) >= 0) and grid[i-1][j] == "1":
        #     self.del_island(grid, i-1, j)
        # if ((j - 1) >= 0) and grid[i][j-1] == "1":
        #     self.del_island(grid, i, j-1)
        # if (i + 1) < len(grid) and grid[i+1][j] == "1":
        #     self.del_island(grid, i+1, j)
        # if (j + 1) < len(grid[0]) and grid[i][j+1] == "1":
        #     self.del_island(grid, i, j+1)
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    count = count + 1
                    self.del_island(grid, i, j)
        return count     