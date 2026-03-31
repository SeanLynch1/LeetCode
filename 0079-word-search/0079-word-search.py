class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def dfs(r, c, i):
            if i == len(word):
                return True

            if r < 0 or c < 0 or r >= rows or c >= cols:
                return False

            if board[r][c] != word[i]:
                return False

            # mark visited
            temp = board[r][c]
            board[r][c] = "#"

            directions = [(0,1), (1,0), (0,-1), (-1,0)]
            for dr, dc in directions:
                if dfs(r + dr, c + dc, i + 1):
                    board[r][c] = temp
                    return True

            board[r][c] = temp
            return False

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True

        return False