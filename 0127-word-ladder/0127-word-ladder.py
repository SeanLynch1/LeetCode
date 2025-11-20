class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        mapping = defaultdict(list)
        queue = deque([beginWord])
        visited = {beginWord}
        L = len(beginWord)
        for word in wordList:
            for i in range(L):
                temp = word[:i] + "*" + word[i+1:]
                mapping[temp].append(word)

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

