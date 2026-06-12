class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        maxA = 0
        while i < j:
            maxA = max(maxA,(j - i) * min(heights[i], heights[j]))
            if heights[j] < heights[i]:
                j -= 1
            else:
                i += 1
        return maxA