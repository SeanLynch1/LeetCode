class Solution:
    def maxBalancedSubarray(self, nums: List[int]) -> int:
        mapping = {(0, 0): 0}
        xor_val = odds = max_len = 0

        for i, num in enumerate(nums):
            odds += 1 if num & 1 else -1

            xor_val ^= num
            state = (xor_val, odds)

            if state not in mapping:
                mapping[state] = i + 1
            else:
                max_len = max(max_len, i + 1 - mapping[state])

        return max_len