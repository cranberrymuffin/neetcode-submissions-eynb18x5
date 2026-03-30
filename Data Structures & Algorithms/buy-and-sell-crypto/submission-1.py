class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minVal = float('inf')
        for price in prices:
            minVal = min(price, minVal)
            profit = max(profit, price - minVal)

        return int(profit)
        