class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        max_reach = 0

        for i in range(len(nums)):
            
            # if we have surpassed the max reach i.e gone where we coldn't reach
            if i > max_reach:
                return False

            # represents the farthest cell we can go to
            max_reach = max(max_reach, nums[i] + i)

            if max_reach >= len(nums) - 1:
                return True

        return True
