class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        if endWord not in wordList:
            return 0
        mapping = defaultdict(list)
        queue = deque([beginWord])
        visited = {beginWord}
        L = len(beginWord)
        for word in wordList:
            for i in range(L):
                mapping[word[:i] + "*" + word[i+1:]].append(word)

        steps = 1
        while queue:

            for i in range(len(queue)):
                curr = queue.popleft()

                if curr == endWord:
                    return steps

                for i in range(L):
                    for word in mapping[curr[:i] + "*" + curr[i+1:]]:
                        if word not in visited:
                            queue.append(word)
                            visited.add(word)
            
            steps += 1

        return 0

