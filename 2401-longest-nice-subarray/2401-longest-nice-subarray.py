class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        
        longest = 0

        for i, ch in enumerate(nums):
            

            count = 1

            bit_start = nums[i]

            right = i + 1

            while right < len(nums) and nums[right] & bit_start == 0:
                
                bit_start |= nums[right]
                
                count += 1
                right += 1

            longest = max(count, longest)


        return longest