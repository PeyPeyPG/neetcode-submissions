class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        se = set()

        l,r = 0,0
        m = 0

        while r < len(s):
            while s[r] in se:
                se.remove(s[l])
                l += 1 
                
            se.add(s[r])
            m = max(m,r-l+1)
            r += 1
        
        return m