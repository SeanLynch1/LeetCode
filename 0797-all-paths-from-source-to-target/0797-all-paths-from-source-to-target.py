class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        res = []
        print(graph[0])

        for val in graph[0]:
            print(f"val = {val}")

        def dfs(i:int, path: List[int]) -> None:

            if i == len(graph) - 1:
                res.append(path.copy())

            for node in graph[i]:
                print(f"node = {node}")
                
                path.append(node)
                dfs(node, path)
                path.pop()

        dfs(0,[0])
        return res