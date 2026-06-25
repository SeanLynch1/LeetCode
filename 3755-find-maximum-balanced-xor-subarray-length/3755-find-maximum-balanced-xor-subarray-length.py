class Solution:
    def maxBalancedSubarray(self, nums: List[int]) -> int:
        max_len = 0
        mapping = {(0, 0): 0}
        odds = 0
        xor_val = 0

        for i in range(len(nums)):
            num = nums[i]
            if num % 2 == 1:
                odds += 1
            else:
                odds -= 1

            xor_val ^= num
            state = (xor_val, odds)

            if state not in mapping:
                mapping[state] = i + 1
            else:
                max_len = max(max_len, i + 1 - mapping[state])

        return max_len