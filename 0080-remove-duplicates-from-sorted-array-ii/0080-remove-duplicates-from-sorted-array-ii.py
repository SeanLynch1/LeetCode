class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 1
        left = 1

        for right in range(1, len(nums)):
            
            if nums[right] != nums[right - 1]:
                count = 1
            else:
                count += 1

            if count <= 2:
                nums[left] = nums[right]
                left += 1

        return left
