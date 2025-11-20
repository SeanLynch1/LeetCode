class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        if endWord not in wordList:
            return 0

        mapping = defaultdict(list)
        L = len(beginWord)

        for word in wordList:
            for i in range(L):
                mapping[word[:i] + "*" + word[i+1:]].append(word)

        queue = deque([beginWord])
        visited = {beginWord}
        steps = 1

        while queue:

            for i in range(len(queue)):
                curr = queue.popleft()

                if curr == endWord:
                    return steps

                for i in range(L):
                    temp = curr[:i] + "*" + curr[i+1:]
                    for word in mapping[temp]:
                        if word not in visited:
                            queue.append(word)
                            visited.add(word)
            
            steps += 1

        return 0

