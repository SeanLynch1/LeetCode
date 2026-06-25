class Solution:
    def maxBalancedSubarray(self, nums: List[int]) -> int:
        max_len = 0
        mapping = defaultdict(dict)
        mapping[0][0] = 0

        odds = 0
        xor_val = 0

        for i in range(len(nums)):
            num = nums[i]
            if num % 2 == 1:
                odds += 1
            else:
                odds -= 1

            xor_val = xor_val ^ num

            if xor_val in mapping[odds]:
                idx = mapping[odds][xor_val]
                max_len = max(max_len, i + 1 - idx)

            if xor_val not in mapping[odds]:
                mapping[odds][xor_val] = i + 1
            
            

        return max_len