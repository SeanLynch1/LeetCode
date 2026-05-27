class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows = len(matrix)
        cols = len(matrix[0])
        self.prefixes = [[0] * (cols + 1) for _ in range(rows + 1)]

        for row in range(rows):
            for col in range(cols):
                total = 0
                total += matrix[row][col]
                total += self.prefixes[row + 1][col]
                total += self.prefixes[row][col + 1]
                total -= self.prefixes[row][col]

                self.prefixes[row + 1][col + 1] = total

        for row in self.prefixes:
            print(row)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        
        total = 0

        total += self.prefixes[row2 + 1][col2 + 1]
        total -= self.prefixes[row2 + 1][col1]
        total -= self.prefixes[row1][col2 + 1]
        total += self.prefixes[row1][col1]
        print(f"total = {total}")
        print("")
        return total

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

'''[0, 0, 0, 0, 0, 0]
[0, 3, 3, 4, 8, 10]
[0, 8, 14, 18, 24, 27]
[0, 9, 17, 21, 28, 36]
[0, 13, 22, 26, 34, 49]
[0, 14, 23, 30, 38, 58]'''