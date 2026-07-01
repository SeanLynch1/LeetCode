class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int):

        def atMost(k):
            if k < 0:
                return 0

            left = 0
            curr = 0
            total = 0

            for right in range(len(nums)):
                curr += nums[right]

                while curr > k:
                    curr -= nums[left]
                    left += 1

                total += right - left + 1

            return total

        return atMost(goal) - atMost(goal - 1)