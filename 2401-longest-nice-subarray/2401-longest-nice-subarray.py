class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        bitmask = 0
        left = 0
        longest = 0

        for right in range(len(nums)):

            # If there is overlap, contract from the left
            while bitmask & nums[right] != 0:
                bitmask ^= nums[left]  # remove left number's bits
                left += 1

            # Add this number to the window
            bitmask |= nums[right]

            longest = max(longest, right - left + 1)

        return longest