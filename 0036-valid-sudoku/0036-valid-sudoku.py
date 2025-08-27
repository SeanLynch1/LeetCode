from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        cols = {}
        squares = {}
            
        offset = 0
        for i in range(len(board)):
            rows[i] = defaultdict(int)

            square_no = 0 + offset

            if square_no not in squares:
                squares[i] = defaultdict(int)

            for j in range(len(board[i])):
                if j not in cols:
                    cols[j] = defaultdict(int)

                # squares
                if board[i][j] != ".":
                    if board[i][j] not in squares[square_no]:
                        squares[square_no][board[i][j]] += 1
                    else:
                        return False

                if j < (len(board[i]) - 1) and (j + 1) % 3 == 0:
                    square_no += 1

                    if square_no not in squares:
                        squares[square_no] = defaultdict(int)
                    
                # rows and cols
                if board[i][j] != ".":
                    if board[i][j] not in rows[i]:
                        rows[i][board[i][j]] += 1
                    else:
                        return False

                    if board[i][j] not in cols[j]:
                        cols[j][board[i][j]] += 1
                    else:
                        return False

            if i > 0 and (i + 1) % 3 == 0:
                offset += 3

        return True