class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            stack.append((i, temp))
            while len(stack) >= 2 and stack[-1][1] > stack[-2][1]:
                res[stack[-2][0]] = i - stack[-2][0]
                stack.pop(-2)
        
        return res