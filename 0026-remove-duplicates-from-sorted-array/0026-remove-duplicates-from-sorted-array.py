class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        left = 0
        temp = 0
        n = len(nums) - 1

        while temp < n:
            
            if nums[temp] == nums[left]:
                while temp < n and nums[temp] == nums[left]:
                    temp += 1
                
                if nums[left] == nums[temp]:
                    break

                left += 1
                nums[left] = nums[temp]
            else:
                left += 1
            
        return left + 1
                


