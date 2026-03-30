class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if (len(stones) == 1):
            return stones[0]
        if (len(stones) == 0):
            return 0
        
        x = max(stones)
        stones.remove(x)
        y = max(stones)
        if x == y:
            stones.remove(y)
        if x < y:
            stones[stones.index(y)] = y - x
        if x > y:
            stones[stones.index(y)] = x - y
        
        return self.lastStoneWeight(stones)

        