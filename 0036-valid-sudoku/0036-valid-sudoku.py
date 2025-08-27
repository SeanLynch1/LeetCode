from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)
        
        for i in range(len(board)):
            for j in range(len(board[i])):

                val = board[i][j]
                # squares
                if val == ".":
                    continue

                square_no = (i // 3) * 3 + (j // 3)

                if val in squares[square_no] or val in rows[i] or val in cols[j]:
                    return False

                rows[i].add(val)
                cols[j].add(val)
                squares[square_no].add(val)

        return True