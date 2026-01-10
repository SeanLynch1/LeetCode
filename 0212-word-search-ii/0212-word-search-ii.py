class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        output = set()
        trie = TrieNode()
        rows = len(board)
        cols = len(board[0])

        print(f"rows = {rows}")
        print(f"cols = {cols}")
        
        # build trie
        for word in words:
            curr = trie

            for i in range(len(word)):
                
                l = word[i]

                if l not in curr.children:
                    curr.children[l] = TrieNode()
                
                curr = curr.children[l]

            curr.word = word

        def dfs(curr: TrieNode, x: int, y: int):

            l = board[x][y]
            print(f"current letter = {l}")
            if l not in curr.children:
                return
            
            print("children =", curr.children)
            print("word = ", curr.word)
            if curr.children[l].word is not None:
                output.add(curr.children[l].word)

            # mark visited, if we snake back to the tile later this is a no no
            board[x][y] = "#"

            # check up
            if x - 1 >= 0:
                dfs(curr.children[l], x - 1, y)

            # check left
            if y - 1 >= 0:
                dfs(curr.children[l], x, y - 1)

            # check right
            if y + 1 < cols:
                dfs(curr.children[l], x, y + 1)

            # check down
            if x + 1 < rows:
                dfs(curr.children[l], x + 1, y)

            board[x][y] = l

            return

        for r in range(rows):
            for c in range(cols):
                print(board[r][c])
                dfs(trie, r, c)   
                print("\n")       
            
        return list(output)
                
