class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixes = [1]
        prefix = 1

        suffixes = [1] * len(nums)
        suffix = 1

        for i in range(1, len(nums)):
            prefix *= nums[i - 1]
            prefixes.append(prefix)

        for j in range(len(nums)- 1,-1,-1):
            suffixes[j] = prefixes[j] * suffix
            suffix *= nums[j]

        return suffixes