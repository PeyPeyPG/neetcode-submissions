class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = [height[0]]

        for i in range(1,len(height)):
            maxLeft.append(max(maxLeft[i-1],height[i]))
        
        maxRight = [height[-1]]

        for i in range(len(height)-2, -1, -1):
            maxRight.append(max(maxRight[-1], height[i]))

        maxRight.reverse()

        res = 0

        for i in range(len(height)):
            area = min(maxLeft[i], maxRight[i]) - height[i]
            if area > 0:
                res += area
        
        return res