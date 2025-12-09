class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not wordList:
            return 0

        wordList = set(wordList)
        visited = set([beginWord])
        queue = deque([beginWord])

        letters = set()

        for word in wordList:
            for w in word:
                if w not in letters:
                    letters.add(w)

        moves = 1
        while queue:
            for _ in range(len(queue)):

                curr = queue.popleft()

                if curr == endWord:
                    return moves
            

                for i in range(len(curr)):
                    for c in letters:
                        if curr[i] != c:
                            find = curr[:i] + c + curr[i + 1:]
                            
                            if find in wordList and find not in visited:
                                queue.append(find)
                                visited.add(find)

            moves += 1

        return 0