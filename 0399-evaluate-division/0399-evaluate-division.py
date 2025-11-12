class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        mapping = {}
        output = []

        # build query mapping
        for i in range(len(equations)):
            
            var_0 = equations[i][0]
            var_1 = equations[i][1]

            if var_0 not in mapping:
                # initalise new query
                mapping[var_0] = {}

            mapping[var_0][var_1] = values[i]
            
            if var_1 not in mapping:
                mapping[var_1] = {}

            mapping[var_1][var_0] = 1 / values[i]

        def helper(start: str, target: str, visited: set, product: float) -> float:
            if start == target:
                return product

            visited.add(start)
            
            for key, value in mapping[start].items():
                if key in visited:
                    continue

                output = helper(key, target, visited, product * value)

                if output != -1: return output
            
            return -1

        for j in range(len(queries)):
            
            var_0 = queries[j][0]
            var_1 = queries[j][1]

            if var_0 not in mapping or var_1 not in mapping:
                output.append(-1)
                continue

            visited = set()
            output.append(helper(var_0, var_1, visited, 1))

        return output