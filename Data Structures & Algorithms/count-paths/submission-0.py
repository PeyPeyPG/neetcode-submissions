class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def uniquePathsHelper(i, j):
            if i > m or j > n:
                return 0
            elif i == (m-1) and j == (n-1):
                return 1
            else:
                return uniquePathsHelper(i+1, j) + uniquePathsHelper(i, j+1)
        return uniquePathsHelper(0, 0)