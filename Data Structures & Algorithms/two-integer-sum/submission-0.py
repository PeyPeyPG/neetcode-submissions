class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for i in range(len(nums)):
            n = target - nums[i]
            if n in m:
                return [m[n], i]
            else:
                m.update({nums[i] : i})
        return -1