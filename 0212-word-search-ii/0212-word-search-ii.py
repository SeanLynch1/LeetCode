class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        trie = TrieNode()
        output = []
        rows = len(board)
        cols = len(board[0])
        # create trie
        for word in words:
            curr = trie
            for l in word:

                if l not in curr.children:
                    curr.children[l] = TrieNode()

                curr = curr.children[l]
            
            curr.word = word

        
        # dfs the board, referencing the trie
        def dfs(curr: TrieNode, x : int, y : int):

            l = board[x][y]

            if l not in curr.children:
                return
            
            if curr.children[l].word != None:
                output.append(curr.children[l].word)
                curr.children[l].word = None
            
            # prevent looping with snaking back to same tile
            board[x][y] = "#"

            # up
            if x - 1 >= 0:
                dfs(curr.children[l], x - 1, y)
            # left
            if y - 1 >= 0:
                dfs(curr.children[l],x, y - 1)
            # right
            if y + 1 < cols:
                dfs(curr.children[l],x, y + 1)
            # down
            if x + 1 < rows:
                dfs(curr.children[l],x + 1, y)

            board[x][y] = l

            return 

        for r in range(rows):
            for c in range(cols):
                dfs(trie, r, c)
                
        return output