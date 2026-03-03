class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        
        rows = len(board)
        cols = len(board[0])

        word_len = len(word)
        # check down each column
        for y in range(cols):
            found = 0
            needs_reset = False
            for x in range(rows):
                if board[x][y] == "#":
                    needs_reset = False
                    if found != word_len:
                        found = 0
                    else:
                        return True
                elif found >= word_len:
                    found = 0
                elif board[x][y] != ' ' and board[x][y] != word[found]:
                    needs_reset = True

                if not needs_reset:
                    if board[x][y] == ' ' or board[x][y] == word[found]:
                        found += 1
                    else:
                        found = 0

                    if found >= word_len:
                        needs_reset = True
                    
            if found == word_len:
                return True

        # check up each column
        for y in range(cols):
            found = 0
            needs_reset = False
            for x in range(rows-1,-1,-1):
                if board[x][y] == "#":
                    needs_reset = False
                    if found != word_len:
                        found = 0
                    else:
                        return True
                elif found >= word_len:
                    found = 0
                elif board[x][y] != ' ' and board[x][y] != word[found]:
                    needs_reset = True

                if not needs_reset:
                    if board[x][y] == ' ' or board[x][y] == word[found]:
                        found += 1
                    else:
                        found = 0

                    if found >= word_len:
                        needs_reset = True
                    
            if found == word_len:
                return True

        # check right across each column
        for x in range(rows):
            found = 0
            needs_reset = False
            for y in range(cols):
                if board[x][y] == "#":
                    needs_reset = False
                    if found != word_len:
                        found = 0
                    else:
                        return True
                elif found >= word_len:
                    found = 0

                elif board[x][y] != ' ' and board[x][y] != word[found]:
                    needs_reset = True
                    
                if not needs_reset:
                    if board[x][y] == ' ' or board[x][y] == word[found]:
                        found += 1
                    else:
                        found = 0

                    if found >= word_len:
                        needs_reset = True
                    
            if found == word_len:
                return True

        # check left across each column
        for x in range(rows):
            found = 0
            needs_reset = False
            for y in range(cols-1,-1,-1):
                if board[x][y] == "#":
                    needs_reset = False
                    if found != word_len:
                        found = 0
                    else:

                        return True
                elif found >= word_len:
                    found = 0

                elif board[x][y] != ' ' and board[x][y] != word[found]:
                    needs_reset = True

                if not needs_reset:
                    if board[x][y] == ' ' or board[x][y] == word[found]:
                        found += 1
                    else:
                        found = 0

                    if found >= word_len:
                        needs_reset = True
                    
            if found == word_len:
                return True

        return False

        

            


