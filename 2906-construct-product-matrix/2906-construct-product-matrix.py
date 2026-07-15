class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        
        rows = len(grid)
        cols = len(grid[0])

        row_prefix = [1] * (rows)
        row_suffix = [1] * (rows)
        prefixes = [[1] * (cols) for row in range(rows)]

        curr = 1
        for row in range(rows):
            row_prefix[row] = curr * row_prefix[row]

            pre_curr = 1
            for col in range(cols):
                prefixes[row][col] = pre_curr
                pre_curr *= grid[row][col]
                pre_curr %= 12345

                curr *= grid[row][col]
                curr %= 12345
        
        curr = 1
        for row in range(rows-1,-1,-1):
            row_suffix[row] = curr * row_suffix[row]

            for col in range(cols):
                curr *= grid[row][col]
                curr %= 12345

        for row in range(rows):
            suffixes = 1
            for col in range(cols-1,-1,-1):
                total = prefixes[row][col] * suffixes

                total *= row_prefix[row]

                total *= row_suffix[row]

                suffixes *= grid[row][col]

                grid[row][col] = total % 12345
            
        return grid