class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        mapping = defaultdict(set)
        visited = defaultdict(int)

        for slot in prerequisites:
            mapping[slot[0]].add(slot[1])
            mapping[slot[0]].add(slot[1]) 

        print(mapping)

        def helper(start) -> bool:
            
            if visited[start] == -1:
                return True
            elif visited[start] > 1:
                return False

            # already looped through contents
            if len(mapping[start]) == 0:
                visited[start] = -1
                return True

            visited[start] += 1
            for val in mapping[start]:
                output = helper(val)

                if not output:
                    visited[start] = 2
                    return False

            visited[start] = -1

            return True

        for n in range(0, numCourses):
            if n in mapping:
                res = helper(n)

                if not res:
                    return False

        return True