class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        
        if not bank:
            return -1

        bank = set(bank) 

        visited = set([startGene])
        queue = deque([startGene])
        mutations = 0

        while queue:
            for genes in range(len(queue)):
                curr = queue.popleft()

                if curr == endGene:
                    return mutations

                for gene in bank:
                    diff = 0

                    if gene not in visited:
                        for i in range(len(gene)):
                            if curr[i] != gene[i]:
                                diff += 1
                            
                            if diff == 2:
                                break
                        
                        if diff == 1:
                            queue.append(gene)
                            visited.add(gene)
            
            mutations += 1
        return -1
