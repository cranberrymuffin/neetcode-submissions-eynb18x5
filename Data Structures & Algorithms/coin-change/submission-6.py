class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        ways = {}
        def findWays(change):
            total = sum(change)
            if total in ways:
                prev = ways[total]
                ways[total] = min(len(change), ways[total])
                if ways[total] == prev:
                    return
            else:
                ways[total] = len(change)
            if total == amount:
                return ways[total]
            if total > amount:
                return
            for coin in coins:
                change.append(coin)
                findWays(change)
                change.pop()
        findWays([])
        if amount in ways:
            return ways[amount]
        return -1