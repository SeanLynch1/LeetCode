class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # rows
        m = len(matrix)

        # cols
        n = len(matrix[0])

        # if we find a zero, store a zero at the first index of its row and column
        fill_top = False
        fill_left = False

        for j in range(n):
            if matrix[0][j] == 0:
                fill_top = True
                break

        for i in range(m):
            if matrix[i][0] == 0:
                fill_left = True
                break

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        bottom = m - 1
        right = n - 1

        if bottom >= 1 and right >= 1:
            while bottom > 0 or right > 0:

                if bottom < 1:
                    bottom = 1

                if right < 1:
                    right = 1

                # across
                if matrix[0][right] == 0:
                    for i in range(m):
                        matrix[i][right] = 0

                if matrix[bottom][0] == 0:
                    for j in range(n):
                        matrix[bottom][j] = 0
                
                bottom -= 1
                right -= 1
        

        if fill_top:
            for j in range(n):
                matrix[0][j] = 0

        if fill_left:
            for i in range(m):
                matrix[i][0] = 0

        return matrix