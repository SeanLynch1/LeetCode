class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        

        longest = 0
        bank = k
        left = 0

        for right in range(len(nums)):

            if nums[right] != 1:

                bank -= 1

                while bank < 0:

                    if nums[left] == 0:
                        bank += 1

                    left += 1

            longest = max(longest, right + 1 - left)

        return longest