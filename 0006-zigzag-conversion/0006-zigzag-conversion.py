class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if numRows == 1:
            return s
        
        zig_zag = [[] for _ in range(numRows)]

        index = 0
        direction = 1

        for i in range(len(s)):
            # turning point
            if index == 0:
                direction = 1
            #turning point
            elif index == numRows - 1:
                direction = -1
            
            zig_zag[index].append(s[i])

            index += direction

        return ''.join([''.join(_) for _ in zig_zag])
