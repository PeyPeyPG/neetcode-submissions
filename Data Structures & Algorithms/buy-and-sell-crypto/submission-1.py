class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        sol = 0

        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
                r += 1
            else:
                profit = prices[r] - prices[l]
                sol = max(sol, profit)
                r += 1
        
        return sol