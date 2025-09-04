class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        i = 0
        while i < len(nums) - 1:
            if nums[i] == 0:
                return False
            
            target = nums[i] + i

            cap = min(i + nums[i] + 1, len(nums))
            print("cap = ", cap)
            for j in range(i + 1, cap):
                print("j = ", j)
                if j == len(nums) - 1:
                    return True
                elif nums[j] + j >= target:
                    target = nums[j] + j
                    i = j

        return True
