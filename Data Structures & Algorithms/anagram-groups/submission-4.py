class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        
        for s in strs:
            arr = [0] * 26
            for c in s:
                arr[ord(c) - ord('a')] += 1

            arr = tuple(arr)
            if arr not in dic:
                dic[arr] = []
            
            dic[arr].append(s)

        return list(dic.values())