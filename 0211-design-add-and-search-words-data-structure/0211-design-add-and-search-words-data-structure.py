class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class WordDictionary:

    def __init__(self):
        self.trie = TrieNode()

    def addWord(self, word: str) -> None:
        
        node = self.trie

        for l in word:
            if l not in node.children:
                node.children[l] = TrieNode()
            
            node = node.children[l]
        
        node.is_word = True

    def dfs(self, node: TrieNode, word: str, idx: int) -> bool:
        if idx == len(word):
            return node.is_word
        
        for val, next_dict in node.children.items():
            if val == word[idx] or word[idx] == ".":
                outcome = self.dfs(next_dict, word, idx + 1)

                if outcome:
                    return outcome

        return False

    def search(self, word: str) -> bool:
        node = self.trie

        for i in range(len(word)):
            l = word[i]
            
            if l == ".":
                return self.dfs(node, word, i)
            elif l not in node.children:
                return False

            node = node.children[l]
        
        return node.is_word
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)