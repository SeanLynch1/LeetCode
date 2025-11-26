class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        mapping = defaultdict(dict)
        res = []

        for i in range(len(equations)):
            
            mapping[equations[i][0]][equations[i][1]] = values[i]

            mapping[equations[i][1]][equations[i][0]] = 1 / values[i]

        # traverse mapping
        def helper(start, end, product):
            if end in mapping[start]:
                return product * mapping[start][end]
            elif start == end:
                return 1
            elif start in visited:
                return -1

            visited.add(start)
            for key, val in mapping[start].items():
                print(key, val, f"end = {end}")
                output = helper(key, end, product * val)

                if output != -1:
                    return output

            return -1

        for s, e in queries:
            visited = set()
            if s not in mapping or e not in mapping:
                res.append(-1)
            else:
                res.append(helper(s, e, 1))

        return res