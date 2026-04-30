class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row_sets = [set() for _ in range(9)]
        col_sets = [set() for _ in range(9)]
        box_sets = [set() for _ in range(9)]

        # begin by initializing sets
        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    val = board[r][c]
                    row_sets[r].add(val)
                    col_sets[c].add(val)
                    box_sets[(r // 3) * 3 + (c // 3)].add(val)
        
        def dfs(r, c) -> bool:
            if r == 9:
                return True

            if c == 9:
                return dfs(r + 1, 0)
            
            
            if board[r][c] == ".":
                curr_box = (r // 3) * 3 + (c // 3)

                for i in range(1, 10):
                    s = str(i)  

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