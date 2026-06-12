class Solution:
    def del_island(self, grid, i, j):
        grid[i][j] = "0"
        if ((i - 1) >= 0) and grid[i-1][j] == "1":
            self.del_island(grid, i-1, j)
        if ((j - 1) >= 0) and grid[i][j-1] == "1":
            self.del_island(grid, i, j-1)
        if (i + 1) < len(grid) and grid[i+1][j] == "1":
            self.del_island(grid, i+1, j)
        if (j + 1) < len(grid[0]) and grid[i][j+1] == "1":
            self.del_island(grid, i, j+1)
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    count = count + 1
                    self.del_island(grid, i, j)
        return count
                    
        