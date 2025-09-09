class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if numRows <= 1:
            return s

        grid = [[] for _ in range(numRows)]

        d = 1
        index = 0

        for letter in s:
            
            if index == 0:
                d = 1
            elif index == numRows - 1:
                d = -1
            
            grid[index].append(letter)

            index += d

        return ''.join([''.join(g) for g in grid])