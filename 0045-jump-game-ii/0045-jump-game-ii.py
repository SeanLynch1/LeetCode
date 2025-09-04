class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        farthest = 0
        end = 0
        
        for i in range(len(nums) - 1):  # no need to consider the last index
            farthest = max(farthest, i + nums[i])
            if i == end:  # time to make a jump
                jumps += 1
                end = farthest
                
        return jumps
