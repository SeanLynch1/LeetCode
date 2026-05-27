class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows = len(matrix)
        cols = len(matrix[0])
        self.prefixes = [[0] for _ in range(rows)]

        for row in range(rows):
            for col in range(cols):
                self.prefixes[row].append(self.prefixes[row][-1] + matrix[row][col])

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = 0

        for row in range(row1, row2 + 1):
            total += self.prefixes[row][col2 + 1] - self.prefixes[row][col1]
        
        return total

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)