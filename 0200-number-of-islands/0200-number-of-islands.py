class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        islands = 0
        rows = len(grid)
        cols = len(grid[0])

        directions = [(-1,0), (1, 0), (0,-1), (0,1)]
        def dfs(x , y) -> None:

            if grid[x][y] != "1":
                return

            grid[x][y] = "#"

            for nx, ny in directions:
                if x + nx >= 0 and x + nx < rows and y + ny >= 0 and y + ny < cols:
                    dfs(x + nx, y + ny)

            return

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    dfs(r,c)
                    islands += 1

        return islands