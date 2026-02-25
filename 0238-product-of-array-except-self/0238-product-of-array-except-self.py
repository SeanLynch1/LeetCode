class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefixes = [1]

        for i in range(1, len(nums)):
            prefixes.append(prefixes[-1] * (nums[i-1]))

        last = 1
        for j in range(len(nums)-1,-1,-1):
            prefixes[j] *= last
            last *= nums[j]

        return prefixes