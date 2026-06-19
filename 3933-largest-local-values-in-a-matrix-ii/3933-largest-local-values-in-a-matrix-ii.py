class Solution:
    def countLocalMaximums(self, matrix: list[list[int]]) -> int:
        #[4,0,0,3]
        #[1,0,1,0]
        #[1,1,2,1]
        #[1,2,1,1]

        #rows & cols max for 2:
        #[0,0,0,0,0]
        #[0,1,1,1,2]
        #[0,1,1,1,2]
        #[0,1,1,1,2]
        #[0,1,1,1,2]

        count = 0
        rows = len(matrix)
        cols = len(matrix[0])

        prefixes = defaultdict(list)

        for arr in matrix:
            for val in arr:
                if val not in prefixes:
                    # make prefix for this val
                    grid = [[0] * (cols + 1) for r in range(rows + 1)]

                    for row in range(rows + 1):
                        for col in range(cols + 1):

                            if row == 0 or col == 0:
                                continue

                            left_box = grid[row][col - 1]
                            top_box = grid[row -1 ][col]
                            top_corner = grid[row - 1][col - 1]
                            next_val = matrix[row - 1][col - 1] > val

                            total = ((left_box + top_box) - (top_corner)) + (next_val)
                            grid[row][col] = total

                    prefixes[val] = grid
        
        for row in range(rows):
            for col in range(cols):
                
                val = matrix[row][col]
                if val > 0:
                    grid = prefixes[val]

                    bottom_right = grid[min(len(grid)-1,row + val + 1)][min(len(grid[0])-1,col + val + 1)]

                    top_left = grid[max(0, row - (val))][max(0, col - val)]

                    top_right = grid[max(0,row - val)][min(len(grid[0])-1,col + val + 1)]

                    bottom_left = grid[min(len(grid)-1,row + val + 1)][max(0,col - val)]

                    total = bottom_right + top_left - (top_right + bottom_left)

                    corners = [(-val,-val),(-val,val),(val,val),(val,-val)]

                    for v, h in corners:
                        if row + v >= 0 and row + v <= (rows -1):
                            if col + h >= 0 and col + h <= (cols - 1):
                                if matrix[row + v][col + h] > val:
                                    total -= 1

                    if total <= 0:
                        count += 1


        return count
