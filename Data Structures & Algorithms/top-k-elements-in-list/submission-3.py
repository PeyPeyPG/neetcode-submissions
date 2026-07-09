class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}

        for num in nums:
            dic[num] = dic.get(num, 0) + 1
        
        dic = dict(sorted(dic.items(), key=lambda item: item[1], reverse=True))

        sol = []

        for index, (key, value) in enumerate(dic.items()):
            if index >= k:
                break
            sol.append(key)
        
        return sol