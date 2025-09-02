class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        end = len(nums)
        left, right = 0, len(nums) - 1

        while left <= right:
            if nums[right] == val:
                nums[right] = "_"
                end = right

                right -= 1
            elif nums[left] == val:
                nums[left] = nums[right]
                nums[right] = "_"
                end = right

                right -= 1
                left += 1
            else:
                left += 1

        k = nums[:end]

        print(k)

        return len(k)
                
    