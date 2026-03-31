class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        output =  []
        trie = defaultdict(dict)
        rows = len(board)
        cols = len(board[0])

        for idx, word in enumerate(words):
            curr = trie
            for i in range(len(word)):
                l = word[i]
                if l not in curr:
                    curr[l] = {}

                curr = curr[l]
            curr['$'] = word

        def back_track(curr, x, y):
            
            if x < 0 or y < 0 or x == rows or y == cols:
                return

            if board[x][y] == '#':
                return

            if board[x][y] not in curr:
                return
                
            temp = board[x][y]
            curr = curr[temp]

            if '$' in curr:
                output.append(curr['$'])
                del curr['$']
            
            # mark as visited
            board[x][y] = '#'

            dirs = [(0,1),(1,0),(0,-1),(-1,0)]

            for h, v in dirs:
                back_track(curr, x + h, y + v)

            board[x][y] = temp

        for r in range(rows):
            for c in range(cols):
                back_track(trie, r, c)

        return output