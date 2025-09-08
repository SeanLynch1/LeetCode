class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixes = [1]
        prefix = 1
        suffix = 1

        for i in range(1, len(nums)):
            prefix *= nums[i - 1]
            prefixes.append(prefix)

        for j in range(len(nums)- 1,-1,-1):
            prefixes[j] = prefixes[j] * suffix
            suffix *= nums[j]

        return prefixes