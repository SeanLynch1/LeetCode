class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        row_sets = [set() for _ in range(9)]
        col_sets = [set() for _ in range(9)]
        box_sets = [set() for _ in range(9)]

        empties = []

        # initialize + collect empty cells
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    empties.append((r, c))
                else:
                    val = board[r][c]
                    row_sets[r].add(val)
                    col_sets[c].add(val)
                    box_sets[(r // 3) * 3 + (c // 3)].add(val)

        def dfs(i: int) -> bool:
            # base case: all empties filled
            if i == len(empties):
                return True

            r, c = empties[i]
            box = (r // 3) * 3 + (c // 3)

            for num in range(1, 10):
                s = str(num)

                if (
                    s not in row_sets[r]
                    and s not in col_sets[c]
                    and s not in box_sets[box]
                ):
                    board[r][c] = s
                    row_sets[r].add(s)
                    col_sets[c].add(s)
                    box_sets[box].add(s)

                    if dfs(i + 1):
                        return True

                    # backtrack
                    board[r][c] = "."
                    row_sets[r].remove(s)
                    col_sets[c].remove(s)
                    box_sets[box].remove(s)

            return False

        dfs(0)