class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0

        for num in s:
            temp = num
            count = 0
            while temp in s:
                count += 1
                temp -= 1
            
            res = max(res, count)
        
        return res
