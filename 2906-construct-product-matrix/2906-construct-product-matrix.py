class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        
        rows = len(grid)
        cols = len(grid[0])

        row_prefix = [1] * (rows)
        row_suffix = [1] * (rows)
        prefixes = [[1] * (cols) for row in range(rows)]

        curr = 1
        for row in range(rows):
            row_prefix[row] = curr

            pre_curr = 1
            for col in range(cols):
                prefixes[row][col] = pre_curr
                pre_curr *= grid[row][col]
                pre_curr %= 12345

                curr *= grid[row][col]
                curr %= 12345
        
        curr = 1
        for row in range(rows-1,-1,-1):
            row_suffix[row] = curr

            for col in range(cols):
                curr *= grid[row][col]
                curr %= 12345

        for row in range(rows):
            suffixes = 1
            for col in range(cols-1,-1,-1):
                total = prefixes[row][col] * suffixes
                total %= 12345

                total *= row_prefix[row]
                total %= 12345

                total *= row_suffix[row]
                total %= 12345

                suffixes *= grid[row][col]
                suffixes %= 12345

                grid[row][col] = total % 12345
            
        return grid