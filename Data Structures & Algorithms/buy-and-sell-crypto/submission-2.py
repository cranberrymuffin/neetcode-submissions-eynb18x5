class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        low = prices[0]

        for price in prices:
            low = min(price, low)
            maxProfit = max(maxProfit, price - low)
        
        return maxProfit
        