class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        
        for row in matrix:
            print(row)

        rows = len(matrix)
        cols = len(matrix[0])

        count = 0
        # [0, 4, 5, 9]
        # {
        # 0: 1
        # 4: 1
        # 5: 2
        # 9: 1
        # }

        for top in range(rows):
            cols_sum = [0] * cols

            for bottom in range(top, rows):

                for col in range(cols):
                    cols_sum[col] += matrix[bottom][col]

                prefixes = defaultdict(int)
                prefixes[0] = 1
                curr = 0

                for val in cols_sum:
                    curr += val
                    needed = curr - target

                    count += prefixes[needed]

                    prefixes[curr] += 1
                    
        return count