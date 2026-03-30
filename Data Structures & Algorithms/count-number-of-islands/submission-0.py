class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_islands = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if(grid[row][col] == "1"):
                    num_islands += 1
                    self.visit(row, col, grid)
        return num_islands

    def visit(self, row: int, col: int, grid: List[List[str]]):
        if grid[row][col] != "1":
            return
        else:
            grid[row][col] = ""
            if row +1 < len(grid):
                self.visit(row + 1, col, grid)
            if row - 1 >=0:
                self.visit(row - 1, col, grid)
            if col +1 < len(grid[0]):
                self.visit(row, col + 1, grid)
            if col - 1 >=0:
                self.visit(row, col - 1, grid)