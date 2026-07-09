class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        front = []
        back = []

        product = 1

        for num in nums:
            product = product * num
            front.append(product)
        
        product = 1

        for num in reversed(nums):
            product = product * num
            back.insert(0, product)
        
        res = []

        for i in range(len(nums)):
            if i == 0:
                res.append(back[i+1])
            elif i == (len(nums)-1):
                res.append(front[len(nums)-2])
            else:
                res.append(front[i-1] * back[i+1])
            
        return res