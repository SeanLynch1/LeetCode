class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        print(candidates)

        output = []
        def back_track(start, curr, path: List):

            if curr == target:
                output.append(path.copy())
                return

            if curr > target:
                return

            for i in range(start, len(candidates)):
                
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                val = candidates[i]
                print(f"val = {val}, path = {path}")

                path.append(val)
                back_track(i + 1, curr + val, path)
                path.pop()
                

        back_track(0, 0, [])
        return output