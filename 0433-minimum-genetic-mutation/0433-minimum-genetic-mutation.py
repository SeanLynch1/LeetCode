class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        
        # need to build a graph
        queue = deque([startGene])
        visited = set()
        
        def compare(x: str, y: str) -> bool:
            diff = 0
            for i in range(len(x)):
                if x[i] != y[i]:
                    diff += 1
                    if diff > 1:
                        return False
            return True

        steps = 0
        while queue:
            for i in range(len(queue)):
                curr = queue.popleft()

                if curr == endGene:
                    return steps

                for gene in bank:
                    if gene not in visited:
                        diff = compare(curr, gene)

                        if diff:
                            queue.append(gene)
                            visited.add(gene)
            steps += 1

        return -1

            
