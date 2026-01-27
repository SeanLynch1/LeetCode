class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        prefixes = [1]
        for i in range(1, n):
            prefixes.append(nums[i - 1] * prefixes[-1])

        last = 1
        for j in range(n-1,-1,-1):
            prefixes[j] *= last
            last *= nums[j]

        return prefixes