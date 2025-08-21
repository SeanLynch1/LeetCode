class Solution:
    def convert(self, s: str, numRows: int) -> str:
        res, direction, ind = [], 0 , 0

        grid = [[] for _ in range(numRows)]

        for char in s:
            if ind == 0:
                direction = 1
            elif ind == numRows - 1:
                direction = -1

            print(ind)
            grid[ind].append(char)
            ind += direction
        
        for i in range(len(grid)):
            res.append(''.join(grid[i]))

        return ''.join(res)