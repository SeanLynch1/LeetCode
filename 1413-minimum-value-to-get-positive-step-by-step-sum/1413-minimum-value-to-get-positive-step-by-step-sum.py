class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        
        ans = 1
        lowest = float('inf')
        vals = [0]
        for num in nums:
            total = num + vals[-1]
            vals.append(total)
            lowest = min(lowest, total)
        
        if lowest < 0:
            ans += abs(lowest)

        return ans