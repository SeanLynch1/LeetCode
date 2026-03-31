class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        self.output = False

        self.rows = len(board)
        self.cols = len(board[0])

        def search(x, y, idx, visited):
            
            if idx == len(word):
                self.output = True
                return

            if x < 0 or y < 0 or x >= self.rows or y >= self.cols:
                return
                
            print(x,y, idx)
            if board[x][y] != word[idx]:
                return
            
            if (x, y) in visited:
                return

            visited.add((x,y))

            # right
            search(x, y + 1, idx + 1,visited)

            # down
            search(x + 1, y, idx + 1,visited)

            # left
            search(x, y - 1, idx + 1, visited)

            # up
            search(x - 1, y, idx + 1, visited)

            visited.remove((x,y))


        for r in range(self.rows):
            for c in range(self.cols):
                search(r, c, 0, set())
                
                if self.output:
                    return True
        
        return False