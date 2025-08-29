class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        n = len(board[0])
        m = len(board)
    
        # modify cells in place
        for i in range(m):
            for j in range(n):
                # if i - 1 >= 0 check above
                # if i + 1 <= m - 1, check below

                # if j - 1 >= 0 check left
                # if j + 1 <= n - 1 check right

                # attempt to check all 8 neighbours, starting from top left neightbour

                live_neighbours = 0
                
                row_offset = -2
                col_offset = -1

                for check in range(0, 9):
                    if check % 3 != 0:
                        col_offset += 1
                    else:
                        col_offset = -1
                        row_offset += 1
                    
                    # check bounds
                    if i + row_offset < 0:
                        continue
                    elif i + row_offset > m - 1:
                        continue
                    
                    if j + col_offset < 0:
                        continue
                    elif j + col_offset > n - 1:
                        continue
                    
                    if row_offset == 0 and col_offset == 0:
                        continue

                    # if cell is alive
                    if board[i + row_offset][j + col_offset] % 2 == 1:
                        live_neighbours += 1

                # check four conditions after each neighbour has been assessed
                if board[i][j] == 1:
                    if live_neighbours >= 2 and live_neighbours <= 3:
                        board[i][j] += 2
                else:
                    if live_neighbours == 3:
                        board[i][j] += 2

        for i in range(m):
            for j in range(n):
                if board[i][j] > 1:
                    board[i][j] = 1
                else:
                    board[i][j] = 0

        return board
                
        