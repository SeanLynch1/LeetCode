class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not wordList:
            return 0
        

        wordList = set(wordList)

        if endWord not in wordList:
            return 0

        queue = deque([beginWord])

        letters = "abcdefghijklmnopqrstuvwxyz"
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
                            
                            if find in wordList:
                                queue.append(find)
                                wordList.remove(find)

            moves += 1

        return 0