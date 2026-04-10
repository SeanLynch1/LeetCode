class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        self.output = []

        def back_track(path: List) -> None:

            if len(path) == len(nums):
                self.output.append(path.copy())
                return

            i = 0
            while i < len(nums):
                if nums[i] != '#':
                    last = nums[i]

                    path.append(nums[i])

                    original = nums[i]
                    nums[i] = '#'
                    
                    back_track(path)
                    
                    nums[i] = original
                    path.pop()
                
                i += 1

                while i < len(nums) and nums[i] == nums[i - 1]:
                    i += 1

            return



        back_track([])

        return self.output