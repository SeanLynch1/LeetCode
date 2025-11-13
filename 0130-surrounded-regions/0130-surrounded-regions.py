class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        no_rows = len(board)
        no_cols = len(board[0])


        def helper(row: int, col: int) -> None:
            
            if (row < 0 or row == no_rows) or (col < 0 or col == no_cols) or board[row][col] != "O":
                return

            print("hello?")
            board[row][col] = "E"
            # down
            helper(row + 1, col)
            # left
            helper(row, col - 1)
            # right
            helper(row, col + 1)
            # up
            helper(row - 1, col)

            return

        # start at edge tiles
        for r in [0,no_rows-1]:
            for c in range(no_cols):
                print(board[r][c])
                if board[r][c] == "O":
                    print("Hi")
                    helper(r, c)

        for c in [0, no_cols - 1]:
            for r in range(no_rows):
                if board[r][c] == "O":
                    helper(r,c)
        for i in range(no_rows):
            print(board[i])

        for r in range(no_rows):
            for c in range(no_cols):
                if board[r][c] == "E":
                    board[r][c] = "O"
                elif board[r][c] == "O":
                    board[r][c] = "X"


                
