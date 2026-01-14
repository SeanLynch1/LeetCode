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

        def findValue(visited: set, start: str, target: str, value: int) -> bool:
            
            if start not in mapping or target not in mapping:
                return False

            if start == target:
                output.append(value)
                return True

            visited.add(start)

            for options in mapping[start]:

                s = options[0]
                v = options[1]

                if s not in visited:
                    if findValue(visited, s, target, value * v):
                        return True

            return False

        for n, d in queries:
            if not findValue(set(), n, d, 1):
                output.append(-1)

        return output