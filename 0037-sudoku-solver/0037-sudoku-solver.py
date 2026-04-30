class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])

        row_sets = [set() for _ in range(9)]
        col_sets = [set() for _ in range(9)]
        box_sets = [set() for _ in range(9)]

        for r in range(rows):
            print(board[r])   

        # begin by initializing sets
        for r in range(rows):
            for c in range(cols):
                if board[r][c] != ".":
                    row_sets[r].add(board[r][c])
                    col_sets[c].add(board[r][c])

                    box_sets[(r // 3) * 3 + (c // 3)].add(board[r][c])
        
        for r in range(len(row_sets)):
            print(f"row {r}: {row_sets[r]}")

        for c in range(len(col_sets)):
            print(f"col {c}: {col_sets[c]}")


        def dfs(r, c) -> bool:
            
            if r == 9:
                return True

            if c == 9:
                return dfs(r + 1, 0)
            
            val = board[r][c]

            if val == ".":
                for i in range(1, 10):
                    s = str(i)  
                    curr_box = (r // 3) * 3 + (c // 3)

                    if s not in row_sets[r] and s not in col_sets[c] and s not in box_sets[curr_box]:
                        board[r][c] = s
                        row_sets[r].add(s)
                        col_sets[c].add(s)
                        box_sets[curr_box].add(s)

                        if dfs(r, c + 1):
                            return True
                        else:
                            board[r][c] = "."
                            row_sets[r].remove(s)
                            col_sets[c].remove(s)
                            box_sets[curr_box].remove(s)
            else:
                return dfs(r, c + 1)

            return False

        dfs(0,0)

        for r in range(rows):
            print(board[r]) 


                















