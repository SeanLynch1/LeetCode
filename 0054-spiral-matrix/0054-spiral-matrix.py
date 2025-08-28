class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        if not matrix:
            return matrix
        
        left = 0
        right = len(matrix[0]) - 1
        top = 0
        bottom = len(matrix) - 1

        res = []

        while left <= right and top <= bottom:

            for j in range(left, right + 1):
                res.append(matrix[top][j])
            top += 1

            print(res)

            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1

            print(res)

            if top <= bottom:
                for j in range(right, left - 1, -1):
                    res.append(matrix[bottom][j])
                bottom -= 1

            print(res)

            print("left = ", left)
            if left <= right:
                for i in range(bottom, top - 1, - 1):
                    print("i = ", i)
                    print(f"{matrix[i][left]}")
                    res.append(matrix[i][left])
                left += 1

            print(res)
            print("\n")

        return res
            
        