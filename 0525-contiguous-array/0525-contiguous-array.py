class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        mapping = {0:0}
        max_len = 0
        balance = 0

        for idx in range(len(nums)):
            balance += (1 if nums[idx] == 1 else -1)

            if balance not in mapping:
                mapping[balance] = idx + 1
            else:
                max_len = max(max_len, idx - mapping[balance] + 1)
            
        return max_len