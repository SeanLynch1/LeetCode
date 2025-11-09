class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        no_rows = len(board)
        no_cols = len(board[0])

        # change all o's found to e
        def helper(row: int, col: int):
            if (row < 0 or row == no_rows) or (col < 0 or col == no_cols) or board[row][col] == "E" or board[row][col] == "X":
                return

            board[row][col] = "E"
            # check down
            helper(row + 1, col)
            # check left
            helper(row, col - 1)
            # check right
            helper(row, col + 1)
            # check up
            helper(row - 1, col)
            return

        # start from top and bottom row
        for r in [0, no_rows - 1]:
            for c in range(no_cols):
                if board[r][c] == "O":
                    helper(r, c)

        # start from left and right side
        for c in [0, no_cols - 1]:
            for r in range(no_rows):
                if board[r][c] == "O":
                    helper(r, c)

        for r in range(no_rows):
            for c in range(no_cols):
                if board[r][c] == "E":
                    board[r][c] = "O"
                elif board[r][c] == "O":
                    board[r][c] = "X"

