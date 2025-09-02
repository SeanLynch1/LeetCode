class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        left, right = 0, len(nums) - 1

        while left <= right:
            if nums[right] == val:
                right -= 1
            elif nums[left] == val:
                nums[left] = nums[right]

                right -= 1
                left += 1
            else:
                left += 1


        return left
                
    