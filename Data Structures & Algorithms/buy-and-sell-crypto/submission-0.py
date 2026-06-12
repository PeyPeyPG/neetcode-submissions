class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prof = 0
        mini = prices[0]
        for price in prices:
            if price < mini:
                mini = price
            if price - mini > prof:
                prof = price - mini
        return prof