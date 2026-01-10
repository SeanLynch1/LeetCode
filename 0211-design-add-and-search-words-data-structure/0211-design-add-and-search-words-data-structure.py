class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            node = node.children.setdefault(ch, TrieNode())
        node.is_word = True

    def dfs(self, node: TrieNode, word: str, idx: int) -> bool:
        if idx == len(word):
            return node.is_word

        ch = word[idx]

        if ch == ".":
            for child in node.children.values():
                if self.dfs(child, word, idx + 1):
                    return True
            return False
        else:
            if ch not in node.children:
                return False
            return self.dfs(node.children[ch], word, idx + 1)

    def search(self, word: str) -> bool:
        node = self.root

        for i, ch in enumerate(word):
            if ch == ".":
                return self.dfs(node, word, i)
            if ch not in node.children:
                return False
            node = node.children[ch]

        return node.is_word
