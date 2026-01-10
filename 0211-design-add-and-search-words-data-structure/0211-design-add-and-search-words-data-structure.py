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
        
        if not node or not node.children:
            return False

        outcome = False
        if word[idx] == ".":
            for next_dict in node.children:
                outcome = self.dfs(node.children[next_dict], word, idx + 1)

                if outcome:
                    return outcome

        elif word[idx] in node.children:
            outcome = self.dfs(node.children[word[idx]], word, idx + 1)

        return outcome

    def search(self, word: str) -> bool:
        node = self.trie

        return self.dfs(node, word, 0)

        
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)