class Solution:
    def visitIsland(self, grid: List[List[int]], row: int, col: int) -> int:
        if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] == 0:
            return 0
        else:
            grid[row][col] = 0
            return 1 + self.visitIsland(grid, row + 1, col) + self.visitIsland(grid, row -1, col) + self.visitIsland(grid, row, col + 1) + self.visitIsland(grid, row, col - 1)
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxIsland = 0

        for row, _ in enumerate(grid):
            for col, _ in enumerate(grid[row]):
                if grid[row][col] == 1:
                    maxIsland = max(maxIsland, self.visitIsland(grid, row, col))

        return maxIsland
        