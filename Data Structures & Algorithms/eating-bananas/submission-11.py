class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k = max(piles)
        l, r = 1, k

        while l <= r:
            m = (l + r) // 2

            hours = 0
            for pile in piles:
                hours += math.ceil(pile/m)
            
            if hours <= h:
                k = min(k, m)
                r = m - 1
            else:
                l = m + 1
        
        return k
