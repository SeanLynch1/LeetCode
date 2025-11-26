class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        no_rows = len(grid)
        no_cols = len(grid[0])
        islands = 0

        def helper(row, col):
            if (row < 0 or row == no_rows) or (col < 0 or col == no_cols) or grid[row][col] == "0":
                return
            
            grid[row][col] = "0"

            # explore all directions
            #down
            helper(row + 1, col)

            # left
            helper(row, col - 1)

            # right
            helper(row, col + 1)

            # up
            helper(row - 1, col)

            return

        for r in range(no_rows):
            for c in range(no_cols):
                if grid[r][c] != "0":
                    helper(r, c)

                    islands += 1

        return islands