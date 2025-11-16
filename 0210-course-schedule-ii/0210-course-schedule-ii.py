class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        output = []
        visited = [0] * numCourses
        found = set()
        for course_1, course_2 in prerequisites:
            graph[course_1].append(course_2)
        
        def helper(start: int) -> bool:
            print(f"start = {start}")
            if visited[start] == 2 or len(graph[start]) == 0:
                return True
            elif visited[start] == 1:
                print(f"visited = {visited}")
                print("FAILED")
                return False

            visited[start] = 1
            res = True

            for val in graph[start]:
                res = helper(val)

                if res == False:
                    return res

                
            visited[start] = 2
            print(f"visited = {visited}")

            return res


        # loop through
        for key, value in prerequisites:
            
            if value in found:
                continue

            print(f"testing with key = {key}, value = {value}")
            res = helper(value)
            
            if res == False:
                return []
            
            output.extend([value])
            found.add(value)
            print(f"output = {output}")
            print(f"visited = {visited}")
            print("\n")

        for i in range(len(visited)):
            if visited[i] == 0:
                if i not in found:
                    output.extend([i])
        return output