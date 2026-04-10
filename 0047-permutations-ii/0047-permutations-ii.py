class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        self.output = []
        used = [False for _ in range(len(nums))]

        def back_track(path: List) -> None:

            if len(path) == len(nums):
                self.output.append(path.copy())
                return

            for i in range(len(nums)):

                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue

                if not used[i]:
                    last = nums[i]

                    path.append(nums[i])

                    used[i] = True
                    
                    back_track(path)
                    

                    path.pop()
                    used[i] = False
                
            return

        back_track([])

        return self.output