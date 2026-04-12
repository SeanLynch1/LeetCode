class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []

        def back_track(path: List, start: int):
            res.append(path.copy())
            
            for i in range(start, len(nums)):

                path.append(nums[i])

                back_track(path, i + 1)
                
                path.pop()

            return
        back_track([], 0)

        return res