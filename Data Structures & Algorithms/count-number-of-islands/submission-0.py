class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0

        def dfs(r,c):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == "0"):
                return
            grid[r][c] = "0"
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for x in range(ROWS):
                for y in range(COLS):
                    if grid[x][y] == "1":
                        dfs(x, y)
                        islands += 1
        return islands
        