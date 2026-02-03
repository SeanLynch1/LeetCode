class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        temp = 1
        n = nums[0]
        max_sequence = 0
        nums.sort()

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                temp += 1

                if temp > max_sequence:
                    n = nums[i]
                    max_sequence = temp

            else:
                temp = 1

            

        return n