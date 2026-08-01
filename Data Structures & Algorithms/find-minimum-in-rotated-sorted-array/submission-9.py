class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        res = 9999999

        while l <= r:
            m = l + (r-l) // 2
            print(m)
            res = min(res,nums[m])
            if nums[l] > nums[r]:
                while nums[l] > nums[r]:
                    l += 1
            elif nums[l] > nums[m]:
                l = m + 1
            else:
                r = m - 1
        
        return res