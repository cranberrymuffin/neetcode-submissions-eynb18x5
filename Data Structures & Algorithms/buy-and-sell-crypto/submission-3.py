class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = max(prices)
        maxProfix = 0
        for price in prices:
            low = min(price, low)
            maxProfix = max(maxProfix, price - low)
        return maxProfix

        