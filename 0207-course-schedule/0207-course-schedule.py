from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[course].append(prereq)

        visited = [0] * numCourses  # 0 = unvisited, 1 = visiting, 2 = visited

        def dfs(course):
            if visited[course] == 1:  # cycle detected
                return False
            if visited[course] == 2:  # already checked, safe
                return True

            visited[course] = 1  # mark as visiting
            for prereq in graph[course]:
                if not dfs(prereq):
                    return False
            visited[course] = 2  # mark as safe
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False

        return True
