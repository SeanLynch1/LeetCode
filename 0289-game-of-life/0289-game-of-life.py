class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        n = len(board[0])
        m = len(board)

        directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    
        # modify cells in place
        for i in range(m):
            for j in range(n):
                # if i - 1 >= 0 check above
                # if i + 1 <= m - 1, check below

                # if j - 1 >= 0 check left
                # if j + 1 <= n - 1 check right

                # attempt to check all 8 neighbours, starting from top left neightbour

                live_neighbours = 0
                
                for x, y in directions:
                    # check bounds
                    if i + x < 0:
                        continue
                    elif i + x > m - 1:
                        continue
                    
                    if j + y < 0:
                        continue
                    elif j + y > n - 1:
                        continue
                    
                    # if cell is alive
                    if board[i + x][j + y] % 2 == 1:
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
                
        