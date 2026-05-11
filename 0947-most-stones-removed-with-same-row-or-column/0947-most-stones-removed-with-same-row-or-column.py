from collections import defaultdict

class Solution:
    def removeStones(self, stones):
        n = len(stones)

        row_map = defaultdict(list)
        col_map = defaultdict(list)

        # build mappings
        for i, (r, c) in enumerate(stones):
            row_map[r].append(i)
            col_map[c].append(i)

        visited = set()

        def dfs(i):
            visited.add(i)
            r, c = stones[i]

            # visit all stones in same row
            for nei in row_map[r]:
                if nei not in visited:
                    dfs(nei)

            # visit all stones in same column
            for nei in col_map[c]:
                if nei not in visited:
                    dfs(nei)

        components = 0

        # count connected components
        for i in range(n):
            if i not in visited:
                dfs(i)
                components += 1

        return n - components