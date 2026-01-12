class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        mapping = defaultdict(list)
        visited = [0] * numCourses

        order = []

        for a,b  in prerequisites:
            mapping[a].append(b)


        def helper(start) -> bool:

            if visited[start] == 1:
                return False
            if visited[start] == 2:
                return True

            visited[start] = 1

            for val in mapping[start]:
                if not helper(val):
                    return False
            
            visited[start] = 2

            order.append(start)
            return True

        
        for n in range(numCourses):
            if not helper(n):
                return []

        return order
