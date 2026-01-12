class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        mapping = defaultdict(list)
        visited = defaultdict(int)

        for x, y in prerequisites:
            mapping[x].append(y)

        def dfs(num: int) -> bool:
            
            if num not in mapping:
                return True

            if visited[num] == 1:
                return False
            elif visited[num] == 2:
                return True

            visited[num] = 1
            
            for n in mapping[num]:
                if not dfs(n):
                    return False

            visited[num] = 2

            return True
        

        for i in range(numCourses):
            outcome = dfs(i)

            if not outcome:
                return False

        return True