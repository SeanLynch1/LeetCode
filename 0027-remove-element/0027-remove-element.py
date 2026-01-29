class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0

        left = 0
        right = len(nums) - 1

        while left <= right:

            if nums[left] == val:
                while left < right and nums[right] == val:
                    right -= 1
                

                if left > right:
                    break

                nums[left] = nums[right]

                right -= 1
            else:
                left += 1
        
        return right + 1