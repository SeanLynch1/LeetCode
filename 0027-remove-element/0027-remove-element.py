class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        left = 0  # Pointer for where the next non-val element goes

        for right in range(len(nums)):
            if nums[right] != val:
                nums[left] = nums[right]
                left += 1

        return left  # left is the new length
