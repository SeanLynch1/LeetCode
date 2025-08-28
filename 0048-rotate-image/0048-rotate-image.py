class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # transpose
        n = len(matrix)
        i = 0
        j = 0

        for i in range(n):
            for j in range(i, n):
                var_1 = matrix[i][j]
                var_2 = matrix[j][i]

                matrix[i][j] = var_2
                matrix[j][i] = var_1

        for i in range(n):
            print(matrix[i])

        print("\n")
        # reverse rows
        # [1, 4, 7] -> [7, 4, 1]
        
        
        for i in range(n):
            left = 0
            right = n - 1
            while left < right:
                val_1 = matrix[i][left]
                val_2 = matrix[i][right]

                matrix[i][left] = val_2
                matrix[i][right] = val_1

                left += 1
                right -= 1

        for i in range(n):
            print(matrix[i])




        return matrix
            