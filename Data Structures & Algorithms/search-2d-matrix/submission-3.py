class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for i in range(len(matrix)):
            l,r = 0, len(matrix[0])-1
            if matrix[i][r] < target:
                continue
            elif matrix[i][l] > target:
                continue
            else:
                while l <= r:
                    mid = l + ((r-l)//2)
                    if matrix[i][mid] == target:
                        return True
                    elif matrix[i][mid] < target:
                        l = mid + 1
                    else:
                        r = mid - 1
            
        return False