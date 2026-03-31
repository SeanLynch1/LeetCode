class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()

        visited = set()
        output = []
        def back_track(start, curr, path: List):

            if curr == target:
                if tuple(path) not in visited:
                    output.append(path.copy())
                    visited.add(tuple(path))
                return

            if curr > target:
                return
                

            for i in range(start, len(candidates)):

                val = candidates[i]

                path.append(val)
                back_track(i + 1, curr + val, path)
                path.pop()

        back_track(0, 0, [])
        return output