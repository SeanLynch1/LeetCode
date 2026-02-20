class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        
        longest = 1
        count = 1
        left = 0
        bit_start = nums[0]

        for right in range(1, len(nums)):
            
            while nums[right] & bit_start != 0:

                bit_start ^= nums[left]

                left += 1
                count -= 1
            bit_start |= nums[right]

            count += 1
            longest = max(count, longest)

        return longest