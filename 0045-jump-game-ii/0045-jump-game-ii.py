class Solution:
    def jump(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return 0

        i = 1
        jumps = 1
        current_jump = 0 + nums[0]

        while current_jump < len(nums) - 1:
            for j in range(i, current_jump + 1):
                if nums[j] + j > current_jump:
                    current_jump = nums[j] + j
                    i = j
                    
            jumps += 1

        return jumps

