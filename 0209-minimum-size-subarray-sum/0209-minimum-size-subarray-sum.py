class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        output = 0
        start, end, left, right = 0, 0, 0, 0
        summation = 0

        for right in range(len(nums)):
            summation += nums[right]

            while summation >= target:
                
                if right - left < end - start or end == 0:
                    start, end = left, right
                    output = end - start + 1

                summation -= nums[left]
                left += 1
        
        return output


