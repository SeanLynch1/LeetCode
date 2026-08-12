class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        
        nums.sort()

        prefixes = 0
        output = 1
        curr = 0
        for i in range(len(nums)):
            target = nums[i]
            prefixes += target

            while ((i + 1 - curr) * target) - prefixes > k:
                prefixes -= nums[curr]
                curr += 1

            output = max(output, i - curr + 1)

        return output