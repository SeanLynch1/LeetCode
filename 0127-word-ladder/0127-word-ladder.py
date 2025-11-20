class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        mapping = defaultdict(list)
        queue = deque([beginWord])
        visited = {beginWord}

        for word in wordList:
            for i in range(len(word)):
                temp = list(word)
                temp[i] = "*"

                mapping["".join(temp)].append(word)

        def compare(x: str, y: str) -> bool:

            diff = 0
            for i in range(len(x)):
                if x[i] != y[i]:
                    diff += 1
                    if diff > 1:
                        return False
            
            return True

        steps = 1
        while queue:

            for i in range(len(queue)):
                curr = queue.popleft()

                if curr == endWord:
                    return steps

                for i in range(len(curr)):
                    temp = list(curr)
                    temp[i] = "*"

                    for word in mapping["".join(temp)]:
                        if word != curr and word not in visited and compare(curr, word):
                            queue.append(word)
                            visited.add(word)
            
            steps += 1

        return 0

