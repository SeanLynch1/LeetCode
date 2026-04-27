class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        visited = set()

        gold = 0

        def dfs(row: int, col: int) -> int:
            
            if (row, col) in visited:
                return 0

            if row < 0 or row >= rows or col < 0 or col >= cols:
                return 0

            if grid[row][col] == 0:
                return 0

            visited.add((row, col))

            val = grid[row][col]
            best = 0

            dir = ((0,1),(1,0), (-1,0), (0,-1))
            
            for r, c in dir:
                best = max(dfs(row + r, col + c), best)
            
            val += best
            visited.remove((row, col))
            
            return val

        for r in range(rows):
            for c in range(cols):
                # start points
                gold = max(gold, dfs(r, c))

        return gold