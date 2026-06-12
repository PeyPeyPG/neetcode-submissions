class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        sol = 0

        while l < r:
            sol = max(sol, (min(heights[l], heights[r]) * (r-l)))
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1     
        
        return sol