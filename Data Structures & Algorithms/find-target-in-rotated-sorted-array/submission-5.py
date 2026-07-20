class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l <= r:
            m = l + (r - l) // 2

            if nums[m] == target:
                return m

            if nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]:
                    # target is inside the left side
                    r = m - 1
                else:
                    # target must be on the right side
                    l = m + 1
            else:
                if nums[m] < target <= nums[r]:
                    # target is inside the right side
                    l = m + 1
                else:
                    # target must be on the left side
                    r = m - 1
        
        return -1