class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        
        mapping = {}

        n = len(board)
        no_tiles = n * n
        tile = no_tiles
        toggle = (n % 2 == 0)

        for i in range(n):
            for j in range(n):

                if toggle:
                    if board[i][j] != -1:
                        mapping[tile] = board[i][j]
                    else:
                        mapping[tile] = -1
                else:
                    if board[i][n + 1 - j] != -1:
                        mapping[tile] = board[i][n + 1 - j]
                    else:
                        mapping[tile] = -1
                
                tile -= 1
            
            toggle = not toggle

        print(mapping)

        moves = 0


        return moves
