class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lr, lc, hr, hc = 0, 0, len(matrix)-1, len(matrix[0])-1
        for row in matrix:
            if target in row:
                return True
        return False