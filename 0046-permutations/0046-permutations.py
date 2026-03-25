class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        output = []
        used = [False] * len(nums)

        def back_track(path: List):

            if len(path) == len(nums):
                output.append(path.copy())
                return

            for i in range(len(nums)):
                
                if used[i]:
                    continue
                
                path.append(nums[i])
                used[i] = True

                back_track(path)                
                
                used[i] = False
                path.pop()

        back_track([])

        return output