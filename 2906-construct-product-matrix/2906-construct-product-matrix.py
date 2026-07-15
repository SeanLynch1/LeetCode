class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        
        MOD = 12345
        rows = len(grid)
        cols = len(grid[0])

        # Store product of each row
        row_products = [1] * rows

        for r in range(rows):
            for c in range(cols):
                row_products[r] *= grid[r][c]
                row_products[r] %= MOD

        # Prefix and suffix products of rows
        row_prefix = [1] * rows
        row_suffix = [1] * rows

        curr = 1
        for r in range(rows):
            row_prefix[r] = curr
            curr *= row_products[r]
            curr %= MOD

        curr = 1
        for r in range(rows - 1, -1, -1):
            row_suffix[r] = curr
            curr *= row_products[r]
            curr %= MOD

        # Build result with left products
        result = [[1] * cols for _ in range(rows)]

        for r in range(rows):
            curr = 1
            for c in range(cols):
                result[r][c] = curr
                curr *= grid[r][c]
                curr %= MOD

        # Multiply by right products and row products
        for r in range(rows):
            curr = 1

            # Product of all rows except current row
            other_rows = row_prefix[r] * row_suffix[r]
            other_rows %= MOD

            for c in range(cols - 1, -1, -1):
                # left * right
                result[r][c] *= curr
                result[r][c] %= MOD

                # multiply by all other rows
                result[r][c] *= other_rows
                result[r][c] %= MOD

                curr *= grid[r][c]
                curr %= MOD

        return result