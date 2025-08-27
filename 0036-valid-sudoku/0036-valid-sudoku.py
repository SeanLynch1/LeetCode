from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        cols = {}
        squares = {}

        for i in range(len(board)):
            if i % 3 == 0:
                print("------" + ("--" * len(board)))

            for j in range(len(board[i])):
                if j % 3 == 0:
                    print("|", end = " ")
                print(board[i][j], end = " ")
                
            print(end = "\n")

            
        print("\n")
        offset = 0
        squares[0] = defaultdict(int)
        for i in range(len(board)):
            rows[i] = defaultdict(int)

            square_no = 0 + offset
            print("squares = ", squares)
            for j in range(len(board[i])):
                if j not in cols:
                    cols[j] = defaultdict(int)

                # squares
                if board[i][j] != ".":
                    if board[i][j] not in squares[square_no]:
                        print(f"adding {board[i][j]} to square {square_no}")
                        squares[square_no][board[i][j]] += 1
                        print("square = ", squares[square_no])
                    else:
                        print("false square")
                        print(f"square_no = {square_no}, squares = {squares[square_no]}")
                        return False

                if j < (len(board[i]) - 1) and (j + 1) % 3 == 0:
                    square_no += 1

                    if square_no not in squares:
                        print("adding/ reseting square!")
                        squares[square_no] = defaultdict(int)
                    
                    print("sqaures = ", squares)
                    print("\n")
                
                # rows and cols
                if board[i][j] != ".":
                    if board[i][j] not in rows[i]:
                        rows[i][board[i][j]] += 1
                    else:
                        print("false for rows!")
                        return False

                    if board[i][j] not in cols[j]:
                        cols[j][board[i][j]] += 1
                    else:
                        print("false for cols!")
                        return False

            if i > 0 and (i + 1) % 3 == 0:
                offset += 3

                    


        print("rows = ")
        for i in range(len(board)):
            print(rows[i])

        print("\n")
        print("cols = ")
        for i in range(len(board)):
            print(cols[i])

        print("\n")
        print("squares = ")
        for i in range(len(board)):
            print(squares[i])

        return True