class Solution:



    def numIslands(self, grid: List[List[str]]) -> int:
        def visitIsland(row: int, col: int):
            if row >=0 and col >=0 and row < len(grid) and col <len(grid[0]) and grid[row][col] == '1':
                grid[row][col]= '0';
                visitIsland(row - 1, col)
                visitIsland(row + 1, col)
                visitIsland(row, col - 1)
                visitIsland(row, col + 1)

        num_island = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    num_island += 1
                    visitIsland(r, c)

        return num_island
        

        