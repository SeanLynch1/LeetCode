class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return 0

            val = grid[r][c]
            grid[r][c] = 0  # mark visited

            best = 0
            for dr, dc in [(0,1),(1,0),(-1,0),(0,-1)]:
                best = max(best, dfs(r + dr, c + dc))

            grid[r][c] = val  # backtrack
            return val + best

        return max(dfs(r, c) for r in range(rows) for c in range(cols))