class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])

        # dfs board
        def dfs(x: int, y : int) -> None:
            # changes e's to o's, change o's to x's
            if board[x][y] == "O":
                board[x][y] = "E"
            else:
                return

            # check up
            if x - 1 >= 0:
                dfs(x - 1, y)

            # check left
            if y - 1 >= 0:
                dfs(x, y - 1)

            # check right
            if y + 1 < cols:
                dfs(x, y + 1)

            # check down
            if x + 1 < rows:
                dfs(x + 1, y)

            return

        # traverse top and bottom sides
        for r in [0, rows - 1]:
            for c in range(cols):
                if board[r][c] == "O":
                    dfs(r, c)

        # traverse left and right sides
        for c in [0, cols - 1]:
            for r in range(rows):
                if board[r][c] == "O":
                    dfs(r,c)

        # update board
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "E":
                    board[r][c] = "O"