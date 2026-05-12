class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        # (0,0),(0,1),
        # (1,0),
        #      ,(2,1),(2,2)

        # (0,0) : (1,0)
        # (1,0) : (0,0)
        # (2,1) : (2,2)
        # (2,2) : (2,1)

        # rows:
        # 0 : (0,0), (0,1)
        # 1 : (1,0)
        # 2 : (2,1), (2,2)

        # cols:
        # 0: (0,0), (1,0)
        # 1: (0,1), (2,1)
        # 2: (2,2)

        rows = defaultdict(list)
        cols = defaultdict(list)

        # set up rows and cols
        for x, y in stones:
            rows[x].append((x,y))
            cols[y].append((x,y))

        visited = set()
        def dfs(x, y):
            
            if (x,y) in visited:
                return

            visited.add((x, y))
            # check rows
            for r, c in rows[x]:
                if (r, c) not in visited:
                    dfs(r, c)

            # check cols
            for r, c in cols[y]:
                if (r, c) not in visited:
                    dfs(r, c)

        output = 0
        for x, y in stones:
            if (x,y) not in visited:
                dfs(x, y)
                output += 1

        return len(stones) - output