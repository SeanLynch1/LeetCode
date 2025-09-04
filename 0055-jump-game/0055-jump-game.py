class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        i = 0
        while i < len(nums) - 1:
            if nums[i] == 0:
                return False
            
            target = nums[i] + i

            for j in range(i + 1, i + nums[i] + 1):

                if j >= len(nums) - 1:
                    return True
                elif nums[j] + j >= target:
                    target = nums[j] + j
                    i = j

        return True
