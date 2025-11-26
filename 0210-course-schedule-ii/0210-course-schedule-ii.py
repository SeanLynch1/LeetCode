class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        mapping = defaultdict(set)
        visited = [0] * numCourses

        pre = []
        suff = []

        for slot in prerequisites:
            mapping[slot[0]].add(slot[1])

            if slot[1] not in mapping:
                mapping[slot[1]] = set()

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

            res.append(start)
            return True

        
        for n in range(numCourses):
            if n not in mapping:
                pre.append(n)
            else:
                res = []

                output = helper(n)
                
                if not output:
                    return []
                else:
                    suff.extend(res)

        pre.extend(suff)

        return pre
