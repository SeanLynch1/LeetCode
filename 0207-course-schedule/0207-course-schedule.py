class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = {}
        visited = [0] * numCourses
        # build graph
        for course_1, course_2 in prerequisites:
            
            if course_1 not in graph:
                graph[course_1] = []

            if course_2 not in graph:
                graph[course_2] = []

            graph[course_1].append(course_2)

        # define helper funciton to loop through graph

        def helper(start: int) -> bool:
            if len(graph[start]) == 0 or visited[start] == 2:
                return True
            elif visited[start] == 1:
                return False

            visited[start] = 1
            for val in graph[start]:
                outcome = helper(val)
                if outcome == False:
                    return outcome
                    
            visited[start] = 2
            return True

        for idx in prerequisites:
            res = helper(idx[1])

            if not res:
                return False
            
        return True