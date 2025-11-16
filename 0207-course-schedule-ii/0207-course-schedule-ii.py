class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        output = []
        visited = [0] * numCourses
        for course_1, course_2 in prerequisites:
            graph[course_1].append(course_2)
        
        def helper(start: int) -> bool:
            if visited[start] == 2:
                return True
            elif visited[start] == 1:
                return False

            visited[start] = 1
            res = True

            for val in graph[start]:
                res = helper(val)

                if res == False:
                    return res

            visited[start] = 2
            output.append(start)

            return res

        # loop through
        for value in range(numCourses):
            if visited[value] == 0:
                res = helper(value)
                
                if res == False:
                    return []
        return output