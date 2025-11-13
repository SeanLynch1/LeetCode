class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        # build a graph
        graph = {}
        output = []

        for i in range(len(equations)):

            var_1 = equations[i][0]
            var_2 = equations[i][1]

            if var_1 not in graph:
                graph[var_1] = {}

            graph[var_1][var_2] = values[i]

            if var_2 not in graph:
                graph[var_2] = {}
            
            graph[var_2][var_1] = 1 / values[i]

        # create a helper function to search through graph
        def helper(start: str, target: str, visited: set, product: float) -> float:
            if start == target:
                return product

            if start not in visited:
                visited.add(start)

            for divisor, value in graph[start].items():
                if divisor in visited:
                    continue

                res = helper(divisor, target, visited, product * value)

                if res != -1:
                    return res

            return -1

        for numerator, denomenator in queries:
            if numerator not in graph or denomenator not in graph:
                output.append(-1)
            else:
                visited = set()
                output.append(helper(numerator, denomenator, visited, 1))

        return output
