class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # recursion baby let's go

        islands = 0
        num_rows = len(grid)
        num_cols = len(grid[0])
        
        def helper(row: int, col: int) -> bool:
            
            if (row >= num_rows or row < 0) or (col >= num_cols or col < 0) or grid[row][col] == '0':
                # represents water...
                return 
            
            grid[row][col] = '0'
            
            # check left
            helper(row, col - 1)
            # check up
            helper(row - 1, col)
            # check right
            helper(row, col + 1)
            # check down
            helper(row + 1, col)

        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] == '1':
                    # obilterate island
                    helper(row, col)
                    islands += 1

        return islands