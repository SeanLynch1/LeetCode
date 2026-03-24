class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        output = []


        def back_track(start: int):

            if start == len(nums):
                output.append(nums.copy())
                return


            for i in range(start, len(nums)):
                
                nums[start], nums[i] = nums[i], nums[start]

                back_track(start + 1)
                
                nums[start], nums[i] = nums[i], nums[start]

        back_track(0)

        return output