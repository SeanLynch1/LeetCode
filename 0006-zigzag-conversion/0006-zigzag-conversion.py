class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
            
        index, d = 0, 1
        n = len(s)

        final_str = [[] for i in range(numRows)]

        for char in s:
            final_str[index].append(char)
            if index == 0:
                d = 1
            elif index == numRows -1:
                d = -1
            index += d

        return ''.join([''.join(final_str[i]) for i in range(numRows)])


       
