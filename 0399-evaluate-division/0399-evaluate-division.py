class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        mapping = defaultdict(list)
        output = []

        for i in range(len(values)):
            n, d = equations[i][0], equations[i][1]
            v = values[i]

            mapping[n].append((d, v))
            mapping[d].append((n, 1 / v))

        # traverse mapping

        def findValue(visited: set, start: str, target: str, value: int) -> int:
            
            if start == target:
                return value

            visited.add(start)
            output = -1

            for options in mapping[start]:

                s = options[0]
                v = options[1]

                if s not in visited:
                    output = findValue(visited, s, target, value * v)
                    
                    if output != -1:
                        return output

            return -1

        for n, d in queries:
            if n not in mapping or d not in mapping:
                output.append(-1)
            else: output.append(findValue(set(), n, d, 1))

        return output