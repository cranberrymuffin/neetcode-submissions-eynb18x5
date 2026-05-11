class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        seen = {}

        def countPaths(r: int, c: int) -> int:
            if r == m - 1 and c == n - 1:
                return 1
            if r < 0 or c < 0 or r >= m or c >= n:
                return 0
            if (r, c) in seen:
                return seen[(r, c)]
            seen[(r,c)] = countPaths(r + 1, c) + countPaths(r, c+1)
            return seen[(r,c)]
            
        return countPaths(0, 0)

        