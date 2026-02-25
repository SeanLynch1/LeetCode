class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 1

        left = 1
        last = nums[0]

        for right in range(1, len(nums)):

            if nums[right] != last:
                nums[left] = nums[right]
                left += 1
                last = nums[right]

        return left