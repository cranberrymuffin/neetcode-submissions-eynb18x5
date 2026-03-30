class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        area = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    area = max(area, self.visit(row, col, grid))
        return area

    def visit(self, row: int, col: int, grid: List[List[int]]):
        if grid[row][col] != 1:
            return 0
        else:
            area = 1
            grid[row][col] = ""
            if row +1 < len(grid):
                area += self.visit(row + 1, col, grid)
            if row - 1 >=0:
                area += self.visit(row - 1, col, grid)
            if col + 1 < len(grid[0]):
                area += self.visit(row, col + 1, grid)
            if col - 1 >=0:
                area += self.visit(row, col - 1, grid)
        return area