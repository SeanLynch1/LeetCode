class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        islands = 0

        no_rows = len(grid)
        no_cols = len(grid[0])

        def helper(x: int, y: int):

            if x < 0 or x == no_rows or y < 0 or y == no_cols or grid[x][y] == "0":
                return

            # down
            helper(x + 1, y)
            grid[x][y] = "0"
            # left
            helper(x, y - 1)
            # right
            helper(x, y + 1)
            # up
            helper(x - 1, y)

        for r in range(no_rows):
            for c in range(no_cols):
                if grid[r][c] == "1":
                    helper(r,c)
                    islands += 1

        return islands