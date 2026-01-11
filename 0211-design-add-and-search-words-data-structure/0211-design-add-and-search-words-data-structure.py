class TrieNode:
    def __init__ (self):
        self.children = {}
        self.is_word = False

class WordDictionary:

    def __init__(self):
        self.trie = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.trie

        for l in word:
            if l not in curr.children:
                curr.children[l] = TrieNode()
            
            curr = curr.children[l]
        
        curr.is_word = True

    def search(self, word: str) -> bool:
        
        # dfs the trie
        def dfs(curr: TrieNode, idx: int) -> bool:
            
            print(f"word = {word}")
            print(f"curr = {curr.is_word}")
            if idx == len(word):
                return curr.is_word

            l = word[idx]
            print(f"current letter = {l}")
            outcome = False

            if l != ".":
                if l not in curr.children:
                    return False

                print("we've gone here")
                outcome = dfs(curr.children[l], idx + 1)
            else:
                
                print(curr.children)
                for val in curr.children:
                    print(val)
                    outcome = dfs(curr.children[val], idx + 1)

                    if outcome:
                        return True
            

            return outcome


        return dfs(self.trie, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)