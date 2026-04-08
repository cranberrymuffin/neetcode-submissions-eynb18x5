class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = max(prices)
        result = 0
        for price in prices:
            low = min(price, low)
            result = max(result, price - low)
        return result

        