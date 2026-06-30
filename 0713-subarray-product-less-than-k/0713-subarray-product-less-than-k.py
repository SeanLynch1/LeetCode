class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        
        # 10 5  2   6
        # 10 50 100 600

        #398079944
        #194239825
        total = 0
        curr = 1
        left = 0

        for right in range(len(nums)):
            curr *= nums[right]

            while left <= right and curr >= k:
                curr //= nums[left]
                left += 1

            total += right - left + 1

        return total