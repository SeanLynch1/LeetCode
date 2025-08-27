from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[i])):
                square_no = (i // 3) * 3 + (j // 3)

                # squares
                if board[i][j] != ".":
                    continue

                if board[i][j] not in squares[square_no]:
                    squares[square_no].add(board[i][j])
                else:
                    return False

                # rows and cols
                if board[i][j] not in rows[i]:
                    rows[i].add(board[i][j])
                else:
                    return False

                if board[i][j] not in cols[j]:
                    cols[j].add(board[i][j])
                else:
                    return False

        return True