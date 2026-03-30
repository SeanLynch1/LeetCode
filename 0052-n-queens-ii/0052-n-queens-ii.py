class Solution:
    def totalNQueens(self, n: int) -> int:
        
        self.output = 0
        markings = [[0 for _ in range(n)] for _ in range(n)]

        def back_track(col) -> None:

            if col == n:
                self.output += 1
                # reset the column
                return

            for i in range(n):
                
                if markings[i][col] == 0:
                    # update the row
                    for c in range(col, len(markings[i])):
                        markings[i][c] += 1
                    
                    r = i + 1
                    c = col + 1

                    while (r >= 0 and c >= 0) and (r < n and c < n):
                        markings[r][c] += 1
                        r += 1
                        c += 1

                    r = i - 1
                    c = col + 1

                    while (r >= 0 and c >= 0) and (r < n and c < n):
                        markings[r][c] += 1
                        r -= 1
                        c += 1
                    
                    back_track(col + 1)

                    # update the row
                    for c in range(col, len(markings[i])):
                        markings[i][c] -= 1

                    r = i + 1
                    c = col + 1

                    while (r >= 0 and c >= 0) and (r < n and c < n):
                        markings[r][c] -= 1
                        r += 1
                        c += 1

                    r = i - 1
                    c = col + 1

                    while (r >= 0 and c >= 0) and (r < n and c < n):
                        markings[r][c] -= 1
                        r -= 1
                        c += 1

        back_track(0)

        return self.output
