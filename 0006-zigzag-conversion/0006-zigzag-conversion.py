class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        n = len(s)
        s_grid = [[] for _ in range(numRows)]
        numRows -= 1
        output = []

        row = 0
        d = -1

        for i in range(n):
            
            if row == 0:
                d *= -1
            elif row == numRows:
                d *= -1
            s_grid[row].append(s[i])
            row += d
            
        for j in s_grid:
            output.append("".join(j))

        return "".join(output)  