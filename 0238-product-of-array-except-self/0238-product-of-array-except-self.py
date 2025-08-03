class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefixes = [1] * n
        curr_prfx = 1
        curr_sfx = 1

        for i in range(1, n):
            curr_prfx *= nums[i-1]
            prefixes[i] = curr_prfx
        
        for i in range(n-1,-1,-1):
            prefixes[i] = curr_sfx * prefixes[i]
            curr_sfx *= nums[i]

        return prefixes
