class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        
        # [1,1,3,2,4,3,2]
        # [1,1,3,2,4,3,2]
        # [1,1,3,2,4,3,2]

        # [0,0,0,0 ,0 , 0, 0, 0]
        # [0,1,2,5 ,6 ,11,14,15]
        # [0,2,4,10,14,22,28,32]
        # [0,3,6,15,21,33,42,48]

        # [10,10,10,10,10,10]
        # [10,10,10,10, 1, 1]
        # [10,10,10,10, 1, 1]

        # [0,  0,  0,  0,   0,   0,   0]
        # [0, 10, 20, 30,  40,  50,  60]
        # [0, 20, 40, 60,  80,  91, 102]
        # [0, 30, 60, 90, 120, 132, 144]

        res = 0

        rows = len(mat) + 1
        cols = len(mat[0]) + 1

        prefixes = [[0] * (cols) for _ in range(rows)]

        for row in range(1, rows):
            for col in range(1, cols): 
                prefixes[row][col] += mat[row-1][col-1]
                prefixes[row][col] += prefixes[row][col-1]
                prefixes[row][col] += prefixes[row - 1][col]
                prefixes[row][col] -= prefixes[row - 1][col-1]

        min_side = min(rows, cols)

        for i in range(min_side):
            side = i + 1
            for row in range(side, rows):
                for col in range(side, cols):
                    
                    total = (prefixes[row][col]
                            - prefixes[row][col-side]
                            - prefixes[row - side][col]
                            + prefixes[row - side][col - side]
                            )

                    if total <= threshold:
                        res = max(res, side)

        return res