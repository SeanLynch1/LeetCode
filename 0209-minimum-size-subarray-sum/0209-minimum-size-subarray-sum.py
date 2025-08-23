class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        n = len(nums)
        left = 0

        sum_window = 0
        min_length = float("inf")

        for right in range(n):
            sum_window += nums[right]

            while sum_window >= target:
                min_length = min(min_length, right - left + 1)
                sum_window -= nums[left]
                left += 1

        return 0 if min_length == float("inf") else min_length
                
