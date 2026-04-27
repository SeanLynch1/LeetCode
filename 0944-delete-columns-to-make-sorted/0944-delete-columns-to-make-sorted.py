class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        
        rows = len(strs)
        total = 0
        grid = [[] for _ in strs]

        for i in range(len(strs)):
            for j in range(len(strs[i])):
                grid[i].append(strs[i][j])

        def dfs(row: int, col: int, last: str) -> bool:
            if row >= rows:
                return True

            if grid[row][col] < last:
                return False

            if dfs(row + 1, col, grid[row][col]):
                return True
            
            return False

        for i in range(len(strs[0])):
            # search down the col
            if not dfs(1, i, strs[0][i]):
                total += 1

        return total