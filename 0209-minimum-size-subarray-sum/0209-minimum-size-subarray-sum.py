class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        output = 0
        left = 0
        summation = 0

        for right in range(len(nums)):
            summation += nums[right]

            while summation >= target:
                
                if right - left < output or output == 0:
                    output = right - left + 1

                summation -= nums[left]
                left += 1
        
        return output


