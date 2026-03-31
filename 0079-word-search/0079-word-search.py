class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        rows = len(board)
        cols = len(board[0])

        def search(x, y, idx,visited) -> bool:
            
            if idx == len(word):
                return True

            if x < 0 or y < 0 or x >= rows or y >= cols:
                return False

            if board[x][y] != word[idx]:
                return False
            
            if (x, y) in visited:
                return False

            visited.add((x,y))

            # right
            if search(x, y + 1, idx + 1,visited):
                return True

            # down
            if search(x + 1, y, idx + 1,visited):
                return True

            # left
            if search(x, y - 1, idx + 1,visited):
                return True

            # up
            if search(x - 1, y, idx + 1, visited):
                return True

            visited.remove((x,y))

        for r in range(rows):
            for c in range(cols):
                if search(r, c, 0, set()):
                    return True
        
        return False