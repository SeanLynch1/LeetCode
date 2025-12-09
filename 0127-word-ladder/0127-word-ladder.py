class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not wordList:
            return 0

        wordList = set(wordList)
        visited = set([beginWord])
        queue = deque([beginWord])

        moves = 1
        while queue:
            for _ in range(len(queue)):

                curr = queue.popleft()

                if curr == endWord:
                    return moves
            
                for word in wordList:
                    diff = 0

                    if word not in visited:
                        for i in range(len(curr)):
                            if word[i] != curr[i]:
                                diff += 1
                            
                            if diff == 2:
                                break
                    
                    if diff == 1:
                        queue.append(word)
                        visited.add(word)

            moves += 1
            print(f"{queue}", "\n")

        return 0

