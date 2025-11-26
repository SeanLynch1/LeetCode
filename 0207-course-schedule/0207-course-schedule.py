class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        mapping = defaultdict(set)
        visited = defaultdict(int)

        for slot in prerequisites:
            mapping[slot[0]].add(slot[1])
            mapping[slot[0]].add(slot[1]) 

        def helper(start) -> bool:
            
            if visited[start] == 1:
                return False
            elif visited[start] == 2:
                return True

            visited[start] = 1
            for val in mapping[start]:
                if not helper(val):
                    return False

            visited[start] = 2

            return True

        for n in range(0, numCourses):
            if n in mapping:
                res = helper(n)

                if not res:
                    return False

        return True