class Solution:
    memo = {}
    def climbStairs(self, n: int) -> int:
        if n == 0:
            self.memo[n] = 1
            return 1
        elif n < 0:
            self.memo[n] = 0
            return 0
        if n in self.memo:
            return self.memo[n]
        else:
            self.memo[n] = self.climbStairs(n - 2) + self.climbStairs(n - 1)
            return self.memo[n]
        