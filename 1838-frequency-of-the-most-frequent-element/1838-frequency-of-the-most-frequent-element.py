class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        prefixes = [0]
        for num in nums:
            prefixes.append(prefixes[-1] + num)

        left = 0
        output = 1

        for right in range(len(nums)):
            target = nums[right]
            total = prefixes[right + 1] - prefixes[left]
            needed = (right - left + 1) * target

            while needed - total > k:
                left += 1
                total = prefixes[right + 1] - prefixes[left]
                needed = (right - left + 1) * target

            output = max(output, right - left + 1)

        return output