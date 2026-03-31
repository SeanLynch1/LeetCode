class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        self.output = False

        rows = len(board)
        cols = len(board[0])

        def search(x, y, idx):
            
            if idx == len(word):
                self.output = True
                return

            if x < 0 or y < 0 or x >= rows or y >= cols:
                return

            if board[x][y] != word[idx]:
                return
            
            if (x, y) in self.visited:
                return

            self.visited.add((x,y))

            # right
            search(x, y + 1, idx + 1)

            # down
            search(x + 1, y, idx + 1)

            # left
            search(x, y - 1, idx + 1)

            # up
            search(x - 1, y, idx + 1)

            self.visited.remove((x,y))

        self.visited = set()
        for r in range(rows):
            for c in range(cols):
                search(r, c, 0)
                
                if self.output:
                    return True
        
        return False