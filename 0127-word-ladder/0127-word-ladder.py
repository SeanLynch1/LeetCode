from collections import deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0

        beginSet = {beginWord}
        endSet = {endWord}
        visited = set([beginWord, endWord])
        letters = "abcdefghijklmnopqrstuvwxyz"
        moves = 1

        while beginSet and endSet:
            # Always expand the smaller frontier
            if len(beginSet) > len(endSet):
                beginSet, endSet = endSet, beginSet

            nextLevel = set()
            for word in beginSet:
                for i in range(len(word)):
                    for c in letters:
                        if word[i] != c:
                            newWord = word[:i] + c + word[i+1:]
                            if newWord in endSet:
                                return moves + 1
                            if newWord in wordSet and newWord not in visited:
                                visited.add(newWord)
                                nextLevel.add(newWord)
            beginSet = nextLevel
            moves += 1

        return 0
