class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        mapping = defaultdict(list)
        mapping[0] = [0]
        
        max_len = 0
        balance = [0]

        for idx in range(len(nums)):
            val = balance[-1] + (1 if nums[idx] == 1 else -1)
            balance.append(val)
            mapping[val].append(idx + 1)
        
        for key, val in mapping.items():
            max_len = max(max_len, val[-1] - val[0])
            
        return max_len