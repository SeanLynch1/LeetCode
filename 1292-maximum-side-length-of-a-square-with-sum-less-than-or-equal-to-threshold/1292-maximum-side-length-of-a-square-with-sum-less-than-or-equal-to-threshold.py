class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        
        # if a 3 x 3 square passes, then any smaller square will pass too... binary search
         
        rows = len(mat) + 1
        cols = len(mat[0]) + 1

        prefixes = [[0] * cols for _ in range(rows)]

        # [[1,1,3,2,4,3,2],
        #  [1,1,3,2,4,3,2],
        #  [1,1,3,2,4,3,2]]

        #[[10,10,10,10,10,10], 
        # [10,10,10,10, 1, 1], 
        # [10,10,10,10, 1, 1]]

        for row in range(1, rows):
            for col in range(1, cols):
                prefixes[row][col] = (
                    prefixes[row][col-1] +
                    prefixes[row - 1][col] +
                    mat[row-1][col-1] -
                    prefixes[row - 1][col - 1]
                )

        def can_make(side):

            for row in range(side, rows):
                for col in range(side, cols):

                    total = (
                        prefixes[row][col] -
                        prefixes[row - side][col] -
                        prefixes[row][col - side]
                        + prefixes[row - side][col - side]
                    )

                    if total <= threshold:
                        return True

            return False

        min_side = min(rows, cols)

        left = 0
        right = min_side

        while left <= right:

            mid = (left + right) // 2

            if can_make(mid):
                left = mid + 1
            else:
                right = mid - 1

        return right



