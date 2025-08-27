from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)
            
        offset = 0
        for i in range(len(board)):
            square_no = 0 + offset

            for j in range(len(board[i])):
                # squares
                if board[i][j] != ".":
                    if board[i][j] not in squares[square_no]:
                        squares[square_no].add(board[i][j])
                    else:
                        return False

                if j < (len(board[i]) - 1) and (j + 1) % 3 == 0:
                    square_no += 1

                # rows and cols
                if board[i][j] != ".":
                    if board[i][j] not in rows[i]:
                        rows[i].add(board[i][j])
                    else:
                        return False

                    if board[i][j] not in cols[j]:
                        cols[j].add(board[i][j])
                    else:
                        return False

            if i > 0 and (i + 1) % 3 == 0:
                offset += 3

        return True