class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        mapping = {0:0}

        max_len = 0
        balance = [0]

        for idx in range(len(nums)):
            num = nums[idx]

            val = balance[-1] + (1 if num == 1 else -1)
            balance.append(val)

            if val not in mapping:
                mapping[val] = idx + 1
            else:
                max_len = max(max_len, idx - mapping[val] + 1)
            
        return max_len