class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        rows = len(board)
        cols = len(board[0])

        def search(x, y, idx) -> bool:
            
            if idx == len(word):
                return True

            if x < 0 or y < 0 or x >= rows or y >= cols:
                return False

            if board[x][y] != word[idx]:
                return False
            
            if (x, y) in self.visited:
                return False

            self.visited.add((x,y))

            # right
            if search(x, y + 1, idx + 1):
                return True

            # down
            if search(x + 1, y, idx + 1):
                return True

            # left
            if search(x, y - 1, idx + 1):
                return True

            # up
            if search(x - 1, y, idx + 1):
                return True

            self.visited.remove((x,y))

        for r in range(rows):
            for c in range(cols):
                self.visited = set()
                if search(r, c, 0):
                    return True
        
        return False