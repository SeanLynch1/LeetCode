class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        

        output = []

        def back_track(path: List, total: int, start: int) :

            if total == target:
                output.append(path.copy())
                return
            
            if total > target:
                return

            curr = total
            for i in range(start, len(candidates)):

                if curr + candidates[i] <= target:
                    curr += candidates[i]
                    path.append(candidates[i])

                    back_track(path, curr, i)

                    path.pop()
                    curr -= candidates[i]
                    
        back_track([],0, 0)

        return output