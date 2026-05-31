class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        # bisect_left -> gives you the index of the first value that is >= the given value
        # bisect_right -> gives you the index of the first value that is > the given value
        max_val = float('-inf')

        rows = len(matrix)
        cols = len(matrix[0])

        # k = -4
        # [2, -8, -4, 3, -5]

        # [-10, -6, 0, 2]
        
        for row in matrix:
            print(row)

        for top in range(rows):

            cols_sum = [0] * cols
            for row in range(top, rows):
                # populate cols_sum
                for col in range(cols):
                    cols_sum[col] += matrix[row][col]

                prefixes = [0]
                curr = 0

                for val in cols_sum:
                    curr += val
                    
                    idx = bisect_left(prefixes, curr - k)

                    if idx < len(prefixes):
                       idx_num = prefixes[idx]
                       max_val = max(max_val, curr - idx_num)
                       if max_val == k:
                            return k

                    insort(prefixes, curr)

        return max_val