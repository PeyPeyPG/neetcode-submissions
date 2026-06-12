class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        best_k = max(piles)
        while l <= r:
            mid = (l+r) // 2
            
            total = 0

            for pile in piles:
                total += math.ceil(pile / mid)
            
            if total <= h:
                r = mid - 1
                best_k = min(best_k, mid)
            else:
                l = mid + 1
        
        return best_k